import json
from logging import Logger

from confluent_kafka import Message

from message_relay.event_bus_message import EventBusMessage
from kafka.consumer.kafka_consumer_factory import KafkaConsumerFactory
from kafka.consumer_error_exception import ConsumerErrorException


class KafkaEventBusConsumer:
    def __init__(self, logger: Logger, consumer_group_id: str, topic_name: str):
        self.__logger = logger
        self.__topic_name = topic_name
        self.__kafka_consumer = KafkaConsumerFactory(
            consumer_group_id=consumer_group_id
        ).build()
        self.__kafka_consumer.subscribe(topics=[self.__topic_name])

    def consume(self) -> EventBusMessage:
        try:
            while True:
                msg: Message = self.__kafka_consumer.poll(timeout=1.0)
                if msg is None:
                    pass
                elif msg.error():
                    raise ConsumerErrorException(reason=msg.error().str())
                else:
                    msg_value = json.loads(msg.value().decode("utf-8"))
                    event_data = msg_value["payload"]["after"]
                    return EventBusMessage(
                        event_id=event_data["event_id"],
                        event_unique_identifier=event_data["event_unique_identifier"],
                        created_at=event_data["created_at"],
                        payload=event_data["payload"],
                    )
        except Exception as e:
            self.__logger.error(e)
            self.__kafka_consumer.close()
