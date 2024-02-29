from typing import List

from checkout.shopping_cart.domain.error.shopping_cart_invalid_status import ShoppingCartInvalidStatus
from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from checkout.shopping_cart.domain.shopping_cart_line import ShoppingCartLine
from checkout.shopping_cart.domain.shopping_cart_status import ShoppingCartStatus
from checkout.shopping_cart.domain.shopping_cart_total_price import ShoppingCartTotalPrice


class ShoppingCart:

    def __init__(
            self,
            id: ShoppingCartId,
            status: ShoppingCartStatus,
            total_price: ShoppingCartTotalPrice,
            lines: List[ShoppingCartLine],
    ):
        self.id = id
        self.status = status
        self.total_price = total_price
        self.lines = lines

    def __eq__(self, other):
        return self.id.value() == other.id.value()

    def pay(self):
        if self.status != ShoppingCartStatus.IN_PROGRESS:
            raise ShoppingCartInvalidStatus(self.id, self.status)
        self.status = ShoppingCartStatus.COMPLETED
        
