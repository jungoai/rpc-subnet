docker run \
    --name          "rpc-monitor" \
    --network       host \
    -v              "$RPC_SUBNET_WALLET_PATH:/root/.jungoai/" \
    --log-driver    json-file                   \
    --log-opt       max-size="$LOG_MAX_SIZE"    \
    --log-opt       max-file="$LOG_MAX_FILE"    \
    -d \
    test-rpc-subnet \
        rpc-monitor \
            --wallet.name   "$RPC_SUBNET_MONITOR_COLDKEY" \
            --wallet.hotkey "$RPC_SUBNET_MONITOR_HOTKEY" \
            --netuid        "$RPC_SUBNET_NETUID" \
            --chain         "$RPC_SUBNET_CHAIN" \
            --fast_blocks \
            --logging.info
