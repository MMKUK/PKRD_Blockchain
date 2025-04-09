#!/bin/bash
# Push local outbox.json to GitHub

echo "🔄 Syncing outbox.json to GitHub..."

git add outbox.json
git commit -m "📡 Updated outbox.json from node"
git push origin main

echo "✅ Push complete."