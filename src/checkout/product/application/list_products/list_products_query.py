from typing import List

from shared.domain.query.query import Query


class ListProductsQuery(Query):
    def __init__(self, product_ids: List[str]):
        self.product_ids = product_ids
