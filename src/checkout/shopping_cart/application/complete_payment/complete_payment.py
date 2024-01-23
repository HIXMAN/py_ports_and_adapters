from injector import inject

from checkout.product.application.list_products.list_products_query import ListProductsQuery
from checkout.product.application.list_products.list_products_result import ListProductsResult
from checkout.shopping_cart.application.complete_payment.complete_payment_command import CompletePaymentCommand
from checkout.shopping_cart.domain.shopping_cart import ShoppingCart
from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from checkout.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository
from shared.domain.command.command import Command
from shared.domain.command.command_listener import CommandListener
from shared.domain.event.event_bus import EventBus
from shared.domain.query.query_bus import QueryBus


class CompletePayment(CommandListener):
    @inject
    def __init__(
            self,
            shopping_cart_repository: ShoppingCartRepository,
            event_bus: EventBus,
            query_bus: QueryBus,
    ) -> None:
        self._shopping_cart_repository = shopping_cart_repository
        self._event_bus = event_bus
        self._query_bus = query_bus

    def is_subscribed(self, command: Command) -> bool:
        return isinstance(command, CompletePaymentCommand)

    def execute(self, complete_payment_command: CompletePaymentCommand) -> None:
        shopping_cart_id = ShoppingCartId(complete_payment_command.shopping_cart_id)
        self._shopping_cart_repository.save(ShoppingCartId('1'))
        # shopping_cart = self._shopping_cart_repository.find_by_id(shopping_cart_id)
        # total_price = self._calculate_price(shopping_cart)
        # shopping_cart.complete_payment(total_price)
        # self._shopping_cart_repository.save(shopping_cart)
        # self._event_bus.publish(ShoppingCartWasCompleted())

    def _calculate_price(self, shopping_cart: ShoppingCart) -> int:
        # noinspection PyTypeChecker
        list_products_result: ListProductsResult = self._query_bus.ask(ListProductsQuery(shopping_cart.product_ids()))
        total_price = 0
        for product in list_products_result.products:
            total_price += product.price
        return total_price
