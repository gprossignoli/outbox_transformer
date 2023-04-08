class ConsumerErrorException(Exception):
    def __init__(self, reason: str):
        self.__reason = reason
        super().__init__(self.__reason)
