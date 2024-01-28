from checkout.shopping_cart.use_case.intent_payment.intent_payment_command import IntentPaymentCommand
from shared.domain.command.command import Command
from shared.domain.command.command_listener import CommandListener


class IntentPayment(CommandListener):

    def is_subscribed(self, command: Command) -> bool:
        return command.name() == 'checkout.shopping_cart.use_case.intent_payment'

    def execute(self, command: IntentPaymentCommand) -> None:
        print(command.name())
