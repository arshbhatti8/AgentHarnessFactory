---
name: build_and_deploy
description: DevOps/Build Engineer stage. Installs dependencies, builds, tests, and runs the application locally, then reports results. Use as step 5 (final) of the startcycle pipeline.
---

# Skill: Build and Deploy

## Objective
As the DevOps/Build Engineer, run the right build, test, and run commands for the
project's stack and bring the application up locally (or verify the final build artifact).

## Rules of Engagement
- **Stack Inference**: Take commands from the spec's "Build, Run & Test Commands" section. Fall back to the project's build files (e.g. `Makefile`, `package.json`, `Cargo.toml`, `pyproject.toml`, `requirements.txt`, `Dockerfile`).
- **Immutability**: Do not modify source code to make the build pass. If the build fails because of a code defect, send the failure output back to the **Software Engineer** (`.agents/skills/generate_code/SKILL.md`) and resume the pipeline from there.
- **Local Only**: Run locally. Do not deploy to shared, cloud, or production environments unless the user explicitly asks.
- **Target Context**: Run commands from the directory the project structure requires.

## Instructions
1. **Analyze Project Infrastructure**: Read the spec and check the repository for build configuration files.
2. **Install Dependencies**: Run the stack's dependency install command (e.g. `npm install`, `pip install -r requirements.txt`, `cargo fetch`).
3. **Build / Compile**: Run the build (e.g. `npm run build`, `make`, `cargo build --release`, `docker build`).
4. **Test**: Run the full test suite.
5. **Run**: Start the application locally (e.g. `docker compose up -d`, `npm start`, the compiled binary). For a library or CLI, a passing test suite plus a sample invocation is enough.
6. **Final Report**: Tell the user what was built, how to run it, the URL/port if applicable, test results, and any open issues.
