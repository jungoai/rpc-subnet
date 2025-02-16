# RPC Subnet 

## Build Docker Image

Pre requirement: [rye](https://rye.astral.sh/guide/installation/)

```bash
rye build --wheel --clean
docker build . --tag your-image-name
```

## Run with Docker

```bash
cp .env.example .env
```

Then set parameters in `.env`.

Run Worker:
```bash
. ./run_docker_rpc_worker.sh
```

Run Monitor:
```bash
. ./run_docker_rpc_monitor.sh
```
