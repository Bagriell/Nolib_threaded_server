from urllib.request import Request, urlopen
from threading import Thread
import json


def make_request():
    data = {
        "properties": {
            "resourceType": "customer",
            "resourceId": 35,
            "eventType": "resourceHasBeenCreated",
            "triggeredAt": "2018-11-13T20:20:39+00:00",
            "triggeredBy": "server-25",
        }
    }
    encoded = json.dumps(data).encode()
    headers = {
        "Content-Type": "application/json",
        "Content-Length": len(encoded),
    }
    req = Request(
        "http://localhost:8000/event", encoded, headers, method="POST"
    )
    res = urlopen(req).read()
    print(req.getcode)


def main():
    port = 8000
    for _ in range(5):
        Thread(target=make_request).start()


main()
