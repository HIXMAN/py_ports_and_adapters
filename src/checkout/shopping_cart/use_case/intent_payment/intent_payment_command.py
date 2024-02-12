from shared.domain.command.command import Command


class IntentPaymentCommand(Command):

    def __init__(self, shopping_cart_id: int):
        self.shopping_cart_id = shopping_cart_id

    def name(self) -> str:
        return 'checkout.shopping_cart.use_case.intent_payment'
