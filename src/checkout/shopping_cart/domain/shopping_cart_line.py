from checkout.shopping_cart.domain.shopping_cart_line_id import ShoppingCartLineId
from checkout.shopping_cart.domain.shopping_cart_line_quantity import ShoppingCartLineQuantity
from shared.domain.entity import Entity

PRODUCT_MAX_QUANTITY = 5

class ShoppingCartLine(Entity):
    def __init__(
            self,
            id: ShoppingCartLineId,
            quantity: ShoppingCartLineQuantity
    ):
        self.id = id
        self.quantity = quantity

    def is_quantity_valid(self) -> bool:
        return self.quantity <= PRODUCT_MAX_QUANTITY