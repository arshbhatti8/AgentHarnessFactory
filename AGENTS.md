# GLOBAL WORKSPACE RULES & AGENT BOUNDARIES

Welcome to the Multi-Agent Software Engineering Factory. This file defines the global rules and operational boundaries that all agents must strictly adhere to.

## 1. Directory Structure & Assigned Workspaces

All operations must be contained within their respective workspaces:
- **Planner Agent**: Strictly restricted to `/planner_workspace/`.
- **Dependencies Setup Agent**: Permitted to write configuration files and execute setup/installation commands inside `/build_workspace/` and `/qa_workspace/`. Pre-authorized to run CLI commands to install software and package runtimes without user prompts.
- **Generator Agent**: Strictly restricted to `/build_workspace/` (writing application code). Pre-authorized to execute compilation, build scripts, dev servers, and language check commands (such as Node, npm, python3, npx, pip) inside `/build_workspace/` without user prompts.
- **QA Evaluator Agent**: Strictly restricted to `/qa_workspace/` (writing and running validation tests). Pre-authorized to run any test suite execution commands, web testing runners (e.g., pytest, playright, puppeteer, unittest), and diagnostic scripts inside `/qa_workspace/` without user prompts.

> [!IMPORTANT]
> No agent is permitted to modify or create files outside of its designated workspace directory, with the sole exception of the central state ledger `.agents/state.json` as defined in the state handoff protocol.

## 2. State Handoff Protocol

Inter-agent coordination must strictly occur by reading and modifying the central state handoff memory ledger:
- File path: `file:///.agents/state.json`
- Agents must wait until `current_stage` matches their active stage before performing actions. The pipeline stages run in the following sequence:
  
  $$\text{PLANNING} \rightarrow \text{DEPENDENCIES} \rightarrow \text{GENERATION} \rightarrow \text{EVALUATION} \rightarrow \text{DONE}$$

- After completing their work, agents must update the state ledger and flip the `current_stage` to the next phase in the pipeline to pass execution to the next agent.

## 3. Context Compaction & Log Management

To prevent context window degradation:
- Do not paste raw build or test logs larger than 100 lines into prompt history or conversation messages.
- Dump large logs into dedicated log files within the agent's workspace directory (e.g., `/qa_workspace/build.log` or `/build_workspace/compile.log`).
- Provide only a summarized error report/status in `state.json` and refer to the absolute path of the workspace log file for full details.
