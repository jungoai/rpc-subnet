# RPC Subnet 

## What is it?

It is the RPC provider subnet of JungoAI and functions as a decentralized, free and 
open-source solution. It could serve as a replacement for centralized solutions such as 
Infura, Alchemy, and others.

Key features:
- Permissionless: Anyone can run an RPC node and receive rewards in JUNGO.
- Trustless: Requests propagate to all nodes, and the result follows the majority. 
  Thus, the results from minority nodes are considered invalid in the presence of malicious nodes.
- Efficient: Nodes are ranked based on performance, latency, and trust, ensuring that 
  clients receive responses from the node with the lowest latency and highest trust.

Note: Currently just Ethereum RPC supported.

## How it works?

Worker nodes are RPC providers that anyone can run. On the other hand, 
monitor nodes measure the performance of worker nodes. Workers with 
higher uptime and accuracy gain more trust. On the client side, they can 
see the ranking of workers based on performance and trust. Additionally, 
the client receives responses from the geographically closest node with 
the lowest latency.

In the end, the client can choose to receive results in two ways:
- Optimistic: The client receives the result and processes it immediately. After a short delay, it receives validation.
  This method is more efficient and can be used on nodes with high trust.
- Pessimistic: The client receives a validated result, ensuring it follows the majority of nodes.

## Run a Node

If you want to run a Worker or Monitor first follow these steps:
- [Create a wallet](https://jungoai.github.io/jungo-book/builders/create-a-wallet.html) 
- [Create a hotkey](https://jungoai.github.io/jungo-book/builders/create-a-hotkey.html)
- [Register uid on rpc subnet](https://jungoai.github.io/jungo-book/builders/register-uid.html)

Note: RPC subnet is 1002 netuid

Now follow the Pre requirement, Configuration and Run with docker.

### Pre requirement

[rye](https://rye.astral.sh/guide/installation/)

### Configuration

Create `.env` file
```bash
cp .env.example .env
```
Customize parameters in `.env`.

Activate `.env`.
```bash
. ./.env
```

Create `.providers.json`
```bash
cp ./.providers.json ~/.providers.json
```

Open `.providers.json` in your favorite editor
```bash
code ~/.providers.json
```

Edit and add endpoints of RPCs you are running or getting service.

### Run with Docker

```bash
cp .env.example .env
```

Then set parameters in `.env`.

Activate `.env`.
```bash
. ./.env
```

Run Worker:
```bash
. ./scripts/run_rpc_worker_docker.sh
```

Run Monitor:
```bash
. ./scripts/run_rpc_monitor_docker.sh
```

**Note**:
If you are connecting to a local jungochain node with `fast-blocks` enabled, you should pass 
`--fast_blocks` into `./scripts/run_rpc_monitor_docker.sh`

## Run/development in virtual environment

Install deps:
```bash
rye sync
```

Enter virtual environment:
```bash
. .venv/bin/activate
```

Run Worker:
```bash
. ./scripts/run_rpc_worker.sh
```

Run Monitor:
```bash
. ./scripts/run_rpc_monitor.sh
```

**Note**:
If you are connecting to a local jungochain node with `fast-blocks` enabled, you should pass 
`--fast_blocks` into `./scripts/run_rpc_monitor.sh`

## Build Docker Image

```bash
rye build --wheel --clean
docker build . --tag your-image-name
```

## Ethereum JSON-RPC spec

[link](https://playground.open-rpc.org/?schemaUrl=https://raw.githubusercontent.com/ethereum/execution-apis/assembled-spec/openrpc.json&uiSchema%5BappBar%5D%5Bui:splitView%5D=false&uiSchema%5BappBar%5D%5Bui:input%5D=false&uiSchema%5BappBar%5D%5Bui:examplesDropdown%5D=false)
