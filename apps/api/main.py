from fastapi import FastAPI
from injector import Module, Injector
from sqlalchemy.orm import Session

from checkout.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository
from checkout.shopping_cart.infrastructure.sqlalchemy.alchemy_shopping_cart_repository import \
    AlchemyShoppingCartRepository
from checkout.shopping_cart.use_case.intent_payment.intent_payment import IntentPayment
from checkout.shopping_cart.use_case.intent_payment.intent_payment_command import IntentPaymentCommand
from database.bootstrap import database_bootstrap
from shared.domain.command.command_bus import CommandBus

app = FastAPI()


class RepositoryModule(Module):
    def configure(self, binder):
        binder.bind(ShoppingCartRepository, to=AlchemyShoppingCartRepository)


class AlchemyModule(Module):
    def configure(self, binder):
        session = database_bootstrap()
        binder.bind(Session, to=session)


@app.get("/")
def read_root():
    container = Injector([AlchemyModule(), RepositoryModule()])
    command_bus: CommandBus = container.get(CommandBus)
    intent_payment: IntentPayment = container.get(IntentPayment)
    command_bus.add_listener(intent_payment)
    command_bus.publish(IntentPaymentCommand())
    return {"ok"}

