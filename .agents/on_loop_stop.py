import os
import json
import urllib.request
import urllib.parse
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOCK_JIRA_FILE = os.path.join(ROOT_DIR, ".agents", "mock_jira.json")
STATE_FILE = os.path.join(ROOT_DIR, ".agents", "state.json")
DEFAULT_N8N_WEBHOOK = "http://localhost:5678/webhook/jira-update"

def log(message):
    print(f"[{datetime.now().isoformat()}] [HOOK-onLoopStop] {message}")

def load_json(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r") as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

def main():
    if not os.path.exists(STATE_FILE):
        log("Error: state.json not found.")
        return

    state = load_json(STATE_FILE)
    if not state:
        log("Error: Failed to parse state.json.")
        return

    current_stage = state.get("current_stage")
    active_task = state.get("active_task", {})
    ticket_id = active_task.get("jira_ticket")
    summary = active_task.get("summary")

    log(f"Current stage: {current_stage}")
    log(f"Active ticket: {ticket_id} - {summary}")

    if current_stage != "DONE":
        log("Stage is not DONE. Skipping loop transition check.")
        return

    # Load JIRA simulator to see if there is more work in the backlog
    jira_data = load_json(MOCK_JIRA_FILE)
    if not jira_data or "tickets" not in jira_data:
        log("Warning: mock_jira.json not configured for backlog loops. Terminating.")
        return

    # Mark the completed active ticket as DONE in the simulator
    active_id = jira_data.get("active_ticket_id") or ticket_id
    completed_any = False
    for t in jira_data["tickets"]:
        if t["ticket_id"] == active_id:
            t["status"] = "DONE"
            completed_any = True
            log(f"Marked active ticket {active_id} as DONE in JIRA backlog.")
            break

    # Find the next pending ticket
    next_ticket = None
    for t in jira_data["tickets"]:
        if t["status"] == "TODO":
            t["status"] = "IN_PROGRESS"
            jira_data["active_ticket_id"] = t["ticket_id"]
            next_ticket = t
            break

    if next_ticket:
        # Loop continuation: transition state.json back to PLANNING with the new ticket details
        state["current_stage"] = "PLANNING"
        state["last_updated"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        state["active_task"] = {
            "jira_ticket": next_ticket.get("ticket_id"),
            "summary": next_ticket.get("summary", ""),
            "status": "IN_PROGRESS",
            "progress_notes": f"Iteratively pulled next ticket {next_ticket.get('ticket_id')} via local backlog.\n\nDescription:\n{next_ticket.get('description')}"
        }
        state["qa_validation"] = {
            "tests_passed": False,
            "build_logs_path": "",
            "error_summary": ""
        }
        
        save_json(MOCK_JIRA_FILE, jira_data)
        save_json(STATE_FILE, state)
        
        log(f"Continuing pipeline: Flipped state to PLANNING for next ticket {next_ticket.get('ticket_id')}.")
        print(f"--- LOOP_CONTINUE_STAGE: PLANNING | TICKET: {next_ticket.get('ticket_id')} ---")
    else:
        # Backlog fully completed: Clear active ticket and fire final n8n webhook
        jira_data["active_ticket_id"] = None
        save_json(MOCK_JIRA_FILE, jira_data)
        
        log("All tickets in JIRA backlog are completed! Initiating final webhook termination.")
        
        webhook_url = os.environ.get("N8N_WEBHOOK_URL", DEFAULT_N8N_WEBHOOK)
        log(f"Firing HTTP POST to n8n webhook: {webhook_url}")

        payload = {
            "jira_ticket": ticket_id,
            "summary": summary,
            "status": "DONE",
            "qa_validation": state.get("qa_validation", {}),
            "last_updated": state.get("last_updated")
        }

        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            webhook_url,
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                status_code = response.getcode()
                log(f"Webhook fired successfully. Response code: {status_code}")
        except Exception as e:
            log(f"Warning: Failed to reach webhook endpoint. Exception: {e}")
            log("Process complete locally.")

if __name__ == "__main__":
    main()
