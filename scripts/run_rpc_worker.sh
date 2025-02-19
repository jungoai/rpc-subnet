#!/bin/bash

source .env

rpc-worker \
    --ip                "$RPC_SUBNET_WORKER_IP" \
    --port              "$RPC_SUBNET_WORKER_PORT" \
    --providers-file    "$RPC_SUBNET_PROVIDERS_PATH" \
    --netuid            "$RPC_SUBNET_NETUID" \
    --wallet.name       "$RPC_SUBNET_WORKER_COLDKEY" \
    --wallet.hotkey     "$RPC_SUBNET_WORKER_HOTKEY" \
    --chain             "$RPC_SUBNET_CHAIN" \
    --logging.debug
