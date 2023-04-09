from datetime import datetime
from logging import Logger

from kafka import KafkaEventBusProducer
from message_relay.outbox_record import OutboxRecord
from message_relay.outbox_record_to_event_bus_message_translator import OutboxRecordToEventBusMessageTranslator
from message_relay.transactional_outbox_repository import TransactionalOutboxRepository


class MessageRelay:
    def __init__(
        self,
        logger: Logger,
        outbox_repository: TransactionalOutboxRepository,
        event_bus_producer: KafkaEventBusProducer,
    ):
        self.__logger = logger
        self.__outbox_repository = outbox_repository
        self.__outbox_record_to_event_bus_message_translator = OutboxRecordToEventBusMessageTranslator()
        self.__event_bus_producer = event_bus_producer

    def start(self) -> None:
        for record in self.__outbox_repository.find():
            event = self.__outbox_record_to_event_bus_message_translator.translate(record)
            try:
                self.__event_bus_producer.publish(event)
            except Exception as e:
                self.__mark_delivery_error(record)
            else:
                self.__mark_successful_delivery(record)

            try:
                self.__outbox_repository.save(record)
            except Exception as e:
                self.__logger.error(f"ERROR - record with id: {record.id} couldn't be updated.")
                self.__logger.exception(f"ERROR - {e}")

    def __mark_delivery_error(self, record: OutboxRecord) -> None:
        record.delivery_errors += 1

        if record.delivery_errors >= 5:
            record.delivery_paused_at = datetime.now()

    def __mark_successful_delivery(self, record: OutboxRecord) -> None:
        record.delivered_at = datetime.now()
