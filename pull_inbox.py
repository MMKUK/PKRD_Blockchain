# pull_inbox.py
# Pulls latest inbox.json from GitHub

import os

print("📥 Pulling latest inbox.json from GitHub...")
os.system("git pull origin main")

if os.path.exists("inbox.json"):
    print("✅ inbox.json is updated and ready.")
else:
    print("⚠️ inbox.json not found after pull.")