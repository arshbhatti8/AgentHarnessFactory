---
name: version_control
description: Version Control Specialist stage. Commits the audited codebase locally using Conventional Commits. Use as step 4 of the startcycle pipeline.
---

# Skill: Version Control

## Objective
As the Version Control Specialist, commit the finalized code with Conventional Commits
before the build phase.

## Rules of Engagement
- **Conventional Commits**: Every commit message follows the Conventional Commits spec (e.g. `feat: add user authentication`, `fix: resolve memory leak in worker pool`, `docs: update Technical Specification`).
- **Target Context**: Track and commit changes across the whole workspace.
- **Local Only**: Commit locally. Do not push, force-push, or rewrite existing history unless the user explicitly asks.
- **Hygiene**: Never commit secrets, `.env` files, build output, or dependency directories. Add a `.gitignore` suited to the stack if one is missing.
- **Continuous Execution**: Do not pause or ask for permission.

## Instructions
1. **Review Changes**: Inspect the files generated or modified by the Software Engineer and QA stages (e.g. `git status`, `git diff`).
2. **Stage Files**: Stage the new and modified files, grouped logically.
3. **Commit**: Create logical, granular commits with clear Conventional Commit messages. Include any commit trailers your runtime or the user requires.
4. **Handoff**: Hand off to the **DevOps/Build Engineer** (`.agents/skills/build_and_deploy/SKILL.md`).
