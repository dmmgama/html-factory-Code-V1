"""
TableEditor Server v2 — acc_server.py
Porta 8765

GET  /ping                → { ok, dir, workDir }
GET  /config              → { ok, config }
POST /config              → grava campos no _editor_config.json
POST /save                → { filename, data, mirrorWithNum? } → grava na workDir + mirror
POST /autosave            → { data, tableId? } → grava _autosave_{tableId}.json
GET  /load?filename=X     → lê da workDir
GET  /autosave-load?tableId=X → lê _autosave_{tableId}.json
GET  /list                → lista .json da workDir (exclui _*)
POST /set-workdir         → { path }
POST /set-mirror          → { path, withNum? }
GET  /tables              → lista de tabelas do config
POST /tables/save         → { tables, activeTable }
POST /tables/new          → { name, file } → cria ficheiro JSON vazio
DELETE /tables/file       → { file } → apaga ficheiro .json da workDir
"""

import http.server
import json
import os
from pathlib import Path
from urllib.parse import urlparse, parse_qs, unquote

BASE_DIR      = Path(__file__).resolve().parent
PORT          = 8765

# A3-ii: estado local/descartável vive em .tableeditor/ (gitignored). Ficheiros de
# DADOS versionáveis ficam na workDir. Layout:
#   .tableeditor/index.json         -> global: workDir, activeTable, tables[{id,name,file}], misc
#   .tableeditor/<id>.config.json   -> config de máquina por projecto (classe B)
#   .tableeditor/<id>.autosave.json -> autosave de dados por projecto (envelope, classe A)
# load_config()/save_config() apresentam um dict UNIFICADO (compat com os endpoints e o
# cliente) mas leem/escrevem o layout repartido. CONFIG_FILE legado é migrado 1x.
TE_DIR         = BASE_DIR / ".tableeditor"
INDEX_FILE     = TE_DIR / "index.json"
LEGACY_CONFIG  = BASE_DIR / "_editor_config.json"
TABLE_CFG_KEYS = ("mirror", "mirrorWithNum", "saveFormatMirror", "channels")  # classe B por projecto
_DEF_CH = {"parts": {"schema": True, "types": False, "view": False}, "destino": "", "cols": {}}
DEFAULT_TABLE_CFG = {
    "mirror": "", "mirrorWithNum": False, "saveFormatMirror": "table",
    # channels: composição à la carte por canal de saída (export/mirror) — classe B
    "channels": {"export": dict(_DEF_CH), "mirror": dict(_DEF_CH)},
}

DEFAULT_CONFIG = {
    "workDir":       str(BASE_DIR),
    "mirrorPath":    "",
    "mirrorWithNum": False,
    "panelWidth":    360,
    "lastFile":      "CompaniesInfo",
    "activeTable":   "companies-info",
    # A3-i: cada entrada de tabela guarda só IDENTIDADE + config de máquina (classe B:
    # mirror/mirrorWithNum/saveFormatMirror). A organização (colSort/sort/groupLevels/
    # fieldLinks = classe A) vive SÓ no autosave de dados (envelope), não aqui.
    "tables": [
        {
            "id": "companies-info",
            "name": "Companies Info",
            "file": "CompaniesInfo",
            "mirror": "",
            "mirrorWithNum": False,
            "saveFormatMirror": "table"
        },
        {
            "id": "acc-members-info",
            "name": "ACC Members Info",
            "file": "ACCMembersInfo",
            "mirror": "",
            "mirrorWithNum": False,
            "saveFormatMirror": "table"
        }
    ]
}

EMPTY_TABLE = {
    "columns": [
        {"label": "Col1", "hidden": False, "fixed": False},
        {"label": "Col2", "hidden": False, "fixed": False},
        {"label": "Col3", "hidden": False, "fixed": False},
        {"label": "Col4", "hidden": False, "fixed": False},
    ],
    "rows": [],
    "groupLevels": [],
    "colSort": {},
    "sortOptsEnabled": False,
    "sortHierarchy": [],
}

def _safe_id(tid) -> str:
    return Path(os.path.basename(str(tid))).name or "default"

def _table_cfg_path(tid) -> Path:
    return TE_DIR / f"{_safe_id(tid)}.config.json"

def autosave_path(tid) -> Path:
    return TE_DIR / f"{_safe_id(tid)}.autosave.json"

def _read_json(p: Path, default):
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default

