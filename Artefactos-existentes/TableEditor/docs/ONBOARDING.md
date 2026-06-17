# TableEditor — Onboarding Guide

## Project Overview

**Name:** TableEditor
**Languages:** HTML/CSS/JS (vanilla), Python, JSON, Markdown, Batch
**Frameworks:** None — intentionally zero dependencies
**Description:** Standalone browser-based multi-table editor (like Excel) with a vanilla JavaScript frontend and a Python stdlib autosave server. No build system, no `pip install`, nothing external.

---

## Architecture Layers

### 1. Frontend Application — `MembrosInfo_Editor.html`
The entire application: ~2300 lines of vanilla JS/HTML/CSS in a single file. Implements an Excel-like grid with inline editing, drag-to-reorder, multi-level sort, hierarchical grouping, field-link nesting, two output formats, a 50-level undo stack, and automatic communication with the autosave server.

### 2. Autosave Server — `acc_server.py`
Python stdlib HTTP server on port 8765. Zero dependencies (no pip). Provides a REST-like API for the frontend to persist state: config, table data files, lossless autosave snapshots, and optional mirror writes. Intentionally minimal so the folder is fully self-contained.

### 3. Persisted Table Data — `ACCMembersInfo.json`, `CompaniesInfo.json`
Live on-disk snapshots written by `stateToJSON()`. These are the authoritative source of truth loaded at app startup. Format is lossless (includes columns, rows, sort hierarchy, group levels, field links) — not the export/grouped format.

### 4. Infrastructure — `Iniciar_Servidor.bat`
The single entry point to run the whole system. Sets `PYTHONUTF8=1` and `PYTHONIOENCODING=utf-8` before starting the server — mandatory on Windows to avoid crashes on Unicode characters in the server's banner.

### 5. Documentation — `CLAUDE.md`, `SessaoCowork.md`
- `CLAUDE.md`: authoritative developer reference (architecture, invariants, function map, operating rules).
- `SessaoCowork.md`: historical design log explaining the *why* behind key decisions (Format A/B, two sort modes, T1/T2). Read for rationale, not current state.

---

## Key Concepts

### Multi-Table Model
Each "project" (table) has its own data file + autosave. The global registry is `_editor_config.json`: `tables[]` list + `activeTable` + `workDir`.

### The Critical Persistence Split
There are **two parallel persistence paths**:

