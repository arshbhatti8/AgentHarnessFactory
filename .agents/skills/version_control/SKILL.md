---
name: version_control
description: Version Control Specialist stage. Commits the audited changes locally using Conventional Commits scoped per component. Use as step 4 of the startcycle pipeline.
---

# Skill: Version Control

## Objective
As the Version Control Specialist, commit the finalized code with Conventional Commits
before the build phase.

## Rules of Engagement
- **Conventional Commits**: Every commit message follows the Conventional Commits spec. Use the scopes listed under Commit Scopes in `docs/Project_Profile.md`, typically the component name (e.g. `feat(<component>): …`, `fix(<component>): …`, `docs: …`).
- **Target Context**: Track and commit changes across the whole workspace.
- **Local Only**: Commit locally. Do not push, force-push, or rewrite existing history unless the user explicitly asks.
- **Hygiene**: Never commit secrets, local environment files, build output, caches, or dependency directories. Make sure each component's stack has appropriate ignore rules, and add any that are missing. Do commit lockfiles.
- **Continuous Execution**: Do not pause or ask for permission.

## Instructions
1. **Review Changes**: Inspect the working tree and diffs to see everything the Software Engineer and QA stages produced.
2. **Group Logically**: Plan commits so that each is one coherent change: shared contracts or schemas, then each component's implementation, then tests, then docs (spec and Profile). A change that must land atomically across components (for example, both sides of a contract) may be one commit.
3. **Commit**: Stage and commit each group with a clear Conventional Commit message. Include any commit trailers your runtime or the user requires.
4. **Handoff**: Hand off to the **DevOps/Build Engineer** (`.agents/skills/build_and_deploy/SKILL.md`).
