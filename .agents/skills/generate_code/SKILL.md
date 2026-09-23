---
name: generate_code
description: Software Engineer stage. Implements the approved docs/Technical_Specification.md across every affected component, in any language or framework, or fixes a QA/build bug list. Use as step 2 of the startcycle pipeline.
---

# Skill: Generate Code

## Objective
As the Software Engineer, implement the approved specification across every affected
component, following the Project Profile, then continue straight to the QA stage.

## Rules of Engagement
- **Strict Compliance**: Implement exactly the spec. Use each component's language, framework, and conventions as recorded in `docs/Project_Profile.md`.
- **Idiomatic Code**: Write code the way experienced practitioners of that component's language and framework would, matching the surrounding code's style, structure, and patterns.
- **Framework Invariants**: Never violate a rule listed under Framework Invariants in the Profile or spec.
- **Contracts Are Exact**: Implement every interface in the spec's "Interfaces & Contracts" section exactly as written, on both sides. Where the stack allows it, generate or share types and schemas from a single definition instead of duplicating them.
- **Profile Ownership**: You may update only the Components (commands) and Runtime Services sections of the Profile, and only when you scaffold a component or change its tooling. Any command you record must be one you have run successfully.
- **Fix Mode**: If you received a bug list from QA or a failure report from the build stage, fix exactly those issues (no unrelated rewrites), then hand back to QA.
- **Continuous Execution**: Do not pause or ask for permission.

## Instructions
1. **Read Inputs**: Study `docs/Technical_Specification.md`, `docs/Project_Profile.md`, and any bug list you were handed.
2. **Plan the Order**: Implement in dependency order: shared contracts, schemas, and migrations first, then providers (services, back ends, activities or tasks), then consumers (clients, front ends, orchestrators or workflows).
3. **Scaffold (if needed)**: For new components, use the ecosystem's standard project initializer or layout. Then record the component and its commands in the Profile.
4. **Implement & Integrate**: Write the code for every affected component and wire it into its entry points: routes, registrations, dependency injection, worker/process registration, exports, configuration.
5. **Record Dependencies**: Declare every new dependency in the component's own manifest using its dependency manager. Never rely on globally installed packages.
6. **Configuration**: Read environment-specific values (URLs, credentials, ports, namespaces, queue names) from configuration, and provide a documented example with no real secrets (e.g. an example env file).
7. **Tests**: Add the unit and integration/contract tests from the spec's Test Plan, using each component's existing test framework and layout.
8. **Self-Check**: Run each affected component's build, lint, typecheck, and unit test commands from the Profile, and fix what you broke.
9. **Handoff**: Hand off to the **QA Engineer** (`.agents/skills/audit_code/SKILL.md`).
