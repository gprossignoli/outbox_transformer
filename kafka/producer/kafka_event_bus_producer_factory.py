from config import settings
from kafka import KafkaEventBusProducer


class KafkaEventBusProducerFactory:
	def build(self) -> KafkaEventBusProducer:
		return KafkaEventBusProducer(logger=settings.logger)
