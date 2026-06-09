import os
import json
import sys
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOCK_JIRA_FILE = os.path.join(ROOT_DIR, ".agents", "mock_jira.json")
STATE_FILE = os.path.join(ROOT_DIR, ".agents", "state.json")

def load_json(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r") as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

def pull_first_active():
    jira_data = load_json(MOCK_JIRA_FILE)
    if not jira_data or "tickets" not in jira_data:
        print("Error: mock_jira.json not initialized correctly.")
        sys.exit(1)

    active_id = jira_data.get("active_ticket_id")
    active_ticket = None

    if active_id:
        # Retrieve currently active ticket
        for t in jira_data["tickets"]:
            if t["ticket_id"] == active_id:
                active_ticket = t
                break
    else:
        # Pull first TODO ticket
        for t in jira_data["tickets"]:
            if t["status"] == "TODO":
                t["status"] = "IN_PROGRESS"
                jira_data["active_ticket_id"] = t["ticket_id"]
                active_ticket = t
                save_json(MOCK_JIRA_FILE, jira_data)
                break

    if not active_ticket:
        print("No active or pending tickets found in the backlog.")
        return False

    # Update state.json to transition to PLANNING stage for this active ticket
    state = load_json(STATE_FILE) or {}
    state["current_stage"] = "PLANNING"
    state["last_updated"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    state["active_task"] = {
        "jira_ticket": active_ticket.get("ticket_id"),
        "summary": active_ticket.get("summary", ""),
        "status": "IN_PROGRESS",
        "progress_notes": f"Pulled ticket {active_ticket.get('ticket_id')} via local mock_jira.json file.\n\nDescription:\n{active_ticket.get('description')}"
    }
    state["qa_validation"] = {
        "tests_passed": False,
        "build_logs_path": "",
        "error_summary": ""
    }
    save_json(STATE_FILE, state)

    print(f"Successfully pulled ticket {active_ticket.get('ticket_id')}: '{active_ticket.get('summary')}'")
    print("State ledger current_stage flipped to 'PLANNING'.")
    return True

def update_status(status):
    jira_data = load_json(MOCK_JIRA_FILE)
    if not jira_data or "tickets" not in jira_data:
        print("Error: mock_jira.json not initialized correctly.")
        sys.exit(1)

    active_id = jira_data.get("active_ticket_id")
    if not active_id:
        print("Error: No active ticket to update status for.")
        sys.exit(1)

    updated = False
    for t in jira_data["tickets"]:
        if t["ticket_id"] == active_id:
            t["status"] = status
            updated = True
            break

    if not updated:
        print(f"Error: Active ticket ID {active_id} not found in tickets list.")
        sys.exit(1)

    if status == "DONE":
        jira_data["active_ticket_id"] = None

    save_json(MOCK_JIRA_FILE, jira_data)
    print(f"Jira Ticket {active_id} status updated to {status}.")

def populate_backlog(filepath):
    if not os.path.exists(filepath):
        print(f"Error: Backlog file {filepath} not found.")
        sys.exit(1)
    
    try:
        with open(filepath, "r") as f:
            tickets = json.load(f)
    except Exception as e:
        print(f"Error reading JSON backlog file: {e}")
        sys.exit(1)

    if not isinstance(tickets, list):
        print("Error: Backlog file must contain a JSON list of ticket objects.")
        sys.exit(1)

    jira_data = {
        "active_ticket_id": None,
        "tickets": tickets
    }
    save_json(MOCK_JIRA_FILE, jira_data)
    print(f"Successfully populated JIRA backlog with {len(tickets)} tickets.")

def usage():
    print("Jira MCP Simulator CLI (Multi-Ticket)")
    print("Usage:")
    print("  python jira_mcp_mock.py pull-first-active")
    print("  python jira_mcp_mock.py update --status <status>")
    print("  python jira_mcp_mock.py populate-backlog <json_file_path>")
    sys.exit(1)

def main():
    if len(sys.argv) < 2:
        usage()

    cmd = sys.argv[1]
    if cmd == "pull-first-active":
        pull_first_active()
    elif cmd == "update":
        status = None
        for i in range(2, len(sys.argv)):
            if sys.argv[i] == "--status" and i + 1 < len(sys.argv):
                status = sys.argv[i + 1]
        if not status:
            usage()
        update_status(status)
    elif cmd == "populate-backlog":
        if len(sys.argv) < 3:
            usage()
        filepath = sys.argv[2]
        populate_backlog(filepath)
    else:
        usage()

if __name__ == "__main__":
    main()
