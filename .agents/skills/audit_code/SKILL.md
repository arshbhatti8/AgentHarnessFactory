---
name: audit_code
description: QA Engineer stage. Audits every affected component against the spec, cross-component contracts, and framework invariants using the commands in docs/Project_Profile.md, looping with the Software Engineer until clean. Use as step 3 of the startcycle pipeline.
---

# Skill: Audit Code

## Objective
As the QA Engineer, make sure the implementation works, honors every contract and framework
invariant, and is ready for version control and build, whatever the language or framework.

## Rules of Engagement
- **Target Context**: Audit every component the spec lists as affected, plus anything that depends on them.
- **Verify, Don't Assume**: Run each affected component's lint, typecheck, build, and test commands from `docs/Project_Profile.md`, and base findings on the real output. If a runtime service needed for integration tests is available, start it and run those tests too. If it is not available, say so.
- **Judge by the Stack**: Apply the idioms, pitfalls, and best practices of each component's own language and framework, not those of any other stack.
- **Report, Don't Fix**: Do not change code yourself. Produce a bug list for the Software Engineer.
- **Continuous Execution**: Do not pause or ask for permission.

## Instructions
1. **Spec Alignment**: Check that every acceptance criterion in `docs/Technical_Specification.md` is implemented and covered by a test.
2. **Tool Checks**: Run the Profile's lint, typecheck, build, and test commands for each affected component, and record every failure.
3. **Contract Verification**: For each boundary in "Interfaces & Contracts", check that both sides agree exactly: names, paths, payload shapes, types, error handling, serialization, versioning.
4. **Framework Invariants**: Check every rule under Framework Invariants in the Profile and spec, using its "How to check" method. Treat any violation as a bug.
5. **Bug Hunting**: Also look for:
   - Missing, undeclared, or conflicting dependencies.
   - Syntax, type, and language-specific anti-patterns.
   - Resource leaks, blocking or unbounded work, race conditions, unhandled errors.
   - Incorrect state management, data consistency, or retry/idempotency behavior.
   - Hard-coded secrets or environment-specific values; unsafe input handling.
   - Code missing from entry points: routes, registrations, worker/process setup, exports.
6. **Write the Bug List**: For each issue give the component, file/line, what is wrong, the evidence (command output or reasoning), and the expected behavior per the spec.
7. **Feedback Loop**: If there is at least one bug, hand the list back to the **Software Engineer** (`.agents/skills/generate_code/SKILL.md`), then re-audit when they finish. After 5 rounds without a clean audit, stop and escalate to the user.
8. **Handoff**: Only when zero bugs remain, hand off to the **Version Control Specialist** (`.agents/skills/version_control/SKILL.md`).
