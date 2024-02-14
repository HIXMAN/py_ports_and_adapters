from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from shared.domain.domain_exception import DomainException


class ShoppingCartNotFound(DomainException):
    def __init__(self, id: ShoppingCartId):
        uuid = str(id.value())
        self.detail = f"Shopping cart with id [{uuid}] not found"
        self.status_code = 400
        super().__init__(self.detail)
