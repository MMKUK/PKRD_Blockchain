# tx_engine.py
# Handles TX mempool and gas enforcement (shared via mempool.json)

import json
import time
import os

MEMPOOL_FILE = "mempool.json"
FLAT_GAS_FEE = 0.001

def load_mempool():
    if os.path.exists(MEMPOOL_FILE):
        with open(MEMPOOL_FILE, "r") as f:
            return json.load(f)
    return []

def save_mempool(mempool):
    with open(MEMPOOL_FILE, "w") as f:
        json.dump(mempool, f, indent=4)

def create_tx(sender, receiver, amount, zkproof, nonce, gas=FLAT_GAS_FEE):
    tx = {
        "from": sender,
        "to": receiver,
        "amount": float(amount),
        "zkproof": zkproof,
        "nonce": nonce,
        "gas": float(gas),
        "timestamp": int(time.time())
    }

    if tx["gas"] < FLAT_GAS_FEE:
        print("❌ Insufficient gas fee. Required:", FLAT_GAS_FEE)
        return None

    mempool = load_mempool()
    mempool.append(tx)
    save_mempool(mempool)
    print("✅ TX added to mempool.")
    return tx

def get_mempool():
    return load_mempool()

def clear_mempool():
    save_mempool([])