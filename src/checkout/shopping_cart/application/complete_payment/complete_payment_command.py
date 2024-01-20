from shared.domain.command.command import Command


class CompletePaymentCommand(Command):
    def __init__(self, shopping_cart_id: str):
        self.shopping_cart_id = shopping_cart_id
