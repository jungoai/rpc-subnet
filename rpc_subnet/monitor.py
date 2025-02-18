from time       import sleep
from jungo_sdk  import Endpoint, Uid, WorkerWeight, add_args_monitor_and_conf, lmap, mk_monitor_from_args
from jsonschema import validate, ValidationError

import bittensor as bt
import argparse
import json
import random
import requests


def main():
    run()

def run():
    parser      = argparse.ArgumentParser()
    conf        = add_args_monitor_and_conf(parser)
    args        = parser.parse_args()
    monitor     = mk_monitor_from_args(args, conf)
    tempo_sec   = monitor.tempo().second()

    with open("api.json", "r") as file:
        rpc_schema = json.load(file)
    methods = rpc_schema.get("methods", [])

    def set_weight(endpoint: Endpoint, uid: Uid) -> tuple[Uid, WorkerWeight]:
        bt.logging.debug(f"endpoint: {endpoint}, uid: {uid}")
        method = random.choice(methods)
        try:
            res = send_request(f"http://{endpoint.ip_str()}:{endpoint.port}/jsonrpc", method)
            bt.logging.debug(f"result: {res}")
            res_schema = method.get("result")
            validate(instance=res, schema=res_schema)
            bt.logging.info(f"✅ Passed")
            return (uid, 1)
        except ValidationError as e:
            bt.logging.info(f"❌ Not Expected Result: {e.message}")
            return (uid, 0)
        except Exception as e:
            bt.logging.info(f"❌ Request Failed: {e}")
            return (uid, 0)

    while True:
        monitor.set_weights_with(set_weight)
        sleep(tempo_sec)

def run_debug():
    parser = argparse.ArgumentParser()
    bt.logging.add_args(parser)

    with open("api.json", "r") as file:
        rpc_schema = json.load(file)
    methods = rpc_schema.get("methods", [])
    method = random.choice(methods)
    try:
        res = send_request("http://localhost:4000/jsonrpc", method)
        bt.logging.debug(f"result: {res}")
        res_schema = method.get("result")
        validate(instance=res, schema=res_schema)
        bt.logging.info(f"✅ Passed")
    except ValidationError as e:
        bt.logging.info(f"❌ Not Expected Result: {e.message}")
    except Exception as e:
        bt.logging.info(f"❌ Request Failed: {e}")

def send_request(url: str, method):
    method_name = method["name"]
    bt.logging.debug(f"method_name: {method_name}")

    args = lmap(lambda x: x.get("value"), method.get("examples", [])[0].get("params"))
    bt.logging.debug(f"args: {args}")

    headers = {'content-type': 'application/json'}
    id = random.randint(1, 100)
    payload = {
        "jsonrpc": "2.0",
        "method": method_name,
        "params": args,
        "id": id
    }
    resp = requests.post(url, data=json.dumps(payload), headers=headers)

    if resp.status_code == 200:
        return resp.json()["result"]
    else:
        raise Exception(f"status code: {resp.status_code}")

if __name__ == "__main__":
    main()
