from kafka.consumer.kafka_event_bus_consumer_factory import KafkaEventBusConsumerFactory
from kafka.producer.kafka_event_bus_producer_factory import KafkaEventBusProducerFactory
from message_relay.message_relay import MessageRelay
from settings import logger, OUTBOX_CDC_TOPIC

if __name__ == "__main__":
    msg_relay = MessageRelay(
        logger=logger,
        kafka_event_bus_consumer=KafkaEventBusConsumerFactory(
            consumer_group_id="outbox_transformer", topic_name=OUTBOX_CDC_TOPIC
        ).build(),
        kafka_event_bus_producer=KafkaEventBusProducerFactory().build(),
    )
    msg_relay.start()
