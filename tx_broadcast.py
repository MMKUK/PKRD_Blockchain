# tx_broadcast.py
# Handles TX broadcast simulation for PKRD nodes

import json
import os

OUTBOX_FILE = "outbox.json"
INBOX_FILE = "inbox.json"

def broadcast_tx(tx):
    """
    Simulates broadcasting a TX by saving it to outbox.json.
    """
    outbox = []

    # Load existing outbox
    if os.path.exists(OUTBOX_FILE):
        with open(OUTBOX_FILE, "r") as f:
            outbox = json.load(f)

    outbox.append(tx)

    # Save updated outbox
    with open(OUTBOX_FILE, "w") as f:
        json.dump(outbox, f, indent=4)

    print("📡 TX broadcasted to outbox.json")

def receive_txs():
    """
    Simulates reading TXs from inbox.json (received from network).
    """
    if not os.path.exists(INBOX_FILE):
        print("📭 No inbox.json found. No TXs received.")
        return []

    with open(INBOX_FILE, "r") as f:
        inbox = json.load(f)

    print(f"📥 Received {len(inbox)} TX(s) from inbox.json")
    return inbox