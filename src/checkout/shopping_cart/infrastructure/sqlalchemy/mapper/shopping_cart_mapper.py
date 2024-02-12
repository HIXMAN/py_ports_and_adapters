from pip._vendor.rich.pretty import pprint

from checkout.shopping_cart.domain.shopping_cart import ShoppingCart
from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from checkout.shopping_cart.domain.shopping_cart_line import ShoppingCartLine
from checkout.shopping_cart.domain.shopping_cart_line_id import ShoppingCartLineId
from checkout.shopping_cart.domain.shopping_cart_line_quantity import ShoppingCartLineQuantity
from checkout.shopping_cart.domain.shopping_cart_status import ShoppingCartStatus
from checkout.shopping_cart.domain.shopping_cart_total_price import ShoppingCartTotalPrice
from checkout.shopping_cart.infrastructure.sqlalchemy.entity.shopping_cart_line_model import ShoppingCartLineModel
from checkout.shopping_cart.infrastructure.sqlalchemy.entity.shopping_cart_model import ShoppingCartModel


class ShoppingCartMapper:

    @staticmethod
    def to_domain(shopping_cart_model: ShoppingCartModel) -> ShoppingCart:
        return ShoppingCart(
            ShoppingCartId(shopping_cart_model.id),
            ShoppingCartStatus(shopping_cart_model.status),
            ShoppingCartTotalPrice(shopping_cart_model.total_price),
            [ShoppingCartLine(
                ShoppingCartLineId(shopping_cart_line_model.id),
                ShoppingCartLineQuantity(shopping_cart_line_model.quantity)
            ) for shopping_cart_line_model in shopping_cart_model.lines]
        )

    @staticmethod
    def to_model(shopping_cart: ShoppingCart) -> ShoppingCartModel:

        lines = [ShoppingCartLineModel(
            id=line.id.value(),
            quantity=line.quantity,
            cart_id=shopping_cart.id.value()
        ) for line in shopping_cart.lines]

        shopping_cart_model = ShoppingCartModel(
            id=shopping_cart.id.value(),
            status=shopping_cart.status.value,
            total_price=shopping_cart.total_price,
            lines=lines
        )

        return shopping_cart_model
