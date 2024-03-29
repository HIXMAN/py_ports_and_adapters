from typing import Dict

from checkout.shopping_cart.domain.shopping_cart import ShoppingCart
from checkout.shopping_cart.use_case.fetch_shopping_cart.fetch_shopping_adapter import FetchShoppingCartAdapter


class OpenApiFetchShoppingCartAdapter(FetchShoppingCartAdapter):
    def parse(self, shopping_cart: ShoppingCart) -> Dict:
        return {
            "data": {
                'id': shopping_cart.id.value(),
                'status': shopping_cart.status.name,
                'lines': [line.id.value() for line in shopping_cart.lines]
            },
            "relationships": {
                "lines": [{
                    "id": line.id.value(),
                    "quantity": line.quantity.value()
                } for line in shopping_cart.lines]
            }
        }
