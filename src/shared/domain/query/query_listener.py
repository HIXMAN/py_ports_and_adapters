from shared.domain.query.query import Query
from shared.domain.query.query_result import QueryResult


class QueryListener:

    def is_subscribed(self, query: Query) -> bool:
        pass

    def execute(self, query: Query) -> QueryResult:
        pass
