from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from shared.domain.domain_exception import DomainException


class ShoppingCartNotFound(DomainException):
    status_code = 400
    detail = 'shopping cart'
    def __init__(self, id: ShoppingCartId):
        super().__init__(f"Shopping cart with id [{id}] not found")
