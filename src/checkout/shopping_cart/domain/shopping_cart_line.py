from checkout.shopping_cart.domain.product_id import ProductId
from checkout.shopping_cart.domain.shopping_cart_line_id import ShoppingCartLineId


class ShoppingCartLine:

    def __init__(
            self,
            uuid: ShoppingCartLineId,
            product_id: ProductId,
            quantity: int
    ):
        self.uuid = uuid
        self.product_id = product_id
        self.quantity = quantity
