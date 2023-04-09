from config import settings
from kafka import KafkaEventBusConsumer


class KafkaEventBusConsumerFactory:
    def __init__(self, consumer_group_id: str, topic_name: str):
        self.__consumer_group_id = consumer_group_id
        self.__topic_name = topic_name

    def build(self) -> KafkaEventBusConsumer:
        return KafkaEventBusConsumer(
            logger=settings.logger,
            consumer_group_id=self.__consumer_group_id,
            topic_name=self.__topic_name,
        )
