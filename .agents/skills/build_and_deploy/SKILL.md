---
name: build_and_deploy
description: DevOps/Build Engineer stage. Starts runtime services, then installs, builds, tests, and runs every component locally in dependency order using docs/Project_Profile.md, and runs the smoke test. Use as step 5 (final) of the startcycle pipeline.
---

# Skill: Build and Deploy

## Objective
As the DevOps/Build Engineer, bring the whole system up locally, whether it is one binary,
a multi-service full-stack app, or workers connected to an orchestration engine, and prove it
works with the smoke test.

## Rules of Engagement
- **Profile-Driven**: Take every command from `docs/Project_Profile.md`. If one is missing or wrong, work out the correct one from the repo's build files and CI configuration, and record it in your report. Do not guess.
- **Immutability**: Do not modify source code to make the build pass. If a failure is caused by a code defect, send the failure output back to the **Software Engineer** (`.agents/skills/generate_code/SKILL.md`) and resume the pipeline from there. You may fix purely local environment issues (missing local tool, port conflict) and report what you changed.
- **Local Only**: Run locally. Do not deploy to shared, cloud, or production environments unless the user explicitly asks.
- **Clean Up Honestly**: Tell the user which processes and services are left running and how to stop them.

## Instructions
1. **Read the Profile**: Note components, runtime services, startup order, and the smoke test.
2. **Start Runtime Services**: Start each required service with the Profile's command and wait for its readiness check to pass before continuing.
3. **Install & Build**: For each component, in dependency order, run its install and build commands.
4. **Test**: Run each component's unit tests, then integration/contract tests now that services are up.
5. **Run**: Start components following the Startup Order (e.g. back ends and background workers before front ends and clients). Wait until each one is healthy.
6. **Smoke Test**: Run the Profile's smoke test end to end and capture the result. For libraries or CLIs with nothing long-running, a passing test suite plus a sample invocation is enough.
7. **Final Report**: Tell the user what was built, how to run and stop it, URLs/ports/endpoints, test and smoke-test results, and any open issues.
