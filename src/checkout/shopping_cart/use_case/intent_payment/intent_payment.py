from injector import inject

from checkout.shopping_cart.domain.error.shopping_cart_not_found import ShoppingCartNotFound
from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from checkout.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository
from checkout.shopping_cart.use_case.intent_payment.intent_payment_command import IntentPaymentCommand
from shared.domain.command.command import Command
from shared.domain.command.command_listener import CommandListener


class IntentPayment(CommandListener):

    @inject
    def __init__(self, shopping_cart_repository: ShoppingCartRepository):
        self._shopping_cart_repository = shopping_cart_repository

    def is_subscribed(self, command: Command) -> bool:
        return command.name() == 'checkout.shopping_cart.use_case.intent_payment'

    def execute(self, command: IntentPaymentCommand) -> None:
        shopping_cart_id = ShoppingCartId(command.shopping_cart_id)
        shopping_cart = self._shopping_cart_repository.find_by_id(shopping_cart_id)
        if not shopping_cart:
            raise ShoppingCartNotFound(shopping_cart_id)
        shopping_cart.pay()
        self._shopping_cart_repository.save(shopping_cart)
