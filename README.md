# 🚀 PKRD Blockchain — Final Autonomic Node Kit

A powerful and unstoppable blockchain framework built for eternity.  
Every node is an auto-signer. Even if one survives, the chain lives.

---

## 🌟 Key Features

- ✅ zk-RingCT privacy (untraceable, unlinkable TXs)
- ✅ Signature verification with wallet-based TX signing
- ✅ Mempool, inbox, outbox system
- ✅ Auto block finalization & sealing
- ✅ Web Wallet (`web_wallet.html`) — for TX generation
- ✅ Blockchain Explorer (`explorer_auto.html`) — live updates
- ✅ Fully Autonomous Nodes (no founder control)
- ✅ Terminal + Web integration
- ✅ Ultra-light executable node (macOS `.app`, Windows `.exe` coming)

---

## 📦 Download Node Kit

👉 [Download PKRD NodeKit ZIP](https://github.com/MMKUK/PKRD_Blockchain/raw/main/PKRD-NodeKit.zip)

Unzip and you're ready to launch.

---

## 🔧 Components Overview

| File                  | Purpose                                |
|-----------------------|----------------------------------------|
| `pkrd-node.py`        | Main CLI for node operations           |
| `tx_engine.py`        | TX creation, mempool management        |
| `tx_signer.py`        | Sign TXs with your private key         |
| `tx_broadcast.py`     | Broadcast TXs to node network          |
| `pull_inbox.py`       | Pull inbox messages (TXs)              |
| `block_finalizer.py`  | Finalize a new block from mempool      |
| `zkringct.py`         | zkProof verification engine            |
| `explorer_auto.html`  | Live mempool, block, inbox explorer    |
| `web_wallet.html`     | Web wallet UI (TX creation + signing)  |
| `start-pkrd.sh`       | Node launcher script                   |
| `sync_node.sh`        | Sync node inbox/outbox with network    |
| `constitution_hash.txt`| Immutable chain constitution hash     |

---

## 🧪 Node CLI Usage

```bash
# Send transaction
python3 pkrd-node.py tx send 0xAAA 0xBBB 100

# Move TX to inbox (simulate P2P)
mv outbox.json inbox.json

# Receive & verify transaction
python3 pkrd-node.py tx receive

# Finalize block
python3 block_finalizer.py