def _write_index_and_configs(cfg: dict):
    """Reparte o dict unificado: index.json (global+identidade) + <id>.config.json (classe B)."""
    TE_DIR.mkdir(parents=True, exist_ok=True)
    index = {
        "workDir":       cfg.get("workDir", str(BASE_DIR)),
        "activeTable":   cfg.get("activeTable", ""),
        "mirrorPath":    cfg.get("mirrorPath", ""),
        "mirrorWithNum": cfg.get("mirrorWithNum", False),
        "panelWidth":    cfg.get("panelWidth", 360),
        "lastFile":      cfg.get("lastFile", ""),
        "tables":        [{"id": t["id"], "name": t.get("name", ""), "file": t.get("file", "")}
                          for t in cfg.get("tables", [])],
    }
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    keep_ids = set()
    for t in cfg.get("tables", []):
        keep_ids.add(_safe_id(t["id"]))
        tc = {k: t.get(k, DEFAULT_TABLE_CFG[k]) for k in TABLE_CFG_KEYS}
        with open(_table_cfg_path(t["id"]), "w", encoding="utf-8") as f:
            json.dump(tc, f, indent=2, ensure_ascii=False)
    # limpar config files de tabelas removidas
    for p in TE_DIR.glob("*.config.json"):
        if p.name[:-len(".config.json")] not in keep_ids:
            try: p.unlink()
            except Exception: pass

def _migrate_if_needed():
    if INDEX_FILE.exists():
        return
    TE_DIR.mkdir(parents=True, exist_ok=True)
    base = _read_json(LEGACY_CONFIG, None) if LEGACY_CONFIG.exists() else None
    if base is None:
        base = dict(DEFAULT_CONFIG)
    _write_index_and_configs(base)
    # mover autosaves antigos workDir/_autosave_<id>.json -> .tableeditor/<id>.autosave.json
    wd = Path(base.get("workDir", str(BASE_DIR)))
    for t in base.get("tables", []):
        old = wd / f"_autosave_{t['id']}.json"
        new = autosave_path(t["id"])
        if old.exists() and not new.exists():
            try:
                new.write_text(old.read_text(encoding="utf-8"), encoding="utf-8")
                old.unlink()
            except Exception:
                pass
    # preservar config legado fora do caminho
    if LEGACY_CONFIG.exists():
        try: LEGACY_CONFIG.rename(BASE_DIR / "_editor_config.json.bak")
        except Exception: pass

def load_config() -> dict:
    _migrate_if_needed()
    index = _read_json(INDEX_FILE, None)
    if index is None:
        return dict(DEFAULT_CONFIG)
    tables = []
    for t in index.get("tables", []):
        tc = _read_json(_table_cfg_path(t["id"]), dict(DEFAULT_TABLE_CFG))
        merged = {"id": t["id"], "name": t.get("name", ""), "file": t.get("file", "")}
        for k in TABLE_CFG_KEYS:
            merged[k] = tc.get(k, DEFAULT_TABLE_CFG[k])
        tables.append(merged)
    return {
        "workDir":       index.get("workDir", str(BASE_DIR)),
        "activeTable":   index.get("activeTable", ""),
        "mirrorPath":    index.get("mirrorPath", ""),
        "mirrorWithNum": index.get("mirrorWithNum", False),
        "panelWidth":    index.get("panelWidth", 360),
        "lastFile":      index.get("lastFile", ""),
        "tables":        tables,
    }

def save_config(cfg: dict):
    _write_index_and_configs(cfg)

def get_work_dir() -> Path:
    p = Path(load_config().get("workDir", str(BASE_DIR)))
    p.mkdir(parents=True, exist_ok=True)
    return p

def safe_name(raw: str) -> str:
    return Path(os.path.basename(raw)).name

def write_json(fpath: Path, data):
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def strip_num(data):
    """Remove campo '#' de rows em qualquer formato (flat ou grouped)."""
    if isinstance(data, list):
        result = []
        for item in data:
            if isinstance(item, dict):
                result.append({k: v for k, v in item.items() if k != '#'})
            else:
                result.append(strip_num(item))
        return result
    if isinstance(data, dict):
        return {k: strip_num(v) for k, v in data.items()}
    return data

def add_num(data):
    """Adiciona '#' sequencial a rows numa estrutura flat ou grouped."""
    counter = [0]
    def walk(node):
        if isinstance(node, list):
            result = []
            for item in node:
                if isinstance(item, dict):
                    counter[0] += 1
                    result.append({'#': counter[0], **item})
                else:
                    result.append(walk(item))
            return result
        if isinstance(node, dict):
            return {k: walk(v) for k, v in node.items()}
        return node
    return walk(data)


