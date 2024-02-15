from urllib.request import Request, urlopen
from threading import Thread
import json
import random
from enum import Enum


class EventTypes(Enum):
    """Enumeration defining possible types of events."""

    CREATE = "resourceHasBeenCreated"
    UPDATE = "resourceHasBeenUpdated"
    DELETED = "resourceHasBeenDeleted"


def make_request():
    data = {
        "properties": {
            "resourceType": "customer",
            "resourceId": random.randint(1, 50),
            "eventType": random.choice(list(EventTypes)).value,
            "triggeredAt": "2018-11-13T20:20:39+00:00",
            "triggeredBy": "server-25",
        }
    }
    encoded = json.dumps(data).encode()
    print(f"sending payload: {encoded}")

    headers = {
        "Content-Type": "application/json",
        "Content-Length": len(encoded),
    }
    req = Request(
        "http://localhost:8000/event", encoded, headers, method="POST"
    )
    try:
        res = urlopen(req)
        print(res.getcode())
    except Exception as error:
        print(error)


def main():
    port = 8000
    for _ in range(3):
        Thread(target=make_request).start()


main()
