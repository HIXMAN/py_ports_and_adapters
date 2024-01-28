from typing import Optional

from checkout.shopping_cart.domain.shopping_cart import ShoppingCart
from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId


class ShoppingCartRepository:
    def find_by_id(self, shopping_cart_id: ShoppingCartId) -> Optional[ShoppingCart]:
        raise NotImplementedError

    def save(self, shopping_cart: ShoppingCartId) -> None:
        raise NotImplementedError
