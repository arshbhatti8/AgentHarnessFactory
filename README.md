# Generic Agents Workspace

A model-agnostic agent factory: an autonomous development pipeline
(**PM → Engineer → QA → Version Control → DevOps**) written entirely in plain Markdown.
It works with any LLM coding agent that can read and write files and run shell
commands (Claude, OpenAI (GPT/Codex), Gemini, or anything else), and on any language,
framework, or architecture.

## How it works

```
/startcycle <idea>
      │
      ▼
Product Manager ──► docs/Project_Profile.md        (how this repo builds/runs/tests)
      │         └──► docs/Technical_Specification.md (what to build) ──► you reply "Approved"
      │
      ▼
Software Engineer ◄──► QA Engineer      (loops until 0 bugs, max 5 rounds)
      │
      ▼
Version Control Specialist              (local Conventional Commits)
      │
      ▼
DevOps/Build Engineer                   (start services, build, test, run, smoke test)
```

All logic lives in vendor-neutral files:

| File | What it is |
|------|------------|
| `AGENTS.md` | Canonical instructions, roles, and global rules. |
| `.agents/workflows/startcycle.md` | The pipeline orchestration. |
| `.agents/skills/<skill>/SKILL.md` | One stage per skill ([Agent Skills](https://agentskills.io) format). |
| `.agents/templates/` | Templates for the Project Profile and Technical Specification. |

## Stack-agnostic by design

No skill hard-codes a language, framework, or toolchain. On the first cycle in a repo, the
Product Manager **discovers** the project and writes `docs/Project_Profile.md`:

- **Components**: each independently built unit, with its language, framework, and exact
  install/build/lint/typecheck/test/run commands (taken from the repo's own scripts and CI).
- **Runtime services**: what must be running locally, how to start it, and how to check it's ready.
- **Framework invariants**: rules a framework imposes that compilers don't catch. QA enforces them.
- **Conventions, commit scopes, and a smoke test.**

Every later stage reads commands and rules from the Profile, so the same pipeline works on:

| Project | What the Profile captures (illustrative) |
|---------|------------------------------------------|
| Full-stack web app | `web`, `api`, and `db` components; the database as a runtime service; the API contract between web and API; client/server code-boundary invariants; start the API before the web app. |
| Temporal workflows repo | `workflows`, `activities`, and `worker` components; the Temporal dev server as a runtime service; workflow/activity signatures and task queue names as contracts; workflow determinism invariants (no direct I/O, clock, or randomness in workflow code); a smoke test that starts a workflow and checks its result. |
| Library / CLI | One component; no runtime services; the public API as the contract; the smoke test is a sample invocation. |

For an empty repo, the PM picks the stack in the spec (you approve it), and the Engineer records
the real commands in the Profile as it scaffolds.

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
- **Pin project-specific rules:** edit `docs/Project_Profile.md` directly (e.g. add a framework
  invariant or fix a command); the pipeline treats it as authoritative.
- **Change behavior:** edit only the canonical files. Never add logic to the shims, so every
  tool stays in sync.
- **Tool-specific tweaks:** put them in `GEMINI.md` (auto-loaded by `.gemini/settings.json`)
  or below the import in `CLAUDE.md`, and keep them minimal.
