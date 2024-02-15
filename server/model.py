"""Module defining data class for customer event"""

from dataclasses import asdict, dataclass
from datetime import datetime
from enum import Enum


class EventTypes(Enum):
    """Enumeration defining possible types of events."""

    CREATE = "resourceHasBeenCreated"
    UPDATE = "resourceHasBeenUpdated"
    DELETED = "resourceHasBeenDeleted"


@dataclass(frozen=True)
class CustomerEvent:
    """Class representing customer event

    Attributes:
        resource_type (str): The type of the resource related to the event.
        resource_id (int): The ID of the resource related to the event.
        event_type (EventTypes): The type of the event.
        triggered_at (datetime): The time when the event was triggered.
        triggered_by (str): The entity that triggered the event.
    """

    resource_type: str
    resource_id: int
    event_type: EventTypes
    triggered_at: datetime
    triggered_by: str

    def to_dict(self):
        """Converts the CustomerEvent instance to a dictionary.

        Returns:
            dict: A dictionary representation of the CustomerEvent instance.
        """
        return {key: str(val) for key, val in asdict(self).items()}
