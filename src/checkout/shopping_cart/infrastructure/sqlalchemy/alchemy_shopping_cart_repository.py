from typing import Optional

from injector import inject
from sqlalchemy.orm import Session

from checkout.shopping_cart.domain.shopping_cart import ShoppingCart
from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from checkout.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository
from checkout.shopping_cart.infrastructure.sqlalchemy.entity.shopping_cart_model import ShoppingCartModel
from checkout.shopping_cart.infrastructure.sqlalchemy.mapper.shopping_cart_mapper import ShoppingCartMapper


class AlchemyShoppingCartRepository(ShoppingCartRepository):

    @inject
    def __init__(self, session: Session) -> None:
        self._session = session

    def find_by_id(self, shopping_cart_id: ShoppingCartId) -> Optional[ShoppingCart]:
        shopping_cart_model: Optional[ShoppingCartModel] = (
            self._session
                .query(ShoppingCartModel)
                .filter_by(id=shopping_cart_id.value())
                .first()
        )
        if shopping_cart_model:
            return ShoppingCartMapper.to_domain(shopping_cart_model)
        return None

    def save(self, shopping_cart: ShoppingCart) -> None:
        shopping_cart_model = ShoppingCartMapper.to_model(shopping_cart)

        self._session.merge(shopping_cart_model)
        self._session.commit()