class Handler(http.server.BaseHTTPRequestHandler):

    def log_message(self, fmt, *args):
        print(f"  [{self.address_string()}] {fmt % args}")

    def cors(self, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_OPTIONS(self):
        self.cors(204)

    def ok(self, d):
        self.cors()
        self.wfile.write(json.dumps(d, ensure_ascii=False).encode())

    def err(self, msg, status=400):
        self.cors(status)
        self.wfile.write(json.dumps({"ok": False, "error": msg}).encode())

    def body(self):
        n = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(n)
        return json.loads(raw.decode("utf-8")) if raw else {}

    # ── GET ──────────────────────────────────────────────────────────────
    def do_GET(self):
        parsed = urlparse(self.path)
        route  = parsed.path
        qs     = parse_qs(parsed.query)

        if route == "/ping":
            cfg = load_config()
            self.ok({"ok": True, "dir": str(BASE_DIR), "workDir": cfg["workDir"]})

        elif route == "/config":
            self.ok({"ok": True, "config": load_config()})

        elif route == "/tables":
            cfg = load_config()
            self.ok({"ok": True, "tables": cfg.get("tables", []), "activeTable": cfg.get("activeTable", "")})

        elif route == "/load":
            fn = safe_name(unquote(qs.get("filename", [""])[0]))
            if not fn.endswith(".json"): fn += ".json"
            fpath = get_work_dir() / fn
            if not fpath.exists():
                self.err(f"Não encontrado: {fn}", 404); return
            try:
                with open(fpath, encoding="utf-8") as f:
                    data = json.load(f)
                self.ok({"ok": True, "data": data, "path": str(fpath)})
            except Exception as e:
                self.err(str(e))

        elif route == "/autosave-load":
            tid = qs.get("tableId", ["default"])[0]
            fpath = autosave_path(tid)
            if not fpath.exists():
                self.ok({"ok": False, "reason": "no autosave"}); return
            try:
                with open(fpath, encoding="utf-8") as f:
                    data = json.load(f)
                self.ok({"ok": True, "data": data})
            except Exception as e:
                self.err(str(e))

        elif route == "/list":
            wd = get_work_dir()
            files = sorted(p.stem for p in wd.glob("*.json") if not p.name.startswith("_"))
            self.ok({"ok": True, "files": files, "workDir": str(wd)})

        else:
            self.err("Not found", 404)

    # ── POST ─────────────────────────────────────────────────────────────
    def do_POST(self):
        route = urlparse(self.path).path

        if route == "/save":
            try:
                b  = self.body()
                fn = safe_name(b.get("filename", "_autosave_default"))
                if not fn.endswith(".json"): fn += ".json"
                data         = b.get("data", {})
                mirror_num   = b.get("mirrorWithNum", False)
                # mirrorData: pre-formatted data for mirror (from client format selector).
                # If present, use it for mirror instead of computing from data.
                mirror_data_override = b.get("mirrorData", None)
                # mirrorIsEnvelope: o mirror é o envelope canónico Frictionless → NUNCA
                # numerar (# violaria SPEC §2: data só tem nomes de campos). Gate explícito
                # por flag, nunca por sniffing de shape.
                mirror_is_envelope = b.get("mirrorIsEnvelope", False)
                wd           = get_work_dir()
                fpath        = wd / fn
                write_json(fpath, data)

                # Mirror
                cfg = load_config()
                # Per-table mirror overrides global
                active_tid = cfg.get("activeTable", "")
                table = next((t for t in cfg.get("tables", []) if t["id"] == active_tid), None)
                mirror_path  = (table.get("mirror", "") if table else "") or cfg.get("mirrorPath", "")
                mirror_num   = (table.get("mirrorWithNum", False) if table else False) or mirror_num
                mirror_result = None
                if mirror_path.strip():
                    try:
                        mp = Path(mirror_path.strip())
                        mp.parent.mkdir(parents=True, exist_ok=True)
                        if mirror_data_override is not None:
                            if mirror_is_envelope:
                                # Envelope canónico: gravar tal-qual, sem tocar em # (SPEC §2)
                                mirror_data = mirror_data_override
                            else:
                                # Client already formatted; just add/strip # based on mirrorWithNum
                                mirror_data = add_num(mirror_data_override) if mirror_num else strip_num(mirror_data_override)
                        else:
                            mirror_data = add_num(data) if mirror_num else strip_num(data)
                        write_json(mp, mirror_data)
                        mirror_result = str(mp)
                    except Exception as me:
                        mirror_result = f"ERRO: {me}"

                if not fn.startswith("_"):
                    cfg["lastFile"] = fn.replace(".json", "")
                    save_config(cfg)

                res = {"ok": True, "path": str(fpath)}
                if mirror_result: res["mirror"] = mirror_result
                self.ok(res)
            except Exception as e:
                self.err(str(e))

        elif route == "/autosave":
            try:
                b   = self.body()
                tid = b.get("tableId", "default")
                TE_DIR.mkdir(parents=True, exist_ok=True)
                fpath = autosave_path(tid)
                write_json(fpath, b.get("data", {}))
                self.ok({"ok": True, "path": str(fpath)})
            except Exception as e:
                self.err(str(e))

        elif route == "/config":
            try:
                b = self.body()
                cfg = load_config()
                cfg.update(b)
                save_config(cfg)
                self.ok({"ok": True, "config": cfg})
            except Exception as e:
                self.err(str(e))

        elif route == "/set-workdir":
            try:
                b = self.body()
                p = b.get("path", "").strip()
                if not p: self.err("path vazio"); return
                Path(p).mkdir(parents=True, exist_ok=True)
                cfg = load_config()
                cfg["workDir"] = p
                save_config(cfg)
                self.ok({"ok": True, "workDir": p})
            except Exception as e:
                self.err(str(e))

        elif route == "/set-mirror":
            try:
                b        = self.body()
                mirror   = b.get("path", "").strip()
                with_num = b.get("withNum", False)
                tid      = b.get("tableId", "")
                cfg = load_config()
                if tid:
                    for t in cfg.get("tables", []):
                        if t["id"] == tid:
                            t["mirror"]        = mirror
                            t["mirrorWithNum"] = with_num
                else:
                    cfg["mirrorPath"]    = mirror
                    cfg["mirrorWithNum"] = with_num
                save_config(cfg)
                self.ok({"ok": True, "mirrorPath": mirror, "mirrorWithNum": with_num})
            except Exception as e:
                self.err(str(e))

        elif route == "/tables/save":
            try:
                b = self.body()
                cfg = load_config()
                cfg["tables"]      = b.get("tables", cfg.get("tables", []))
                cfg["activeTable"] = b.get("activeTable", cfg.get("activeTable", ""))
                save_config(cfg)
                self.ok({"ok": True})
            except Exception as e:
                self.err(str(e))

        elif route == "/tables/new":
            try:
                b    = self.body()
                name = b.get("name", "Nova Tabela").strip()
                fn   = safe_name(b.get("file", name.replace(" ", "") + ".json"))
                if not fn.endswith(".json"): fn += ".json"
                fpath = get_work_dir() / fn
                if not fpath.exists():
                    import datetime, copy
                    empty = copy.deepcopy(EMPTY_TABLE)
                    empty["savedAt"] = datetime.datetime.utcnow().isoformat() + "Z"
                    write_json(fpath, empty)
                self.ok({"ok": True, "file": fn, "path": str(fpath), "created": not fpath.exists()})
            except Exception as e:
                self.err(str(e))

        else:
            self.err("Not found", 404)

    # ── DELETE ───────────────────────────────────────────────────────────
    def do_DELETE(self):
        route = urlparse(self.path).path

        if route == "/tables/file":
            try:
                b  = self.body()
                fn = safe_name(b.get("file", ""))
                if not fn.endswith(".json"): fn += ".json"
                fpath = get_work_dir() / fn
                if fpath.exists():
                    fpath.unlink()
                    self.ok({"ok": True, "deleted": str(fpath)})
                else:
                    self.err(f"Ficheiro não encontrado: {fn}", 404)
            except Exception as e:
                self.err(str(e))
        else:
            self.err("Not found", 404)


if __name__ == "__main__":
    # load_config() migra o config legado e cria .tableeditor/ se preciso
    first = not INDEX_FILE.exists()
    cfg = load_config()
    if first:
        print(f"  Storage criado/migrado: {TE_DIR}")
    wd  = Path(cfg["workDir"])
    wd.mkdir(parents=True, exist_ok=True)

    print(f"\n  TableEditor Server v2")
    print(f"  {'─'*45}")
    print(f"  Porta    : {PORT}")
    print(f"  App dir  : {BASE_DIR}")
    print(f"  Work dir : {wd}")
    active = cfg.get("activeTable", "—")
    tables = cfg.get("tables", [])
    print(f"  Tabelas  : {len(tables)} ({', '.join(t['name'] for t in tables)})")
    print(f"  Activa   : {active}")
    print(f"  Config   : {INDEX_FILE}")
    print(f"  {'─'*45}\n")

    # Multi-thread: um /save lento (ex.: mirror no Google Drive) NÃO pode bloquear
    # o /ping (timeout 1,5s no cliente) — senão a app marcava "servidor fechado".
    server = http.server.ThreadingHTTPServer(("localhost", PORT), Handler)
    print(f"  A correr em http://localhost:{PORT}  (Ctrl+C para parar)\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Servidor parado.")
