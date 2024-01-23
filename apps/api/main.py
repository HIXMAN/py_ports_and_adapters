import injector
from fastapi import FastAPI

from checkout.shopping_cart.application.complete_payment.complete_payment import CompletePayment
from checkout.shopping_cart.application.complete_payment.complete_payment_command import CompletePaymentCommand
from checkout.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository
from checkout.shopping_cart.infrastructure.database.alchemy_shopping_cart_repository import \
    AlchemyShoppingCartRepository
from shared.domain.command.command_bus import CommandBus

app = FastAPI()

import injector


class RepositoryModule(injector.Module):
    def configure(self, binder):
        binder.bind(ShoppingCartRepository, to=AlchemyShoppingCartRepository)


@app.get("/")
def read_root():

    container = injector.Injector([RepositoryModule()])
    command_bus: CommandBus = container.get(CommandBus)
    complete_payment: CompletePayment = container.get(CompletePayment)
    command_bus.add_listener(complete_payment)
    command_bus.publish(CompletePaymentCommand('2'))
    return {"ok"}

