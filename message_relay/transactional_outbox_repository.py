from abc import ABC, abstractmethod
from typing import Iterable

from message_relay.outbox_record import OutboxRecord


class TransactionalOutboxRepository(ABC):
    @abstractmethod
    def save(self, record: OutboxRecord) -> None:
        pass

    @abstractmethod
    def find(self, batch_size: int = 100) -> Iterable[OutboxRecord]:
        pass
