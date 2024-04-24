from checkout.shopping_cart.domain.shopping_cart_line import ShoppingCartLine
from injector import inject
from typing import Dict

from checkout.shopping_cart.domain.error.shopping_cart_not_found import ShoppingCartNotFound
from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from checkout.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository
from checkout.shopping_cart.test.mother.domain.shopping_cart_mother import ShoppingCartMother
from checkout.shopping_cart.use_case.fetch_shopping_cart.fetch_shopping_adapter import FetchShoppingCartAdapter
from checkout.shopping_cart.use_case.fetch_shopping_cart.fetch_shopping_cart_query import FetchShoppingCartQuery
from shared.domain.query.query_listener import QueryListener


class AddLineToShoppingCart(QueryListener):

    @inject
    def __init__(
            self,
            shopping_cart_repository: ShoppingCartRepository,
    ) -> None:
        self.shopping_cart_repository = shopping_cart_repository

    def execute(self, shopping_cart_id: ShoppingCartId, line: ShoppingCartLine)-> None:
        shopping_cart = self.shopping_cart_repository.find_by_id(shopping_cart_id)
        shopping_cart.add_line(line)
        self.shopping_cart_repository.save(shopping_cart)

