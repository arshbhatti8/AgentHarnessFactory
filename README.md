# Generic Agents Workspace

A model-agnostic agent factory: an autonomous development pipeline
(**PM → Engineer → QA → Version Control → DevOps**) written entirely in plain Markdown.
It works with any LLM coding agent that can read and write files and run shell
commands: Claude, OpenAI (GPT/Codex), Gemini, or anything else.

## How it works

```
/startcycle <idea>
      │
      ▼
Product Manager ──► docs/Technical_Specification.md ──► you reply "Approved"
      │
      ▼
Software Engineer ◄──► QA Engineer      (loops until 0 bugs, max 5 rounds)
      │
      ▼
Version Control Specialist              (local Conventional Commits)
      │
      ▼
DevOps/Build Engineer                   (install, build, test, run locally)
```

All logic lives in vendor-neutral files:

| File | What it is |
|------|------------|
| `AGENTS.md` | Canonical instructions, roles, and global rules. |
| `.agents/workflows/startcycle.md` | The pipeline orchestration. |
| `.agents/skills/<skill>/SKILL.md` | One stage per skill ([Agent Skills](https://agentskills.io) format). |

Tool-specific files are **thin shims** that point back to those files:

| Tool | Instructions file | `/startcycle` command |
|------|-------------------|-----------------------|
| Claude Code | `CLAUDE.md` (imports `AGENTS.md`) | `.claude/commands/startcycle.md` |
| Gemini CLI | `.gemini/settings.json` loads `AGENTS.md` | `.gemini/commands/startcycle.toml` |
| OpenAI Codex | `AGENTS.md` (read natively) | Type `startcycle <idea>`; `AGENTS.md` defines the trigger |
| Antigravity | `AGENTS.md` | `.agents/workflows/startcycle.md` (native) |
| Cursor / Aider / others | Point the tool at `AGENTS.md` | Type `startcycle <idea>` |

## Usage

Open this repo in your agent of choice and run:

```
/startcycle A CLI todo app with SQLite storage and due-date reminders
```

If your tool has no slash commands, type `startcycle <idea>` or `start cycle: <idea>`.

### Raw API / custom harness

If you're using a model directly through its API, give it `AGENTS.md` plus
`.agents/workflows/startcycle.md` as the system prompt. It also needs file read/write and
shell tools, and it should read each `SKILL.md` when the workflow calls for it.

## Customizing

- **Add a stage:** create `.agents/skills/<name>/SKILL.md` (with `name`/`description`
  frontmatter), add it to the roles table in `AGENTS.md`, and insert it into
  `.agents/workflows/startcycle.md`.
- **Change behavior:** edit only the canonical files. Never add logic to the shims, so every
  tool stays in sync.
- **Tool-specific tweaks:** put them in `GEMINI.md` (auto-loaded by `.gemini/settings.json`)
  or below the import in `CLAUDE.md`, and keep them minimal.
