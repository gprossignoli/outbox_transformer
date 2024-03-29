from flask import Flask
from flask.cli import AppGroup

from config.settings import logger, db
from kafka.producer.kafka_event_bus_producer_factory import KafkaEventBusProducerFactory
from message_relay.message_relay import MessageRelay
from message_relay.sqlalchemy_transactional_outbox_repository_with_autocommit import \
    SqlalchemyTransactionalOutboxRepositoryWithAutocommit

cli_commands = AppGroup(name="cli")


@cli_commands.command("message-relay-worker")
def message_relay_worker() -> None:
    logger.info("Starting message relay worker")
    while True:
        try:
            msg_relay = MessageRelay(
                logger=logger,
                outbox_repository=SqlalchemyTransactionalOutboxRepositoryWithAutocommit(db.session),
                event_bus_producer=KafkaEventBusProducerFactory().build(),
            )
            msg_relay.start()
        except Exception as e:
            logger.exception(f"MessageRelay suffered an error: {e}")
            logger.info("Resetting the execution of the MessageRelay")


def register_commands(app: Flask) -> None:
    app.cli.add_command(cli_commands)
