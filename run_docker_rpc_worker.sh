docker run \
    --name          "rpc-worker" \
    --network       host \
    -v              "$RPC_SUBNET_WALLET_PATH:/root/.jungoai/" \
    --log-driver    json-file                   \
    --log-opt       max-size="$LOG_MAX_SIZE"    \
    --log-opt       max-file="$LOG_MAX_FILE"    \
    -d \
    test-rpc-subnet \
        rpc-worker \
            --ip            "$RPC_SUBNET_WORKER_IP" \
            --port          "$RPC_SUBNET_WORKER_PORT" \
            --netuid        "$RPC_SUBNET_NETUID" \
            --wallet.name   "$RPC_SUBNET_WORKER_COLDKEY" \
            --wallet.hotkey "$RPC_SUBNET_WORKER_HOTKEY" \
            --chain         "$RPC_SUBNET_CHAIN" \
            --logging.info
