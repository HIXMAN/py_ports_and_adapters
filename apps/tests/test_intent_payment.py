import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from apps.api.main import app
from checkout.shopping_cart.domain.shopping_cart import ShoppingCart
from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from checkout.shopping_cart.domain.shopping_cart_status import ShoppingCartStatus
from checkout.shopping_cart.infrastructure.sqlalchemy.alchemy_shopping_cart_repository import \
    AlchemyShoppingCartRepository
from checkout.shopping_cart.infrastructure.sqlalchemy.entity.base import Base
from checkout.shopping_cart.test.mother.domain.shopping_cart_mother import ShoppingCartMother


class TestIntentPayment:

    @pytest.fixture()
    def client(self):
        return TestClient(app)


    @pytest.fixture(scope="session")
    def engine(self):
        return create_engine('mysql+pymysql://root:root@database:3306/test_mercaclean',  echo=True)

    @pytest.fixture(scope="session")
    def tables(self, engine):
        Base.metadata.create_all(engine)
        yield
        Base.metadata.drop_all(engine)

    @pytest.fixture
    def dbsession(self, engine, tables):
        """Returns a sqlalchemy session, and after the test tears down everything properly."""
        connection = engine.connect()
        # begin the nested transaction
        transaction = connection.begin()
        # use the connection with the already started transaction
        session = Session(bind=connection)

        yield session

        session.close()
        # roll back the broader transaction
        transaction.rollback()
        # put back the connection to the connection pool
        connection.close()

    @pytest.fixture
    def shopping_cart_repository(self, dbsession):
        return AlchemyShoppingCartRepository(dbsession)

    @pytest.fixture
    def shopping_cart(self, shopping_cart_repository):
        shopping_cart = ShoppingCartMother.create(status=ShoppingCartStatus.IN_PROGRESS)
        shopping_cart_repository.save(shopping_cart)
        return shopping_cart_repository.find_by_id(ShoppingCartId(1))

    def test_intent_payment(self, client, shopping_cart: ShoppingCart):
        response = client.get(f"/intent-payment/?id={shopping_cart.id.value()}")
        assert response.status_code == 200