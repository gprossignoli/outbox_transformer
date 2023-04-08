from confluent_kafka import Consumer

from kafka.consumer.kafka_consumer_configuration import KafkaConsumerConfiguration


class KafkaConsumerFactory:
    def __init__(self, consumer_group_id: str) -> None:
        self.__conf = KafkaConsumerConfiguration(
            group_id=consumer_group_id
        ).basic_configuration()

    def build(self) -> Consumer:
        return Consumer(self.__conf)
