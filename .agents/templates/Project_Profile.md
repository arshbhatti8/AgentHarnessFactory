# Project Profile

> Maintained by the pipeline at `docs/Project_Profile.md`. Describes **how this repository is
> built, run, and tested**. It stays valid across cycles; the Technical Specification describes
> **what** is being built in the current cycle.
>
> Fill every field from evidence in the repository (manifests, lockfiles, CI config, READMEs,
> scripts, existing code), or from the approved spec for greenfield work. Write `n/a` when a
> field does not apply and `unknown` when it cannot be determined. Never invent a command.

## Repository Shape
- **Status:** greenfield | existing
- **Layout:** single component | multi-component (monorepo) | other: …
- **Workspace / orchestration tooling:** tools that operate across components, or `n/a`
- **CI configuration:** path(s), or `n/a`

## Components
<!-- Repeat this block for every independently built or deployed unit. -->

### `<component-name>`
- **Path:**
- **Role:** what this component does in the system
- **Language(s) & version:**
- **Framework(s) / key libraries:**
- **Dependency manager:**
- **Depends on:** other components and runtime services this one needs
- **Commands** (run from **Path** unless stated otherwise):

  | Action | Command |
  |--------|---------|
  | install | |
  | build | |
  | lint / format check | |
  | typecheck / static analysis | |
  | test (unit) | |
  | test (integration) | |
  | run (local) | |

## Runtime Services
<!-- Everything that must be running for integration tests or a local run: databases, queues,
     caches, workflow/orchestration engines, emulators, other components' processes. -->

| Service | Needed by | Start locally | Readiness check | Stop |
|---------|-----------|---------------|-----------------|------|

## Startup Order
Order in which runtime services and components must start for a full local run.

## Framework Invariants
<!-- Rules imposed by the languages, frameworks, or platforms in use. Code must never violate
     them, and the QA Engineer enforces them. Each rule must be concrete and checkable. -->

| # | Applies to | Rule | How to check |
|---|------------|------|--------------|

## Conventions
Existing code style, directory structure, naming, test locations, error handling, logging,
configuration and secret handling. Follow these over personal preference.

## Commit Scopes
Conventional Commit scopes to use (usually one per component, e.g. the component name).

## Smoke Test
An end-to-end check that proves the running system works: steps and expected result.
