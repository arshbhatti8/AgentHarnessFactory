# Agent Factory — Operating Instructions

This repository is a **model-agnostic, tool-agnostic, and stack-agnostic** autonomous
development pipeline. It works with any LLM coding agent that can read files, write files, and
run shell commands (Claude Code, OpenAI Codex, Gemini CLI, Antigravity, Cursor, Aider, etc.),
and on any project, in any language or framework: a single script, a full-stack web app,
a workflow-orchestration service, a mobile app, a library, or a polyglot monorepo.

Everything is plain Markdown. There are no vendor-specific APIs, tool names, or
agent handles. Where these instructions say "read", "write", or "run", use whatever
equivalent tool your runtime provides.

## Directory layout

| Path | Purpose |
|------|---------|
| `AGENTS.md` | This file. The canonical instructions for every agent. |
| `.agents/workflows/startcycle.md` | The pipeline orchestration (the single source of truth). |
| `.agents/skills/<skill>/SKILL.md` | One file per pipeline stage, in the open Agent Skills format. |
| `.agents/templates/` | Templates for the two documents below. |
| `docs/Project_Profile.md` | Created by the pipeline; kept across cycles. **How** this repo is built, run, and tested: components, commands, runtime services, framework invariants, conventions. |
| `docs/Technical_Specification.md` | Created by the pipeline each cycle. **What** to build: the contract every later stage follows. |
| `CLAUDE.md`, `.claude/`, `.gemini/` | Thin, tool-specific shims that point back to the files above. Never put logic in them. |

## Triggering the pipeline

Start the pipeline when the user sends any of:

- `/startcycle <idea>`
- `startcycle <idea>`
- `start cycle: <idea>`

Then read `.agents/workflows/startcycle.md` and follow it exactly, using `<idea>` as input.

## Roles

A single agent plays every role in sequence. A "handoff" means: finish the current
stage, announce the switch (e.g. `--- Handoff: QA Engineer ---`), then read and execute
the next skill file. If your runtime supports sub-agents, you may run a stage in a
sub-agent, but this is optional. The pipeline must work without them.

| Role | Skill file | Next role |
|------|-----------|-----------|
| Product Manager | `.agents/skills/write_specs/SKILL.md` | Software Engineer (after user approval) |
| Software Engineer | `.agents/skills/generate_code/SKILL.md` | QA Engineer |
| QA Engineer | `.agents/skills/audit_code/SKILL.md` | Software Engineer (if bugs) / Version Control Specialist (if clean) |
| Version Control Specialist | `.agents/skills/version_control/SKILL.md` | DevOps/Build Engineer |
| DevOps/Build Engineer | `.agents/skills/build_and_deploy/SKILL.md` | Done: report to user |

## Global rules

1. **Spec is law.** After approval, `docs/Technical_Specification.md` is the contract. Stages
   do not change the design; only the Product Manager edits the spec. The Product Manager owns
   `docs/Project_Profile.md`; the Software Engineer may update only its commands and runtime
   services, and only with commands they have actually run successfully.
2. **One gate only.** The pipeline pauses for the user exactly once, at spec approval. After
   that it runs to completion without asking permission, unless it hits a blocker it cannot
   resolve (see rule 5).
3. **Stay in the workspace.** Do not modify files outside the repository. Do not push to
   remotes, publish packages, or deploy to shared or production environments unless the user
   explicitly asks.
4. **Be honest.** Report real command output. Never claim a build, test, or audit passed
   unless you ran it and it passed.
5. **Escalate instead of looping forever.** If the QA ↔ Engineer loop has not converged after
   5 rounds, or a stage is blocked (missing credentials, unavailable toolchain, ambiguous
   spec), stop and report the blocker to the user with what you tried.
6. **Never assume a stack.** No language, framework, package manager, build tool, test runner,
   or architecture is the default. Every stack-specific command and rule comes from
   `docs/Project_Profile.md`, which is derived from evidence in the repository (or, for
   greenfield work, from the approved spec).
7. **Respect the existing codebase.** In an existing repository, follow its stack, structure,
   tooling, and conventions. Write idiomatic code for each component's own language and
   framework.
8. **Think in components.** A project may contain many independently built units with different
   toolchains. Scope work, commands, tests, and commits per component, and treat the interfaces
   between components as explicit contracts.
9. **Honor framework invariants.** Frameworks impose rules that compilers often do not catch
   (e.g. determinism in durable-workflow code, client/server boundaries in full-stack
   frameworks). Record them in the Profile, implement against them, and audit for them.
