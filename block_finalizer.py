# block_finalizer.py
# Finalizes all TXs in mempool into a numbered block (block_2.json, block_3.json, etc)

import json
import time
import os
from tx_engine import get_mempool, clear_mempool

def get_next_block_number():
    existing_blocks = [f for f in os.listdir() if f.startswith("block_") and f.endswith(".json")]
    numbers = [int(f.replace("block_", "").replace(".json", "")) for f in existing_blocks if f.replace("block_", "").replace(".json", "").isdigit()]
    return max(numbers, default=1) + 1

def finalize_block():
    mempool = get_mempool()
    if not mempool:
        print("⚠️ No transactions in mempool. Nothing to finalize.")
        return

    block_number = get_next_block_number()
    block = {
        "block_number": block_number,
        "timestamp": int(time.time()),
        "transactions": mempool
    }

    filename = f"block_{block_number}.json"
    with open(filename, "w") as f:
        json.dump(block, f, indent=4)

    print(f"✅ Block {block_number} finalized with {len(mempool)} TX(s).")
    clear_mempool()

if __name__ == "__main__":
    finalize_block()