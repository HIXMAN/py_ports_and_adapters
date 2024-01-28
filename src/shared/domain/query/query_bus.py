from typing import Set

from shared.domain.query.query import Query
from shared.domain.query.query_listener import QueryListener
from shared.domain.query.query_response import QueryResult

from injector import inject
class Other:
    pass


class QueryBus:
    @inject
    def __init__(self, other: Other):
        self.listeners: Set[QueryListener] = set()
        self.other: other

    def add_listener(self, listener: QueryListener) -> None:
        self.listeners.add(listener)

    def remove_listener(self, listener: QueryListener) -> None:
        self.listeners.remove(listener)

    def ask(self, query: Query) -> QueryResult:
        for listener in self.listeners:
            if listener.is_subscribed(query):
                return listener.execute(query)
