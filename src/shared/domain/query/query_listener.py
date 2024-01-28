from typing import Dict

from shared.domain.query.query import Query


class QueryListener:

    def is_subscribed(self, query: Query) -> bool:
        raise NotImplementedError

    def execute(self, query: Query) -> Dict:
        raise NotImplementedError
