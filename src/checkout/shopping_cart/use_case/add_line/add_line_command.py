from shared.domain.command.command import Command


class AddLineCommand(Command):

    def __init__(self, shopping_cart_id: int, line_id: int, quantity: int):
        self.shopping_cart_id = shopping_cart_id
        self.line_id = line_id
        self.quantity = quantity

    def name(self) -> str:
        return 'checkout.shopping_cart.use_case.add_line'
