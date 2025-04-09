#!/bin/bash

GETH_PATH="./geth"
DATADIR="./pkrd-data"
FOUNDER_ADDRESS="0x6a517CCcf02eE802FAfDd0b9E3AC9ab039ccd465"
PASSWORD_PATH="./password.txt"

echo "🔗 Starting PKRD Node with Auto Signer..."

$GETH_PATH --datadir "$DATADIR" \
  --networkid 98765 \
  --unlock "$FOUNDER_ADDRESS" \
  --password "$PASSWORD_PATH" \
  --mine \
  --allow-insecure-unlock \
  --miner.etherbase "$FOUNDER_ADDRESS" \
  --miner.gasprice 100000000000000 \
  --rpc.txfeecap 0.0001 \
  --syncmode full \
  --verbosity 3 \
  --http --http.api personal,eth,net,web3,txpool \
  --http.corsdomain "*" \
  --http.addr "127.0.0.1" \
  --http.port 8545 \
  --ws --ws.api eth,net,web3 \
  --ws.addr "127.0.0.1" \
  --ws.port 8551 \
  --ws.origins "*" \
  --authrpc.jwtsecret "$DATADIR/geth/jwtsecret" \
  --mine --miner.etherbase "$FOUNDER_ADDRESS"