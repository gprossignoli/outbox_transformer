from dataclasses import dataclass


@dataclass(frozen=True)
class EventBusMessage:
    event_id: str
    event_unique_identifier: str
    created_at: str
    payload: dict
