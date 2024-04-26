from checkout.shopping_cart.domain.shopping_cart_line import ShoppingCartLine
from checkout.shopping_cart.use_case.add_to_shopping_cart.add_to_shopping_cart_command import AddToShoppingCartCommand
from injector import inject

from checkout.shopping_cart.domain.error.shopping_cart_not_found import ShoppingCartNotFound
from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from checkout.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository
from checkout.shopping_cart.use_case.intent_payment.intent_payment_command import IntentPaymentCommand
from shared.domain.command.command import Command
from shared.domain.command.command_listener import CommandListener


class AddToShoppingCart(CommandListener):

    @inject
    def __init__(self, shopping_cart_repository: ShoppingCartRepository):
        self._shopping_cart_repository = shopping_cart_repository

    def is_subscribed(self, command: Command) -> bool:
        return command.name() == 'checkout.shopping_cart.use_case.add_to_shopping_cart'

    def execute(self, command: AddToShoppingCartCommand) -> None:
        shopping_cart_id = ShoppingCartId(command.shopping_cart_id)
        shopping_cart = self._shopping_cart_repository.find_by_id(shopping_cart_id)
        if not shopping_cart:
            raise ShoppingCartNotFound(shopping_cart_id)
        new_line = ShoppingCartLine(command.product_id, command.quantity)
        shopping_cart.add_line(new_line)
        self._shopping_cart_repository.save(shopping_cart)
