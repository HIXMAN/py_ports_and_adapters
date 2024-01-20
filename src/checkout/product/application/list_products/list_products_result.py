from typing import List

from checkout.product.application.list_products.product import Product
from shared.domain.query.query_result import QueryResult


class ListProductsResult(QueryResult):
    def __init__(self, products: List[Product]):
        self.products = products
