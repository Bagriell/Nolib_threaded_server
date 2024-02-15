"""Module providing functions for validating event data."""

import json
import re
from datetime import datetime
from enum import Enum
from typing import Any

from logger import logger

REQUIRED_FIELDS = [
    "resourceType",
    "resourceId",
    "eventType",
    "triggeredAt",
    "triggeredBy",
]


class EventTypes(Enum):
    """Enumeration defining possible types of events."""

    CREATE = "resourceHasBeenCreated"
    UPDATE = "resourceHasBeenUpdated"
    DELETED = "resourceHasBeenDeleted"


def validate_resource_type(value: Any) -> bool:
    """Validate the resourceType property.

    Args:
        value (Any): The value to be validated.

    Returns:
        bool: True if the value is a string and equals 'customer', False otherwise.
    """

    return isinstance(value, str) and value == "customer"


def validate_resource_id(value: Any) -> bool:
    """Validate the resourceId property.

    Args:
        value (Any): The value to be validated.

    Returns:
        bool: True if the value is an integer, False otherwise.
    """

    return isinstance(value, int)


def validate_event_type(value: Any) -> bool:
    """Validate the eventType property.

    Args:
        value (Any): The value to be validated.

    Returns:
        bool: True if the value is a string and is one of the allowed event types, False otherwise.
    """

    return isinstance(value, str) and value in [
        event_type.value for event_type in EventTypes
    ]


def validate_triggered_at(value: Any) -> bool:
    """Validate the triggeredAt property.

    Args:
        value (Any): The value to be validated.

    Returns:
        bool: True if the value is a string and represents a valid datetime, False otherwise.
    """

    # datetime checking infer time if not provided
    return isinstance(value, str) and bool(datetime.fromisoformat(value))


def validate_triggered_by(value: Any) -> bool:
    """Validate the triggeredBy property.

    Args:
        value (Any): The value to be validated.

    Returns:
        bool: True if the value is a string and matches the expected format, False otherwise.
    """

    return isinstance(value, str) and bool(
        re.match("^server-[0-9]{1,100}$", value)
    )


def validate_data(raw_data: bytes) -> bool:
    """Validate the format, type, value of data.

    Args:
        raw_data (bytes): The raw data to be validated.

    Returns:
        bool: True if the data is valid, False otherwise.
    """
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
    except Exception as validation_error:
        logger.error(f"Validating data went wrong: {validation_error}")
        return False
    return True
