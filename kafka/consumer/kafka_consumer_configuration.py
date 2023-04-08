from typing import Dict

from kafka.kafka_client_configuration import KafkaClientConfiguration


class KafkaConsumerConfiguration(KafkaClientConfiguration):
    def __init__(self, group_id: str):
        super().__init__()
        self.__group_id = group_id

    def basic_configuration(self) -> Dict:
        extended_config = super().base_configuration()
        extended_config["group.id"] = self.__group_id
        # 'auto.offset.reset=earliest' to start reading from the beginning of
        # the topic if no committed offsets exist.
        extended_config["auto.offset.reset"] = "earliest"
        return extended_config
