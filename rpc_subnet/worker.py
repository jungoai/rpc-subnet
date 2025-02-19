from fastapi            import HTTPException
from jungo_sdk          import Callable, NodeError, add_args_worker_and_conf, mk_worker_from_args
from werkzeug.wrappers  import Request, Response
from werkzeug.serving   import run_simple
from pathlib            import Path

import bittensor as bt
import traceback
import argparse
import requests
import json


def main():
    run()

def run():
    parser = argparse.ArgumentParser()
    conf = add_args_worker_and_conf(parser)
    parser.add_argument("--providers-file", type=Path, default= Path.home() / ".providers.json")
    args = parser.parse_args()
    providers_file = args.providers_file
    bt.logging.info(f"providers file: {providers_file}")
    with providers_file.open("r") as file:
        rpcs_json = json.load(file)
    urls = rpcs_json.get("providers")
    worker = mk_worker_from_args(args, conf)
    try:
        run_simple("0.0.0.0", worker.port, application(urls))
    except HTTPException as e:
        bt.logging.info(f"HTTPException: {e}")
    except NodeError as e:
        bt.logging.error(f"NodeError: {e}")
        traceback.print_exc()
    except Exception as e:
        bt.logging.error(f"Internal error: {e}")
        traceback.print_exc()

def run_debug():
    parser = argparse.ArgumentParser()
    bt.logging.add_args(parser)
    parser.add_argument("--providers-file", type=Path, default= Path.home() / ".providers.json")
    args = parser.parse_args()
    providers_file = args.providers_file
    bt.logging.info(f"providers file: {providers_file}")
    with providers_file.open("r") as file:
        rpcs_json = json.load(file)
    urls = rpcs_json.get("providers")
    try:
        run_simple("127.0.0.1", 4000, application(urls))
    except HTTPException as e:
        bt.logging.info(f"HTTPException: {e}")
    except Exception as e:
        bt.logging.error(f"Internal error: {e}")
        traceback.print_exc()

def application(urls: list[str]) -> Callable:
    @Request.application
    def application_(req):
        req_log = json.loads(req.data.decode("utf-8"))
        bt.logging.info(f"Request: {req_log}")

        headers = { 'content-type': 'application/json' }

        def request(urls: list[str]):
            url = urls[0]
            try:
                resp = requests.post(url, data=req.data, headers=headers)
            except Exception as e: 
                bt.logging.info(f"Got error {e} from url {url}.")
                next = try_next(urls)
                if next is not None:
                    return next
                else:
                    raise HTTPException(status_code=502, detail="Bad Gateway: Invalid response from upstream server")
            status_code = resp.status_code
            if status_code == 200:
                bt.logging.info(f"Response was ok from {url}.")
                bt.logging.info(f"Response: {resp.text}.")
                return resp
            else:
                bt.logging.info(f"Got status code {status_code} from {url}.")
                return try_next(urls) or resp

        def try_next(urls: list[str]):
            if len(urls) == 1:
                bt.logging.info(f"There is no more url.")
                return None
            else:
                bt.logging.info(f"Trying next url.")
                return request(urls[1:])

        return Response(request(urls))

    return application_

if __name__ == '__main__':
    main()
