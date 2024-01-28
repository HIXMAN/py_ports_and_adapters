from typing import List

from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from checkout.shopping_cart.domain.shopping_cart_line import ShoppingCartLine
from checkout.shopping_cart.domain.shopping_cart_status import ShoppingCartStatus


class ShoppingCart:

    def __init__(
            self,
            uuid: ShoppingCartId,
            status: ShoppingCartStatus,
            lines: List[ShoppingCartLine],
    ):
        self.uuid = uuid
        self.status = status
        self.lines = lines
