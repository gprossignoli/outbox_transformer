from confluent_kafka import Producer

from kafka.producer.kafka_producer_configuration import KafkaProducerConfiguration


class KafkaProducerFactory:
    def __init__(self) -> None:
        self.__producer_conf = KafkaProducerConfiguration().exactly_once_configuration()

    def build(self) -> Producer:
        return Producer(self.__producer_conf)
