---
name: write_specs
description: Product Manager stage. Discovers or updates docs/Project_Profile.md, then turns a raw idea into docs/Technical_Specification.md for any language, framework, or multi-component architecture. Use as step 1 of the startcycle pipeline.
---

# Skill: Write Specs

## Objective
As the Product Manager, understand how this repository works (or decide how it will work, if
it is empty), then turn the user's raw idea into a specification that the rest of the pipeline
can implement without further clarification.

## Rules of Engagement
- **No Assumed Stack**: Never assume a language, framework, package manager, or architecture. Derive it from the repository, or choose it deliberately for greenfield work.
- **Existing Code Wins**: In an existing repository, follow its established stack and conventions. Propose a new language, framework, or component only when the idea truly needs it, and justify it in the spec.
- **Artifacts**: Write `docs/Project_Profile.md` from `.agents/templates/Project_Profile.md` and `docs/Technical_Specification.md` from `.agents/templates/Technical_Specification.md`. Create `docs/` if needed.
- **No Guessing Silently**: Record ambiguous decisions under "Assumptions & Open Questions" so the user can correct them at the approval gate.
- **Approval Gate**: This is the only stage that waits for the user. Do not start implementation until the user approves (see `.agents/workflows/startcycle.md`).

## Instructions
1. **Discover the Project**
   - Survey the repository: directory tree, dependency manifests and lockfiles, build and task files, container and infrastructure files, CI configuration, READMEs, and existing tests.
   - Identify every **component** (each independently built, run, or deployed unit), its language, framework, dependency manager, and the exact commands used to install, build, lint, typecheck, test, and run it. Prefer commands already defined in the repo (task runners, scripts, CI steps) over generic ones.
   - Identify **runtime services** needed locally (databases, queues, caches, workflow/orchestration engines, emulators) and how to start them and check they are ready.
   - Identify **framework invariants**: rules the frameworks in use impose on code (for example, deterministic replay requirements in durable-workflow code, server/client code boundaries in full-stack frameworks, migration ordering rules in ORMs). Consult framework documentation you know or that exists in the repo. Write each rule as concrete and checkable.
   - Record **conventions**: structure, naming, test layout, error handling, config/secret handling.
2. **Write or Update the Profile**
   - If `docs/Project_Profile.md` exists, verify it against the repo and update anything stale.
   - For an empty repository, leave fields as `unknown` for now; complete them in step 4 once the stack is chosen.
3. **Draft the Specification** following the template. Pay particular attention to:
   - **Scope & Affected Components**: which components change or are created.
   - **Interfaces & Contracts**: exact definitions for every boundary this work touches, so both sides can be implemented independently and still match.
   - **Framework Invariants for This Change**, and a **Test Plan** mapped to acceptance criteria.
4. **Greenfield Stack Choice** (empty repos or new components only): choose the stack that best fits the requirements, justify it in the spec, and fill in the corresponding Profile fields: components, intended commands, runtime services, invariants.
5. **Request Approval**: Summarize the spec (and any Profile changes) for the user and ask them to reply "Approved" or give feedback. Revise and repeat until approved.
6. **Handoff**: Once approved, hand off to the **Software Engineer** (`.agents/skills/generate_code/SKILL.md`).
