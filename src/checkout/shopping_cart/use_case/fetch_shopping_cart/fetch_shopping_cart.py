from typing import Dict

from injector import inject

from checkout.shopping_cart.domain.shopping_cart.error.shopping_cart_not_found import ShoppingCartNotFound
from checkout.shopping_cart.domain.shopping_cart.shopping_cart_id import ShoppingCartId
from checkout.shopping_cart.domain.shopping_cart.shopping_cart_repository import ShoppingCartRepository
from checkout.shopping_cart.use_case.fetch_shopping_cart.fetch_shopping_cart_query import FetchShoppingCartQuery
from checkout.shopping_cart.use_case.fetch_shopping_cart.fetch_shopping_adapter import FetchShoppingCartResponse, \
    FetchShoppingCartAdapter
from shared.domain.query.query import Query
from shared.domain.query.query_listener import QueryListener
from shared.domain.query.query_response import QueryResponse


class FetchShoppingCart(QueryListener):

    @inject
    def __init__(
            self,
            shopping_cart_repository: ShoppingCartRepository,
            fetch_shopping_cart_adapter: FetchShoppingCartAdapter
    ) -> None:
        self._shopping_cart_repository = shopping_cart_repository
        self._shopping_cart_adapter = fetch_shopping_cart_adapter

    def is_subscribed(self, query: Query) -> bool:
        return query.name() == 'checkout.shopping_cart.use_case.fetch_shopping_cart'

    def execute(self, query: FetchShoppingCartQuery) -> Dict:
        shopping_cart_id = ShoppingCartId(query.shopping_cart_id)
        shopping_cart = self._shopping_cart_repository.find_by_id(shopping_cart_id)

        print(shopping_cart)

        if shopping_cart is None:
            raise ShoppingCartNotFound(shopping_cart_id)

        return self._shopping_cart_adapter.parse(shopping_cart)
