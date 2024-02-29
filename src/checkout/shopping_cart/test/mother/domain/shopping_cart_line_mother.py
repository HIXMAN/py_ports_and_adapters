from checkout.shopping_cart.domain.shopping_cart_line import ShoppingCartLine
from checkout.shopping_cart.domain.shopping_cart_line_id import ShoppingCartLineId
from checkout.shopping_cart.domain.shopping_cart_line_quantity import ShoppingCartLineQuantity


class ShoppingCartLineMother:

    @staticmethod
    def create(
        id: int = 1,
        quantity: int = 10,
    ) -> ShoppingCartLine:
        return ShoppingCartLine(
            id=ShoppingCartLineId(id),
            quantity=ShoppingCartLineQuantity(quantity)
        )
