from injector import inject

from checkout.shopping_cart.domain.error.shopping_cart_not_found import ShoppingCartNotFound
from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from checkout.shopping_cart.domain.shopping_cart_line_id import ShoppingCartLineId
from checkout.shopping_cart.domain.shopping_cart_line_quantity import ShoppingCartLineQuantity
from checkout.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository
from checkout.shopping_cart.use_case.add_line.add_line_command import AddLineCommand
from shared.domain.command.command import Command
from shared.domain.command.command_listener import CommandListener


class AddLine(CommandListener):

    @inject
    def __init__(self, shopping_cart_repository: ShoppingCartRepository):
        self._shopping_cart_repository = shopping_cart_repository

    def is_subscribed(self, command: Command) -> bool:
        return command.name() == 'checkout.shopping_cart.use_case.add_line'

    def execute(self, command: AddLineCommand) -> None:
        shopping_cart_id = ShoppingCartId(command.shopping_cart_id)
        quantity = ShoppingCartLineQuantity(command.quantity)
        line_id = ShoppingCartLineId(command.line_id)

        shopping_cart = self._shopping_cart_repository.find_by_id(shopping_cart_id)
        if not shopping_cart:
            raise ShoppingCartNotFound(shopping_cart_id)
        shopping_cart.add_line(line_id, quantity)
        self._shopping_cart_repository.save(shopping_cart)
