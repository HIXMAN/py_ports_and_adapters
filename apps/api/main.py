from fastapi import FastAPI
from injector import Module, Injector
from sqlalchemy.orm import sessionmaker, Session

from checkout.shopping_cart.application.complete_payment.complete_payment import CompletePayment
from checkout.shopping_cart.application.complete_payment.complete_payment_command import CompletePaymentCommand
from checkout.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository
from checkout.shopping_cart.infrastructure.sqlalchemy.alchemy_shopping_cart_repository import \
    AlchemyShoppingCartRepository
from checkout.shopping_cart.infrastructure.sqlalchemy.base import Base
from checkout.shopping_cart.infrastructure.sqlalchemy.engine import engine
from shared.domain.command.command_bus import CommandBus

app = FastAPI()


class RepositoryModule(Module):
    def configure(self, binder):
        binder.bind(ShoppingCartRepository, to=AlchemyShoppingCartRepository)


class AlchemyModule(Module):
    def configure(self, binder):
        Base.metadata.create_all(engine)
        create_session = sessionmaker(bind=engine)
        session = create_session()
        binder.bind(Session, to=session)


@app.get("/")
def read_root():
    container = Injector([RepositoryModule(), AlchemyModule()])
    command_bus: CommandBus = container.get(CommandBus)
    complete_payment: CompletePayment = container.get(CompletePayment)
    command_bus.add_listener(complete_payment)
    command_bus.publish(CompletePaymentCommand('2'))

    return {"ok"}


