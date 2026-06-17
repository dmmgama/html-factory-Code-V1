# Versao V1

# Estrutura

- 3. Ferramentas
    - AI Models
        - Knowledge
    - AI Tools
        - AI Utility Tools
        - Claude Skills
            - AgenticOS
                - agentic-os
                    - .claude-plugin
                        _ plugin.json
                    - skills
                        - agentic-os-obsidian
                            - references
                                - obsidian
                                    - plugins
                                        - customjs
                                            _ main.js
                                            _ manifest.json
                                            _ styles.css
                                        - dataview
                                            _ main.js
                                            _ manifest.json
                                            _ styles.css
                                        - homepage
                                            _ main.js
                                            _ manifest.json
                                            _ styles.css
                                        - obsidian-shellcommands
                                            _ main.js
                                            _ manifest.json
                                            _ styles.css
                                        - terminal
                                            _ main.js
                                            _ manifest.json
                                            _ styles.css
                                    _ command-center.css
                                    _ styles.css
                                    _ dashboard-template.js
                                    _ frappe-charts.min.js
                                    _ claude-md-template.md
                                    _ home-template.md
                                    _ profile-template.md
                                    _ setup-template.md
                                    _ vault-overview-template.md
                            _ SKILL.md
                        - agentic-os-standalone
                            - references
                                - standalone
                                    _ template.tar.gz
                                    _ personalization.md
                                    _ RAILWAY.md
                            _ SKILL.md
                        - os-mcp
                            - reference
                                - relay-mcp-server
                                    - src
                                        - auth
                                            _ clients.ts
                                            _ codes.ts
                                            _ jsonfile.ts
                                            _ pending.ts
                                            _ pocketbase.ts
                                            _ provider.ts
                                            _ refresh-loop.ts
                                            _ sessions.ts
                                            _ tokens.ts
                                        _ config.ts
                                        _ index.ts
                                        _ relay-client.ts
                                    _ .env.example
                                    _ Dockerfile
                                    _ railway.json
                                    _ tsconfig.json
                                    _ package-lock.json
                                    _ package.json
                                    _ AUTH.md
                            _ SKILL.md
                        - web-artifacts-builder
                            - scripts
                                _ shadcn-components.tar.gz
                                _ bundle-artifact.sh
                                _ init-artifact.sh
                            _ LICENSE.txt
                            _ SKILL.md
                _ agentic-os.zip
            - Cannon-Rules
                - Pesquisa para Construcao
                    _ Cannon-Rules-Skill.zip
                    _ Promp-Para-SkillBuilder-CanonRules.md
                    _ relatorio-canon-redaccao-B-skillbuilder.md
                    _ relatorio-canon-redaccao-B-skillbuilder-ext.md
                _ cannon-rules.skill
            - excalidraw
                _ SKILL.md
            - Grill-me
                _ SKILL.md
            - Grill-me-docs
                _ ADR-FORMAT.md
                _ CONTEXT-FORMAT.md
                _ SKILL.md
            - Handoff
                _ SKILL.md
            - Meta Skills
                - .claude-plugin
                    _ plugin.json
                - skills
                    - agent-browser
                        - references
                            _ authentication.md
                            _ commands.md
                            _ profiling.md
                            _ proxy-support.md
                            _ session-management.md
                            _ snapshot-refs.md
                            _ video-recording.md
                        - templates
                            _ authenticated-session.sh
                            _ capture-workflow.sh
                            _ form-automation.sh
                        _ SKILL.md
                    - audio-transcriber
                        - examples
                            _ basic-transcription.sh
                        - references
                            _ tools-comparison.md
                        - scripts
                            _ install-requirements.sh
                            _ transcribe.py
                        _ CHANGELOG.md
                        _ README.md
                        _ SKILL.md
                    - decision-toolkit
                        - references
                            _ bias-encyclopedia.md
                            _ framework-deep-dives.md
                        - templates
                            _ decision-export-template.md
                            _ decision-framework.md
                            _ decision-guide-template.html
                            _ decision-voice-summary.md
                        _ SKILL.md
                    - deep-research
                        - assets
                            _ deep_research.py
                        - references
                            _ workflow.md
                        - scripts
                            _ run_deep_research.py
                        _ CHANGELOG.md
                        _ SKILL.md
                    - fact-checker
                        _ SKILL.md
                    - file-organizer
                        _ SKILL.md
                    - find-skills
                        _ SKILL.md
                    - frontend-slides
                        _ SKILL.md
                        _ STYLE_PRESETS.md
                    - humanizer
                        _ README.md
                        _ SKILL.md
                    - mcp-builder
                        - reference
                            _ evaluation.md
                            _ mcp_best_practices.md
                            _ node_mcp_server.md
                            _ python_mcp_server.md
                        - scripts
                            _ example_evaluation.xml
                            _ requirements.txt
                            _ connections.py
                            _ evaluation.py
                        _ LICENSE.txt
                        _ SKILL.md
                    - openrouter
                        - references
                            _ index.md
                            _ llms.md
                            _ llms-full.md
                            _ llms-small.md
                            _ other.md
                        _ .skillfish.json
                        _ plugin.json
                        _ SKILL.md
                    - process-interviewer
                        - references
                            _ plan-output-template.md
                            _ skill-output-template.md
                        _ process-interviewer.zip
                        _ SKILL.md
                    - prompt-master
                        - references
                            _ patterns.md
                            _ templates.md
                        _ LICENSE
                        _ README.md
                        _ SKILL.md
                    _ youtubel.txt
                _ Meta Skills.zip
                _ Sumarize skill.md
            - pagedesign-notion
                _ pagedesign-notion.skill
                _ SKILL.md
            - SkillCreation
                - .claude
                    _ settings.local.json
                - SessionSkill
                    - references
                        _ instrucao-captura.md
                        _ stage-a-capture.md
                        _ stage-b-summarize.md
                    - scripts
                        _ parse_clipping.py
                        _ parse_transcript.py
                    _ SKILL.md
                - SessionSkill - Creation
                    - .claude
                        _ settings.local.json
                    _ ARRANQUE.md
                    _ CLAUDE.md
                    _ planoSessionSkill.md
                    _ QuestionarioSessionSkill.md
                    _ SessionSkill Creation - Research Report.md
                _ CLAUDE.md
            - Tradutor-de-Intencoes
                _ SKILL.md
            - Transcript Compressor
                _ SKIL v2L.md
                _ SKILL v3.md
                _ SKILL V4A.md
                _ SKILL.md
                _ 2026-04-27_06-21-58_Claude_Chat_GC_-_ente_S10S11_-_Reformulacao_Estrategica_Projetos.md
        - Context Tools
            - SessionSummary
                - SessionTranscripts
        - Prompts
            _ Prompt - Contract First.md
    - Audit and Mapping Tools
        - Code
            _ Understand-Anything - Turn any code into an interactive knowledge graph.md
        - Multisource
            - IRA MF Tool - Auditoria Multi-Fonte
                - Improvement Files
                    - Versao a melhorar
                        _ manual-ira-mf-v1.md
                        _ runbook-ira-mf-v1.md
                    _ IRA MF Tool - Improvement - INIT-Claude-code.md
                    _ IRA MF Tool - Improvement - Roadmap.md
                    _ IRA MF Tool - Readme David - START HERE.md
                    _ IRA MF Tool - Sessao - Audit a V0 e Improvement da Tool.md
                - V0
                    - Audits
                        _ Mapeamento Agentico - Audit Claude.md
                        _ Mapeamento Agentico - Audit Gemini.md
                        _ Mapeamento Agentico - Audit Perplexity.md
                    - First Case
                    _ IRA MF Tool - Sessao de Dev Inicial Transcript.md
                    _ Mapeamento Agentico Tool - LLM Runbook.md
                    _ Mapeamento Agentico Tool - Readme (Human).md
                - V1
                    _ manual-ira-mf.md
                    _ runbook-ira-mf.md
    - Code
        _ manual-claude-code-obsidian.md
    - Data Tools
        - Json-Studio
            - .claude
                - commands
                    _ flatten.md
                    _ from-table.md
                    _ group-by.md
                    _ inspect.md
                    _ to-format.md
                    _ ver.md
            - .vscode
                _ settings.json
            - _bootstrap
                _ JsonEditor-VS.code-workspace.old
                _ 01-ESTRUTURA.md
                _ CHECKLIST.md
                _ GUIA-commands.md
                _ GUIA-formats.md
                _ GUIA-raiz.md
                _ GUIA-rules.md
                _ GUIA-visual.md
                _ GUIA-workspace.md
            - backups
                _ .gitkeep
            - docs
                _ Frictionless-Table-Schema-TableEditor.md
                _ JSonTools.md
            - formats
                _ _TEMPLATE.md
                _ frictionless-envelope.md
                _ grouped-nested.md
                _ raw-array.md
            - input
                _ .gitkeep
            - output
                _ .gitkeep
            - rules
                _ field-conventions.md
                _ file-handling.md
                _ transform-rules.md
                _ visual-rules.md
            - samples
                _ .gitkeep
            - VSCode-Workspaces
                _ Json-Studio.code-workspace
            _ 00-INSTRUCOES-INICIAIS.md
            _ CLAUDE.md
    - Linha do tempo
        _ linha-do-tempo_conceito-base.md
        _ C1_instrucoes-mockup.md
        _ C1_manual.md
        _ C2_relatorio-uiux-ferramentas.md
        _ GRILL-A-transcricao.md
        _ GRILL-B-linha-do-tempo.md
        _ Projeto-Linha-do-Tempo-Guia.md
    - Memory Protocols
        - Claude and NotebookLM
            _ Claude Code and NotebookLM - Infinite Memory.md
            _ Memory - Claude Code Notebook LM Obsidian.md
            _ Memory - Gemini - Notebooklm - Obsidian.md
            _ Memory - With Grill Me Skill.md
        - Cristalizacao
            - Arqueologia
                _ Cristalizacao - Protocolo PreGrillme.md
            _ 0-ROADMAP_sistema-cristalizacao.md
            _ Aprendizagem.md
            _ cristalizacao-conceito_CANONICO.md
            _ cristalizacao-conceito_PARA-DAVID.md
            _ Ficha-Sessao_S2_grillme-cristalizacao.md
            _ HANDOFF_sistema-cristalizacao.md
            _ INSTRUCAO-pesquisa_FASE2.md
            _ PROTOCOLO-cristalizacao_OPERACIONAL.md
            _ PROTOCOLO-ficha-sessao_INJETAR-NO-ARRANQUE.md
            _ SYSTEM-PROMPT_projeto-cristalizacao.md
    - Obsidian Tools
        - Plugins - Active
            _ Obs Plugin - Templater.md
        - Plugins - Inactive
            _ Obs Plugin - Obsidian-custom-sort.md
        - Templates - Notes
            _ 0. Obsidian Plugin - Template.md
            _ Projects - Readme Template.md
            _ Projects - Template.md
        _ 0. Obsidian Plugins - Lista.md
    - Sessions Resume System
        _ Manual Operativo - Cristalização de Transcripts via NotebookLM.md
