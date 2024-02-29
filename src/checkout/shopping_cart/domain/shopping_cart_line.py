from checkout.shopping_cart.domain.shopping_cart_line_id import ShoppingCartLineId
from checkout.shopping_cart.domain.shopping_cart_line_quantity import ShoppingCartLineQuantity
from shared.domain.entity import Entity


class ShoppingCartLine(Entity):

    def __init__(
            self,
            id: ShoppingCartLineId,
            quantity: ShoppingCartLineQuantity
    ):
        self.id = id
        self.quantity = quantity
