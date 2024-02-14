from fastapi import FastAPI, Query
from injector import Module, Injector
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from checkout.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository
from checkout.shopping_cart.infrastructure.interface_adapter.json_fetch_shopping_cart_adapter import \
    JsonFetchShoppingCartAdapter
from checkout.shopping_cart.infrastructure.sqlalchemy.alchemy_shopping_cart_repository import \
    AlchemyShoppingCartRepository
from checkout.shopping_cart.use_case.add_line.add_line import AddLine
from checkout.shopping_cart.use_case.add_line.add_line_command import AddLineCommand
from checkout.shopping_cart.use_case.fetch_shopping_cart.fetch_shopping_adapter import FetchShoppingCartAdapter
from checkout.shopping_cart.use_case.fetch_shopping_cart.fetch_shopping_cart import FetchShoppingCart
from checkout.shopping_cart.use_case.fetch_shopping_cart.fetch_shopping_cart_query import FetchShoppingCartQuery
from checkout.shopping_cart.use_case.intent_payment.intent_payment import IntentPayment
from checkout.shopping_cart.use_case.intent_payment.intent_payment_command import IntentPaymentCommand
from database.bootstrap import database_bootstrap
from shared.domain.command.command_bus import CommandBus
from shared.domain.domain_exception import DomainException
from shared.domain.query.query_bus import QueryBus

app = FastAPI()


class RepositoryModule(Module):
    def configure(self, binder):
        binder.bind(ShoppingCartRepository, to=AlchemyShoppingCartRepository)


class AdaptersModule(Module):
    def configure(self, binder):
        binder.bind(FetchShoppingCartAdapter, to=JsonFetchShoppingCartAdapter)


class AlchemyModule(Module):
    def configure(self, binder):
        session = database_bootstrap()
        binder.bind(Session, to=session)


container = Injector([AlchemyModule(), RepositoryModule(), AdaptersModule()])

command_bus: CommandBus = container.get(CommandBus)
intent_payment: IntentPayment = container.get(IntentPayment)
add_line: AddLine = container.get(AddLine)
command_bus.add_listener(add_line)

query_bus: QueryBus = container.get(QueryBus)
fetch_shopping_cart: FetchShoppingCart = container.get(FetchShoppingCart)
query_bus.add_listener(fetch_shopping_cart)


@app.exception_handler(DomainException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={'message': exc.detail})


@app.get("/intent-payment/")
def intent_payment(id: str = Query(..., description="")):
    intent_payment_command = IntentPaymentCommand(int(id))
    command_bus.publish(intent_payment_command)
    return {"ok"}


@app.get("/fetch-shopping-cart/")
def fetch_shopping_cart(id: str = Query(..., description="")):
    fetch_shopping_cart_query = FetchShoppingCartQuery(int(id))
    return query_bus.ask(fetch_shopping_cart_query)


@app.get("/add-line/")
def add_line(
        shopping_cart_id: str = Query(..., description=""),
        line_id: str = Query(..., description=""),
        quantity: int = Query(..., description="")
):
    add_line_command = AddLineCommand(int(shopping_cart_id), int(line_id), int(quantity))
    command_bus.publish(add_line_command)
    return {"ok"}
