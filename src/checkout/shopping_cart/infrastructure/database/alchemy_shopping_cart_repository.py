from typing import Optional

from sqlalchemy.orm import Session

from checkout.product.domain.shopping_cart.shopping_cart import ShoppingCart
from checkout.product.domain.shopping_cart.shopping_cart_id import ShoppingCartId
from checkout.product.domain.shopping_cart.shopping_cart_repository import ShoppingCartRepository


class AlchemyShoppingCartRepository(ShoppingCartRepository):

    def __init__(self, connection: Session):
        self._connection: Session = connection

    def find_by_id(self, shopping_cart_id: ShoppingCartId) -> Optional[ShoppingCart]:
        shopping_cart = (
            self._connection.query(ShoppingCart)
            .filter_by(id=shopping_cart_id)
            .first()
        )
        return shopping_cart

    def save(self, shopping_cart: ShoppingCartId) -> None:
        self._connection.add(shopping_cart)
