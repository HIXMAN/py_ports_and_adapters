from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from shared.domain.domain_exception import DomainException


class ShoppingCartNotFound(DomainException):
    def __init__(self, id: ShoppingCartId):
        super().__init__(f"Shopping cart with id [{id}] not found")
