# tx_signer.py
# PKRD TX Signing Module using private key + SHA256

import hashlib
import json
import sys

def hash_data(*args):
    joined = ":".join(str(a).strip() for a in args)
    return hashlib.sha256(joined.encode()).hexdigest()

def sign_tx(tx, private_key):
    message = f"{tx['from']}:{tx['to']}:{tx['amount']}:{tx['nonce']}:{tx['zkproof']}"
    signature = hash_data(message, private_key)
    tx["signature"] = signature
    return tx

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 tx_signer.py <tx_json_file> <private_key>")
        sys.exit(1)

    file_path = sys.argv[1]
    private_key = sys.argv[2]

    try:
        with open(file_path, "r") as f:
            txs = json.load(f)

        signed_txs = []
        for tx in txs:
            signed = sign_tx(tx, private_key)
            signed_txs.append(signed)

        # Overwrite with signed TXs
        with open(file_path, "w") as f:
            json.dump(signed_txs, f, indent=4)

        print(f"✅ Signed {len(signed_txs)} TX(s) and saved to {file_path}")
    except Exception as e:
        print("❌ Error signing TX:", e)

if __name__ == "__main__":
    main()

