from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from checkout.shopping_cart.domain.shopping_cart_line_id import ShoppingCartLineId
from shared.domain.domain_exception import DomainException


class ShoppingCartLineInvalidLineQuantity(DomainException):
    def __init__(self, cart_id: ShoppingCartId, line_id: ShoppingCartLineId):
        cart = str(cart_id.value())
        line = str(line_id)
        self.detail = f"Shopping cart with id [{cart}] has too many items in the line [{line}]"
        self.status_code = 400
        super().__init__(self.detail)
