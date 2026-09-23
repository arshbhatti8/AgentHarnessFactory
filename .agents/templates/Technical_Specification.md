# Technical Specification: `<title>`

> Written by the Product Manager at `docs/Technical_Specification.md`. Describes **what** is
> built in this cycle. For how the repository is built, run, and tested, see
> `docs/Project_Profile.md`.

## 1. Executive Summary
A short, high-level overview of the feature or application and why it exists.

## 2. Requirements
### Functional
Numbered acceptance criteria (`AC-1`, `AC-2`, …). Each one must be objectively testable.
### Non-functional
Performance, reliability, security, observability, compatibility; only what matters here.
### User / System Flows
Step-by-step flows through the system, crossing component boundaries where relevant.
### Out of Scope
What this cycle deliberately does not do.

## 3. Scope & Affected Components
| Component | New / Changed | Summary of work |
|-----------|---------------|-----------------|

## 4. Architecture & Tech Stack
Design per affected component. For greenfield work or new components, state and briefly justify
the language, framework, and tooling. For existing components, follow the Project Profile and
note any deviation (and why) explicitly.

## 5. Interfaces & Contracts
Every boundary between components or with external systems: HTTP/RPC endpoints, events and
messages, queue/topic names, workflow and task signatures, function or module APIs, CLI
arguments, file formats. Give exact names, inputs, outputs, errors, and versioning. Both sides
of each contract must be implemented exactly as written here.

## 6. State Management & Data Flow
Where state lives, who owns it, how it changes, and how data moves between components.
Include persistence, schema/migration changes, and consistency or retry semantics.

## 7. Framework Invariants for This Change
The invariants from the Project Profile that this work touches, plus any new ones it introduces.

## 8. Test Plan
- **Unit:** per component, mapped to acceptance criteria.
- **Integration / contract:** across the boundaries in section 5.
- **Smoke:** the end-to-end check that proves the feature works when running.

## 9. Assumptions & Open Questions
Defaults chosen where the request was ambiguous, for the user to confirm at the approval gate.
