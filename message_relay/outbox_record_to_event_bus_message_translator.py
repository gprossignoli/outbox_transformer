from message_relay.event_bus_message import EventBusMessage
from message_relay.outbox_record import OutboxRecord


class OutboxRecordToEventBusMessageTranslator:
    def translate(self, record: OutboxRecord) -> EventBusMessage:
        return EventBusMessage(
            event_id=record.event_id,
            event_unique_identifier=record.event_unique_identifier,
            created_at=record.created_at,
            payload=record.payload,
        )
