from checkout.shopping_cart.domain.shopping_cart.shopping_cart_id import ShoppingCartId
from checkout.shopping_cart.domain.shopping_cart.shopping_cart_status import ShoppingCartStatus
from shared.domain.domain_exception import DomainException


class ShoppingCartInvalidStatus(DomainException):
    def __init__(self, uuid: ShoppingCartId, status: ShoppingCartStatus) -> None:
        super().__init__(f"Shopping cart with id [{uuid}] has invalid status: {status}")

