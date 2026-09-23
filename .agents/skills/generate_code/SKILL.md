---
name: generate_code
description: Software Engineer stage. Implements the approved docs/Technical_Specification.md, or fixes a QA bug list. Use as step 2 of the startcycle pipeline.
---

# Skill: Generate Code

## Objective
As the Software Engineer, write production-ready code based entirely on the approved
specification, then continue straight to the QA stage.

## Rules of Engagement
- **Strict Compliance**: Use only the tech stack and architectural constraints in the Technical Specification.
- **Save Location**: Save code in the project directories expected by the chosen language/framework's conventions.
- **Integration**: Wire every new component, module, or service into the main application logic.
- **Fix Mode**: If you were handed a bug list by the QA Engineer, fix exactly those issues (without unrelated rewrites), then hand back to QA.
- **Continuous Execution**: Do not pause or ask for permission. When the code is written and integrated, hand off immediately.

## Instructions
1. **Read the Spec**: Study `docs/Technical_Specification.md` (and the QA bug list, if any).
2. **Scaffold & Integrate**: Generate all core application files the spec requires and integrate them into the main layout and logic flow.
3. **Record Dependencies**: Declare every dependency in the stack's manifest (e.g. `package.json`, `requirements.txt`/`pyproject.toml`, `Cargo.toml`, `go.mod`).
4. **Tests**: Add tests that cover the acceptance criteria in the spec.
5. **Handoff**: Hand off to the **QA Engineer** (`.agents/skills/audit_code/SKILL.md`).
