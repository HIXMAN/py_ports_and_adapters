from shared.domain.command.command import Command


class IntentPaymentCommand(Command):
    def name(self) -> str:
        return 'checkout.shopping_cart.use_case.intent_payment'
