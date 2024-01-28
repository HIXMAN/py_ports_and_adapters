from typing import Dict

from checkout.shopping_cart.domain.shopping_cart.shopping_cart import ShoppingCart
from checkout.shopping_cart.use_case.fetch_shopping_cart.fetch_shopping_adapter import FetchShoppingCartAdapter


class JsonFetchShoppingCartAdapter(FetchShoppingCartAdapter):
    def parse(self, shopping_cart: ShoppingCart) -> Dict:
        return {
            'status': shopping_cart.status.name,
            'lines': map(lambda line: {
                'quantity': line.quantity,
                'uuid': line.uuid,
            }, shopping_cart.lines)
        }
