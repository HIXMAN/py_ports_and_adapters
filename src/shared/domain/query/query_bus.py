from typing import Set

from shared.domain.query.query import Query
from shared.domain.query.query_listener import QueryListener
from shared.domain.query.query_result import QueryResult


class QueryBus:
    def __init__(self):
        self.listeners: Set[QueryListener] = set()

    def add_listener(self, listener: QueryListener) -> None:
        self.listeners.add(listener)

    def remove_listener(self, listener: QueryListener) -> None:
        self.listeners.remove(listener)

    def ask(self, query: Query) -> QueryResult:
        for listener in self.listeners:
            if listener.is_subscribed(query):
                return listener.execute(query)
