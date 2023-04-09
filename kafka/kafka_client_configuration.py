from typing import List

from config.settings import KAFKA_SERVERS, KAFKA_CLIENT_ID


class KafkaClientConfiguration:
    def __init__(self):
        self.__bootstrap_servers: List[str] = KAFKA_SERVERS
        self.__client_id: str = KAFKA_CLIENT_ID
        self._base_configuration = {}

    def base_configuration(self) -> dict:
        self._base_configuration = {
            "bootstrap.servers": self.__bootstrap_servers,
            "client.id": self.__client_id,

        }

        return self._base_configuration

    def base_producer_configuration(self) -> dict:
        base_producer_config = self.base_configuration()
        base_producer_config["delivery.timeout.ms"] = 20000

        return base_producer_config
