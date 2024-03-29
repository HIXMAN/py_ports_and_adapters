from typing import Dict

from checkout.shopping_cart.domain.shopping_cart import ShoppingCart
from checkout.shopping_cart.use_case.fetch_shopping_cart.fetch_shopping_adapter import FetchShoppingCartAdapter


class JsonFetchShoppingCartAdapter(FetchShoppingCartAdapter):
    def parse(self, shopping_cart: ShoppingCart) -> Dict:
        return {
            'id': shopping_cart.id.value(),
            'status': shopping_cart.status.name,
            'total_price': shopping_cart.total_price.value(),
            'lines': [
                {
                    'id': line.id.value(),
                    'quantity': line.quantity.value()
                } for line in shopping_cart.lines
            ]
        }
