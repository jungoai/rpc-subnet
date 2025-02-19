# RPC Subnet 

It is the RPC provider subnet of JungoAI and functions as a decentralized, 
free and open-source solution. It could serve as a replacement for centralized 
solutions such as Infura, Alchemy, and others.

To read more about what is RPC Subnet and How it works, visit [here](https://jungoai.github.io/jungo-book/builders/rpc-subnet.html).

## Run a Node

See [here](https://jungoai.github.io/jungo-book/builders/run-rpc-worker-monitor.html).

## Build and Development

Pre requirement:
[rye](https://rye.astral.sh/guide/installation/)

Installation on Linux:
```bash
curl -sSf https://rye.astral.sh/get | bash
```

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

First build the python package:
```bash
rye build --wheel --clean
```
Docker image would build from the package.
```bash
docker build . --tag your-image-name
```

## Ethereum JSON-RPC spec

[link](https://playground.open-rpc.org/?schemaUrl=https://raw.githubusercontent.com/ethereum/execution-apis/assembled-spec/openrpc.json&uiSchema%5BappBar%5D%5Bui:splitView%5D=false&uiSchema%5BappBar%5D%5Bui:input%5D=false&uiSchema%5BappBar%5D%5Bui:examplesDropdown%5D=false)
