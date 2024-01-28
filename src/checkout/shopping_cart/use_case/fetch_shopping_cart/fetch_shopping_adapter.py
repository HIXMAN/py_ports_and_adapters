from typing import Dict

from checkout.shopping_cart.domain.shopping_cart.shopping_cart import ShoppingCart


class FetchShoppingCartAdapter:

    def parse(self, shopping_cart: ShoppingCart) -> Dict:
        raise NotImplementedError
    