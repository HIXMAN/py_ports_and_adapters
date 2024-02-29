from checkout.shopping_cart.use_case.intent_payment.intent_payment_command import IntentPaymentCommand


class IntentPaymentCommandMother:
    @staticmethod
    def create(
        id: int = 1,
    ) -> IntentPaymentCommand:
        return IntentPaymentCommand(id)