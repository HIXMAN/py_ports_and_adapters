from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from shared.domain.domain_exception import DomainException


class ShoppingCartNotFound(DomainException):
    def __init__(self, uuid: ShoppingCartId):
        super().__init__(f"Shopping cart with id [{uuid}] not found")
