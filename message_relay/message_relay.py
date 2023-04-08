from logging import Logger

from kafka import KafkaEventBusConsumer, KafkaEventBusProducer


class MessageRelay:
    def __init__(
        self,
        logger: Logger,
        kafka_event_bus_consumer: KafkaEventBusConsumer,
        kafka_event_bus_producer: KafkaEventBusProducer,
    ):
        self.__logger = logger

        self.__kafka_event_bus_consumer = kafka_event_bus_consumer
        self.__kafka_event_bus_producer = kafka_event_bus_producer

    def start(self) -> None:
        while True:
            event = self.__kafka_event_bus_consumer.consume()
            self.__kafka_event_bus_producer.publish(event)
