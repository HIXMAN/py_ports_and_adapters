from typing import List, Optional

from checkout.product.domain.product_id import ProductId
from checkout.shopping_cart.domain.error.shopping_cart_invalid_status import ShoppingCartInvalidStatus
from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from checkout.shopping_cart.domain.shopping_cart_line import ShoppingCartLine
from checkout.shopping_cart.domain.shopping_cart_status import ShoppingCartStatus
from checkout.shopping_cart.domain.shopping_total_price import ShoppingCartTotalPrice


class ShoppingCart:

    def __init__(
            self,
            uuid: ShoppingCartId,
            status: ShoppingCartStatus,
            lines: List[ShoppingCartLine],
            total_price: Optional[ShoppingCartTotalPrice],
    ):
        self.uuid = uuid
        self.status = status
        self.lines = lines
        self.total_price = total_price

    def complete_payment(self, total_price) -> None:
        self._validate_shopping_cart_to_be_completed()
        self._set_completed_status()
        self._set_total_price(total_price)

    def _validate_shopping_cart_to_be_completed(self) -> None:
        if self.status is not ShoppingCartStatus.IN_PROGRESS:
            raise ShoppingCartInvalidStatus(self.uuid, self.status)

    def _set_completed_status(self) -> None:
        self.status = ShoppingCartStatus.COMPLETED

    def _set_total_price(self, total_price: int) -> None:
        self.total_price = ShoppingCartTotalPrice(total_price)

    def product_ids(self) -> List[ProductId]:
        return [product.product_id for product in self.lines]
