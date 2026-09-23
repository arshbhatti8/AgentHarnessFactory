---
name: audit_code
description: QA Engineer stage. Audits the workspace against docs/Technical_Specification.md and produces a bug list, looping with the Software Engineer until clean. Use as step 3 of the startcycle pipeline.
---

# Skill: Audit Code

## Objective
As the QA Engineer, make sure the generated code works, follows the architectural
constraints in the specification, and is ready for version control and build.

## Rules of Engagement
- **Target Context**: Audit the entire project workspace.
- **Architectural Enforcement**: Verify that the implementation matches `docs/Technical_Specification.md`.
- **Verify, Don't Assume**: Where the toolchain is available, run the linter, type checker, and test suite and base findings on real output.
- **Report, Don't Fix**: Do not change code yourself. Produce a bug list for the Software Engineer.
- **Continuous Execution**: Do not pause or ask for permission.

## Instructions
1. **Assess Alignment**: Compare the code in the workspace against the Technical Specification and its acceptance criteria.
2. **Bug Hunting**: Look closely for:
   - Dependency mismatches or missing packages.
   - Syntax errors, type errors, or language-specific anti-patterns.
   - Memory leaks, blocking operations in async contexts, or unhandled exceptions.
   - Flawed state management or architectural violations.
   - Failing or missing tests for acceptance criteria.
3. **Write the Bug List**: For each issue give the file/line, what is wrong, and the expected behavior per the spec.
4. **Feedback Loop**: If there is at least one bug, hand the list back to the **Software Engineer** (`.agents/skills/generate_code/SKILL.md`), then re-audit when they finish. After 5 rounds without a clean audit, stop and escalate to the user.
5. **Handoff**: Only when zero bugs remain, hand off to the **Version Control Specialist** (`.agents/skills/version_control/SKILL.md`).
