#!/usr/bin/env python3

import sys
import json
import time
import hashlib
import os

from tx_engine import create_tx, get_mempool

# ✅ Signature verification with float formatting fix
def is_signature_valid(tx, private_key="secretkey123"):
    try:
        amount_str = format(float(tx['amount']), '.1f')
        msg = f"{tx['from']}:{tx['to']}:{amount_str}:{tx['nonce']}:{tx['zkproof']}"
        expected = hashlib.sha256(f"{msg}:{private_key}".encode()).hexdigest()
        return expected == tx.get("signature", "")
    except Exception as e:
        print("❌ Signature check failed:", e)
        return False

# ✅ Main CLI Entry
def main():
    if len(sys.argv) < 2:
        print("Usage: pkrd-node <command>")
        sys.exit(1)

    cmd = sys.argv[1]
    args = sys.argv[1:]

    if cmd == "tx":
        if len(args) < 2:
            print("TX Commands:")
            print("  send <from> <to> <amount>")
            print("  receive")
            print("  mempool")
            sys.exit(1)

        subcmd = args[1]

        if subcmd == "send":
            if len(args) != 5:
                print("Usage: pkrd-node tx send <sender> <receiver> <amount>")
                sys.exit(1)

            sender = args[2]
            receiver = args[3]
            amount = args[4]
            nonce = str(int(time.time()))
            zkproof = hashlib.sha256(f"{sender}:{receiver}:{amount}:{nonce}".encode()).hexdigest()

            private_key = "secretkey123"
            amount_str = format(float(amount), '.1f')
            message = f"{sender}:{receiver}:{amount_str}:{nonce}:{zkproof}"
            signature = hashlib.sha256(f"{message}:{private_key}".encode()).hexdigest()

            tx = create_tx(sender, receiver, amount, zkproof, nonce)
            tx["signature"] = signature

            if tx:
                print("📦 TX added with zkProof & gas.")
                print(f"🧠 Mempool size: {len(get_mempool())}")
                with open("outbox.json", "w") as f:
                    json.dump([tx], f, indent=4)
                print("📡 TX broadcasted to outbox.json")

        elif subcmd == "receive":
            if not os.path.exists("inbox.json"):
                print("📭 No inbox.json found. No TXs received.")
                return

            with open("inbox.json", "r") as f:
                txs = json.load(f)

            accepted = 0
            for tx in txs:
                print(f"🔍 Validating TX: {tx}")
                if not is_signature_valid(tx):
                    print("❌ TX Signature invalid. Rejected.")
                    continue

                get_mempool().append(tx)
                print("✅ TX Signature verified. Added to mempool.")
                accepted += 1

            print(f"📥 Received {accepted} TX(s) from inbox.json")

        elif subcmd == "mempool":
            pool = get_mempool()
            print(f"📥 Mempool contains {len(pool)} TX(s):")
            for tx in pool:
                print(" -", tx)

        else:
            print("Unknown TX subcommand.")

    else:
        print("Unknown command. Try: pkrd-node tx ...")

if __name__ == "__main__":
    main()