---
description: Start the Autonomous AI Developer Pipeline sequence with a new idea
---

# Workflow: Start Cycle

Input: `<idea>`, the user's raw feature or application idea (everything after `startcycle`).
If no idea was given, ask the user for one and stop.

Follow the global rules in `AGENTS.md`. For each stage, read the named skill file and
execute its instructions in full before moving on.

## Execution Sequence

1. **Product Manager**: execute `.agents/skills/write_specs/SKILL.md` with `<idea>`.
   - **Approval gate:** Present a summary of the spec and ask the user to review
     `docs/Technical_Specification.md`. Wait for the reply.
   - If the user gives feedback (in chat or by editing/commenting in the Markdown file),
     re-read the file, revise the spec, and ask again.
   - Repeat until the user replies "Approved" (case-insensitive). Do not continue before that.
2. **Software Engineer**: execute `.agents/skills/generate_code/SKILL.md`.
3. **QA Engineer**: execute `.agents/skills/audit_code/SKILL.md`.
   - If bugs are found, return to step 2 with the bug list, then audit again.
   - Maximum 5 rounds; after that, stop and escalate to the user.
4. **Version Control Specialist**: execute `.agents/skills/version_control/SKILL.md`.
5. **DevOps/Build Engineer**: execute `.agents/skills/build_and_deploy/SKILL.md`.
6. **Final report**: summarize for the user what was built, where it lives, the commits
   created, how to run it, and any open issues.

Announce each stage switch on its own line, e.g. `--- Handoff: Software Engineer ---`.
