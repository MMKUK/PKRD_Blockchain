# 🚀 PKRD Node — Minimal Blockchain Framework

A simple and powerful prototype blockchain node in Python featuring:

- ✅ zkProof validation (RingCT-style)
- ✅ Digital Signature verification
- ✅ Mempool handling + TX sealing
- ✅ CLI-based TX flow
- ✅ Web wallet UI (`pkrd_pay.html`)
- ✅ Live blockchain explorer (`explorer_auto.html`)

---

## 🔧 Components

| File                | Purpose                             |
|---------------------|-------------------------------------|
| `pkrd-node.py`      | Main CLI node for TX & validation   |
| `tx_engine.py`      | Handles TX creation & mempool logic |
| `block_finalizer.py`| Finalizes block from mempool        |
| `pkrd_pay.html`     | Web UI to sign & verify TXs         |
| `explorer_auto.html`| Live blockchain explorer view       |

---

🌐 [PKRD Explorer (Live)](https://mmkuk.github.io/PKRD-NodeSync/explorer_auto.html)

## 🧪 Run Locally

```bash
python3 pkrd-node.py tx send 0xAAA 0xBBB 123
mv outbox.json inbox.json
python3 pkrd-node.py tx receive
python3 block_finalizer.py