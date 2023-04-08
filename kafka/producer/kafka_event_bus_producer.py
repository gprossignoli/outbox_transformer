import json
from logging import Logger

from message_relay.event_bus_message import EventBusMessage
from kafka.kafka_topics_manager import KafkaTopicsManager
from kafka.producer.kafka_producer_factory import KafkaProducerFactory
from message_relay.register_delivery_data import register_delivery_data
from message_relay.register_publication_data import register_publication_data


class KafkaEventBusProducer:
    def __init__(self, logger: Logger):
        self.__logger = logger
        self.__topics_manager = KafkaTopicsManager()
        self.__topic_created = False
        self.__kafka_producer = KafkaProducerFactory().build()

    def publish(self, message: EventBusMessage) -> None:

        if self.__topic_created is False:
            try:
                self.__create_topic(message.event_unique_identifier)
                self.__topic_created = True
                self.__topics_manager = None
            except Exception as e:
                self.__logger.error(f"Error creating the topic {message.event_unique_identifier}")
                raise e

        try:
            self.__publish_event(message=message, payload=json.dumps(message.payload))
        except Exception as e:
            raise e

    def __create_topic(
            self, event_identifier: str, partitions: int = 3, replication_factor: int = 3
    ) -> None:
        self.__topics_manager.create_topic(
            topic_name=event_identifier,
            num_partitions=partitions,
            replication_factor=replication_factor,
            config={"min.insync.replicas": 2},
        )

    @register_publication_data
    def __publish_event(self, message: EventBusMessage, payload: str):
        self.__kafka_producer.produce(
            topic=message.event_unique_identifier,
            value=payload,
            key=message.event_id,
            on_delivery=self.__on_delivery,
        )
        self.__kafka_producer.flush(timeout=30)

    @register_delivery_data
    def __on_delivery(self, err, msg) -> None:
        if err:
            self.__logger.info(
                f"ERROR: Message {msg.value().decode('utf-8')} failed delivery: {err}"
            )
        else:
            self.__logger.info(
                f"Event to topic {msg.topic()}: key = {msg.key().decode('utf-8')}"
            )
