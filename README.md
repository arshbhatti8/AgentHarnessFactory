# Multi-Agent Software Engineering Factory

Welcome to the **Multi-Agent Software Engineering Factory** repository. This project coordinates a set of specialized, autonomous agents through sequential lifecycle stages to plan, build, and test applications in isolated environments.

---

## 1. Project Overview & Objective

The main objective of this repository is to provide a standardized, automated harness for orchestrating multi-agent software engineering pipelines. By partitioning agent operations into dedicated workspace folders and coordinating progress through a central state ledger, the factory allows agents to work collaboratively without colliding or corrupting the repository's main history.

---

## 2. Directory Structure & Workspace Boundaries

To support autonomous operations, the repository is organized into distinct, isolated workspaces governed by strict agent boundaries:

```
.
├── .agents/                    # Central state ledger, JIRA backlog mocks, and hooks
├── build_workspace/            # Sandbox directory for implementation and compilation
├── planner_workspace/          # Sandbox directory for specifications and design guides
├── qa_workspace/               # Sandbox directory for writing and executing test suites
├── Dockerfile                  # Container definition for localized pipeline runs
└── README.md                   # Harness documentation
```

### Agent Roles & Workspaces
* **Planner Agent** (`/planner_workspace/`): Responsible for breaking down product specifications, drafting implementation guides, and outlining architecture blueprints.
* **Dependencies Setup Agent** (Config level): Configures package/library runtimes and manages dependencies inside `build_workspace/` and `qa_workspace/`.
* **Generator Agent** (`/build_workspace/`): Implements the core logic, databases, APIs, and client-side interfaces.
* **QA Evaluator Agent** (`/qa_workspace/`): Writes E2E testing suites, integration scripts, and runs code validation.

---

## 3. State Handoff & Loop Automation

The factory orchestrates agent handoffs using a central state ledger.

### The Pipeline Lifecycle
The pipeline transitions through the following sequential stages:

$$\text{PLANNING} \rightarrow \text{DEPENDENCIES} \rightarrow \text{GENERATION} \rightarrow \text{EVALUATION} \rightarrow \text{DONE}$$

1. **State Ledger** (`.agents/state.json`): Tracks the active stage, active JIRA ticket details, and validation reports.
2. **Execution Hook** (`.agents/hooks.json`): Triggers post-execution processing hooks (e.g., `python .agents/on_loop_stop.py`) on loop termination.
3. **Loop Stop Processor** (`.agents/on_loop_stop.py`):
   - Monitors the state.
   - If the active stage transitions to `DONE`, it marks the current ticket as completed in `.agents/mock_jira.json`.
   - If there are remaining tickets in the backlog, it automatically transitions the state back to `PLANNING` and assigns the next ticket, keeping the agent loop running.
   - When all tickets are completed, it fires a final webhook notification to external integration services (e.g., n8n).

### JIRA MCP Simulator CLI
You can simulate ticket backlog transitions locally using the utility script:
- **Pull first pending ticket**: `python .agents/jira_mcp_mock.py pull-first-active`
- **Update ticket status manually**: `python .agents/jira_mcp_mock.py update --status <status>`
- **Load backlog from file**: `python .agents/jira_mcp_mock.py populate-backlog <json_file_path>`

---

## 4. Execution & Verification

### Running inside Docker
You can run the entire testing and verification loop within a containerized environment:

```bash
# Build the Docker image
docker build -t agent-harness-factory .

# Run the test suites
docker run --rm agent-harness-factory
```

### Running Tests Locally
To execute the test suites manually outside of Docker:
```bash
python -m unittest discover -s qa_workspace -p "*_test.py"
```

> [!NOTE]
> All local and remote changes must be merged and pushed to the `main` branch. Ensure that agent operations respect their designated workspace bounds to prevent merge conflicts and state pollution.