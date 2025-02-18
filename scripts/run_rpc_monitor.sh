#!/bin/bash

source .env

rpc-monitor \
    --wallet.name   "$RPC_SUBNET_MONITOR_COLDKEY" \
    --wallet.hotkey "$RPC_SUBNET_MONITOR_HOTKEY" \
    --netuid        "$RPC_SUBNET_NETUID" \
    --chain         "$RPC_SUBNET_CHAIN" \
    --logging.debug

    # --fast_blocks \
