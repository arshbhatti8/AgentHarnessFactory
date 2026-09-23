---
name: write_specs
description: Product Manager stage. Turns a raw idea into a rigorous technical specification at docs/Technical_Specification.md. Use as step 1 of the startcycle pipeline.
---

# Skill: Write Specs

## Objective
As the Product Manager, turn the user's raw idea into a rigorous technical specification
that the rest of the pipeline can implement without further clarification.

## Rules of Engagement
- **Artifact Handover**: Save all final output to the file system.
- **Save Location**: Always write the document to `docs/Technical_Specification.md` (create `docs/` if it does not exist).
- **Tech Stack Flexibility**: Choose the most appropriate architecture, language, and framework for the request and the current repository state. Justify the choice briefly.
- **No Guessing Silently**: If a requirement is ambiguous, pick a sensible default and record it under an "Assumptions" heading so the user can correct it at the approval gate.
- **Approval Gate**: This is the only stage that waits for the user. Do not start implementation until the user approves (see `.agents/workflows/startcycle.md`).

## Instructions
1. **Analyze Requirements**: Work out the functional and non-functional requirements from the idea.
2. **Draft the Document**: The specification MUST include:
   - **Executive Summary**: A brief, high-level overview of the feature or application.
   - **Requirements**: Clear acceptance criteria and user flows.
   - **Architecture & Tech Stack**: The project structure and chosen stack (languages, frameworks, databases, tooling).
   - **State Management & Data Flow**: How data flows through the application and how state is managed.
   - **Build, Run & Test Commands**: The exact commands to install dependencies, build, run, and test.
   - **Assumptions & Open Questions**: Defaults you chose and anything the user should confirm.
3. **Save Artifact**: Write the final document to `docs/Technical_Specification.md`.
4. **Request Approval**: Summarize the spec for the user and ask them to reply "Approved" or give feedback. Revise and repeat until approved.
5. **Handoff**: Once approved, hand off to the **Software Engineer** (`.agents/skills/generate_code/SKILL.md`).
