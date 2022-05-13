import json
import sys
import time
import requests
import yaml

def get_status_msg(status):
    if status == 'OFF':
        return "OFF \U0000274C"
    else:
        return "ON \U0001F49A"

if __name__ == "__main__":
    args = {}
    with open("args.yaml", "r") as stream:
        try:
            args = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise exc

    serverUrl = f"http://{args['serverIP']}:{args['serverPort']}/ac/{args['buildingName']}/{args['roomNumber']}"

    while True:
        response = requests.get(serverUrl)
        status = json.loads(response.text)

        sys.stdout.write(f"\rTHE AIR CONDITIONING IS: {get_status_msg(status['status'])}")
        sys.stdout.flush()
        time.sleep(5)
