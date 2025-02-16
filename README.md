# RPC Subnet 

## Pre requirement

[rye](https://rye.astral.sh/guide/installation/)

## Run in virtual environment 

Install deps:
```bash
rye sync
```

Enter virtual environment:
```bash
. .venv/bin/activate
```

Create `.env` file
```bash
cp .env.example .env
```

Customize parameters in `.env`.

Activate `.env`.
```bash
. ./.env
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

## Run with Docker

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

## Ethereum JSON-RPC spec

[link](https://playground.open-rpc.org/?schemaUrl=https://raw.githubusercontent.com/ethereum/execution-apis/assembled-spec/openrpc.json&uiSchema%5BappBar%5D%5Bui:splitView%5D=false&uiSchema%5BappBar%5D%5Bui:input%5D=false&uiSchema%5BappBar%5D%5Bui:examplesDropdown%5D=false)
