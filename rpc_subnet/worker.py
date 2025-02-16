from fastapi            import HTTPException
from jungo_sdk          import NodeError, add_args_worker_and_conf, mk_worker_from_args
from werkzeug.wrappers  import Request, Response
from werkzeug.serving   import run_simple

import bittensor as bt
import traceback
import argparse
import requests
import json


def main():
    run()

def run():
    parser = argparse.ArgumentParser()
    try:
        conf = add_args_worker_and_conf(parser)
        args = parser.parse_args()
        worker = mk_worker_from_args(args, conf)
        run_simple("0.0.0.0", worker.port, application)
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
    try:
        run_simple("127.0.0.1", 4000, application)
    except HTTPException as e:
        bt.logging.info(f"HTTPException: {e}")
    except Exception as e:
        bt.logging.error(f"Internal error: {e}")
        traceback.print_exc()

@Request.application
def application(req):
    req_log = json.loads(req.data.decode("utf-8"))
    bt.logging.info(f"Request: {req_log}")

    headers = { 'content-type': 'application/json' }

    with open("providers.json", "r") as file:
        providers = json.load(file)
    urls = providers.get("urls")

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

if __name__ == '__main__':
    main()
