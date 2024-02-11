from typing import Optional

from injector import inject
from sqlalchemy.orm import Session

from checkout.shopping_cart.domain.shopping_cart import ShoppingCart
from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from checkout.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository
from checkout.shopping_cart.infrastructure.sqlalchemy.entity.shopping_cart import ShoppingCart as ShoppingCartModel
from checkout.shopping_cart.infrastructure.sqlalchemy.entity.shopping_cart_line import ShoppingCartLine as ShoppingCartLineModel


class AlchemyShoppingCartRepository(ShoppingCartRepository):

    @inject
    def __init__(self, session: Session) -> None:
        self._session = session

    def find_by_id(self, shopping_cart_id: ShoppingCartId) -> Optional[ShoppingCart]:
        return self._session.query(ShoppingCartModel).filter_by(id=shopping_cart_id).first()

    def save(self, shopping_cart: ShoppingCartId) -> None:
        pass