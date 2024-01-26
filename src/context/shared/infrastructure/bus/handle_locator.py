from typing import Callable, Dict


class HandleLocator:
    def __init__(self):
        self._handlers: Dict[str, Callable] = {}

    # TODO: implement typing
    def add(self, key: str, handler: Callable):
        self._handlers[key] = handler

    def find(self, key: str) -> Callable:
        return self._handlers[key]
