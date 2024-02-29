from typing import List
from checkout.shopping_cart.domain.shopping_cart import ShoppingCart
from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from checkout.shopping_cart.domain.shopping_cart_line import ShoppingCartLine
from checkout.shopping_cart.domain.shopping_cart_status import ShoppingCartStatus
from checkout.shopping_cart.domain.shopping_cart_total_price import ShoppingCartTotalPrice
from checkout.shopping_cart.test.mother.domain.shopping_cart_line_mother import ShoppingCartLineMother


class ShoppingCartMother:

    @staticmethod
    def create(
        id: int = 1,
        status: ShoppingCartStatus = ShoppingCartStatus.CREATED,
        total_price: float = 10.10,
        lines: List[ShoppingCartLine] = [
            ShoppingCartLineMother.create(id=1, quantity=10),
            ShoppingCartLineMother.create(id=2, quantity=20),
        ]
    ) -> ShoppingCart:
        return ShoppingCart(
            id=ShoppingCartId(id),
            status=status,
            total_price=ShoppingCartTotalPrice(total_price),
            lines=lines
        )