| Path | When | Format | Purpose |
|---|---|---|---|
| **Autosave** (`persistLS`, debounce 2s) | Continuously | **Lossless** `stateToJSON()` snapshot | Restore on reload |
| **Mirror** (on "Gravar" click) | Manual save | **Formatted** (A or B, user's choice) | Consumer output |

Export formats are **lossy** — grouping removes the group-by column; field links collapse columns into objects. If autosave used the export format, reopening the app would silently destroy data. This is why autosave is always lossless.

### Two Sort Modes
- **MODE OFF** (`sortOptsEnabled=false`): `getSortedRows()` returns `rows` as-is; clicking sort physically reorders the array.
- **MODE ON** (`sortOptsEnabled=true`): `getSortedRows()` computes a sorted view *without* mutating `rows`; switching off restores insertion order.

`colSort` is **never mutated outside `applySortPopup`** — breaking this invariant breaks drag-to-reorder.

### Two Output Formats
- **Format A** (`getTableFormatData`): groups by the active sort hierarchy → hierarchical reporting.
- **Format B** (`getExportFormatData`): groups by `groupLevels` (tab Opções) → original export format.

Both apply field-link nesting. Only the mirror and Export/Copy buttons use these formats. Autosave always bypasses them.

### T1 — Grouping Dedup
When grouping by a level, `buildGrouped`/`buildGroupedRaw` delete the group-by column from child objects (it lives as the group key, not inside children). Changing one requires changing the other.

### T2 — Field Links
`fieldLinks` nest `parent → children`: `{"Company":"X","ID":"1"}` becomes `{"Company":{"value":"X","ID":"1"}}`. Constraints: no cycles, depth=1 only, children can't be group-by fields, no duplicate parents.

### `applyState` — 4 Input Shapes
1. Full lossless state (`columns` + `rows`)
2. Legacy `col_xx`/`key` format (auto-migrated)
3. Grouped export object (`flattenGrouped` + `detectGroupField`)
4. Flat array

---

## Guided Tour (10 steps)

| # | Title | What to look at |
|---|---|---|
| 1 | Developer Reference | Read `CLAUDE.md` first — the mental model for everything |
| 2 | Launching the App | `Iniciar_Servidor.bat` — why UTF-8 env vars are mandatory |
| 3 | The Autosave Server | `acc_server.py` — zero-dependency stdlib HTTP, `safe_name` path traversal guard |
| 4 | The Editor | `MembrosInfo_Editor.html` — the entire app in one file |
| 5 | State & Persistence | `persistLS` + `serverSave` — lossless vs lossy split |
| 6 | ACC Members Data | `ACCMembersInfo.json` — what `stateToJSON()` actually writes |
| 7 | Companies Data | `CompaniesInfo.json` — field links in practice, mirror target |
| 8 | Sort Engine | Two modes — MODE OFF (physical reorder) vs MODE ON (computed view) |
| 9 | Output Formats | Format A vs B — only affect mirror/export, never restore |
| 10 | Design Rationale | `SessaoCowork.md` — *why* there are two modes, two formats, T1/T2 |

---

## File Map

| File | Layer | Complexity | What it does |
|---|---|---|---|
| `MembrosInfo_Editor.html` | Frontend | complex | Entire app: grid UI, all JS logic, sort/group/field-link engine, undo stack, server communication |
| `acc_server.py` | Server | complex | Stdlib HTTP server, REST-like API, autosave/mirror/config persistence |
| `CLAUDE.md` | Docs | moderate | Authoritative developer reference + AI operating rules |
| `CompaniesInfo.json` | Data | moderate | Companies table lossless snapshot (field links in practice) |
| `ACCMembersInfo.json` | Data | simple | ACC Members table lossless snapshot |
| `Iniciar_Servidor.bat` | Infra | simple | UTF-8 launcher for the server |
| `SessaoCowork.md` | Docs | complex | Design rationale (historical, not current spec) |

---

## Complexity Hotspots

### `MembrosInfo_Editor.html` — the whole frontend (complex)
~2300 lines, all state in globals, no module system. Key risk areas:
- **Drag/copy/paste** index against `getSortedRows()` and map back via `rows.indexOf(row)` — any sort change must preserve this mapping.
- **`colSort` mutation** — must only happen inside `applySortPopup`. Touching it elsewhere breaks drag-to-reorder silently.
- **`render()` triggers `persistLS`** — if in-memory state is bad and the browser is open, autosave files get corrupted. Test carefully.

### `acc_server.py` — HTTP request handler (complex)
`do_POST` handles all write endpoints in one method. `safe_name` is the only path traversal guard — don't bypass it. `add_num`/`strip_num` have different logic for flat vs grouped data.

### `SessaoCowork.md` — not a spec, just history (complex)
Dense historical log. Don't act on it as current state — verify against `CLAUDE.md` and the actual code.

---

## Invariants That Must Never Break

| | Invariant |
|---|---|
| (a) | `buildGroupedRaw` must mirror the T1 strip logic of `buildGrouped` — change one, change both |
| (b) | `applyFieldLinksToRow` is called in grouped *and* flat paths — keep in sync |
| (c) | `colSort` is **only mutated inside `applySortPopup`** |
| (d) | Format A and B are never mixed in a single output |
| (e) | `renameCol`/`deleteColumn` must keep `fieldLinks`/`colSort`/`sortHierarchy`/`groupLevels` coherent |

---

## Quick Start

```bash
# 1. Double-click to start the server
Iniciar_Servidor.bat

# 2. Verify it's running
curl http://localhost:8765/ping
# → {"ok": true, ...}

# 3. Open the app in your browser
# File → Open → MembrosInfo_Editor.html
# (or serve the folder: py -m http.server 8080)
```
