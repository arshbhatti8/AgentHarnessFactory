---
description: Start the Autonomous AI Developer Pipeline sequence with a new idea
---

When the user types `/startcycle <idea>`, orchestrate the development process strictly using the defined `.agents/skills/`.

### Execution Sequence:
1. Act as the **Product Manager** and execute the `write_specs.md` skill using the `<idea>`.
   *(Wait for the user to explicitly approve the spec. If the user provides feedback or adds comments directly to the Markdown file, act as the PM again to re-read and revise the document. Loop this step until they type "Approved").*
2. Shift context, act as the **Software Engineer**, and execute the `generate_code.md` skill.
3. Shift context, act as the **QA Engineer**, and execute the `audit_code.md` skill.
4. Shift context, act as the **Version Control Specialist**, and execute the `version_control.md` skill.
5. Shift context, act as the **DevOps/Build Engineer**, and execute the `build_and_deploy.md` skill.
