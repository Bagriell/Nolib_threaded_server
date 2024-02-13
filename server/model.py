from dataclasses import dataclass
from datetime import datetime


class Event_types(Enum):
    CREATE = "resourceHasBeenCreated"
    UPDATE = "resourceHasBeenUpdated"
    DELETED = "resourceHasBeenDeleted"


@dataclass(frozen=True)
class Customer_event:
    """Class representing customer event"""

    resource_type: str
    resource_id: int
    event_type: Event_types
    triggered_at: datetime
    triggered_by: str
