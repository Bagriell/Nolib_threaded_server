import json
from enum import Enum
from typing import Any
import re
from datetime import datetime

REQUIRED_FIELDS = [
    "resourceType",
    "resourceId",
    "eventType",
    "triggeredAt",
    "triggeredBy",
]


class Event_types(Enum):
    CREATE = "resourceHasBeenCreated"
    UPDATE = "resourceHasBeenUpdated"
    DELETED = "resourceHasBeenDeleted"


def validate_resource_type(value: Any) -> bool:
    return isinstance(value, str) and value == "customer"


def validate_resource_id(value: Any) -> bool:
    return isinstance(value, int)


def validate_event_type(value: Any) -> bool:
    return isinstance(value, str) and value in [
        event_type.value for event_type in Event_types
    ]


def validate_triggered_at(value: Any) -> bool:

    # datetime checking infer time if not provided
    return isinstance(value, str) and bool(datetime.fromisoformat(value))


def validate_triggered_by(value: Any) -> bool:
    return isinstance(value, str) and bool(
        re.match("^server-[0-9]{1,100}$", value)
    )


def validate_data(raw_data: bytes) -> bool:

    try:
        data = json.loads(raw_data)
        if not all(field in data["properties"] for field in REQUIRED_FIELDS):
            raise ValueError("Incorrect json format.")
        if not all(
            [
                validate_resource_type(data["properties"]["resourceType"]),
                validate_resource_id(data["properties"]["resourceId"]),
                validate_event_type(data["properties"]["eventType"]),
                validate_triggered_at(data["properties"]["triggeredAt"]),
                validate_triggered_by(data["properties"]["triggeredBy"]),
            ]
        ):
            raise ValueError("Incorrect properties json format.")
    except Exception as error:
        print(error)
        return False
    return True
