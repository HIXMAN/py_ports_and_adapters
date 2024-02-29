import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from checkout.shopping_cart.domain.shopping_cart_status import ShoppingCartStatus
from checkout.shopping_cart.domain.shopping_cart_total_price import ShoppingCartTotalPrice
from checkout.shopping_cart.infrastructure.sqlalchemy.alchemy_shopping_cart_repository import \
    AlchemyShoppingCartRepository
from checkout.shopping_cart.infrastructure.sqlalchemy.entity.base import Base
from checkout.shopping_cart.test.mother.domain.shopping_cart_line_mother import ShoppingCartLineMother
from checkout.shopping_cart.test.mother.domain.shopping_cart_mother import ShoppingCartMother


class TestAlchemyShoppingCartRepository:

    @pytest.fixture(scope="session")
    def engine(self):
        return create_engine('mysql+pymysql://root:root@database:3306/test_mercaclean'  ,  echo=True)

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

    def test_should_return_none_when_not_found_shopping_cart(self, shopping_cart_repository):
        shopping_cart = shopping_cart_repository.find_by_id(ShoppingCartId(10))
        assert shopping_cart is None

    def test_should_create_a_shopping_cart(self, shopping_cart_repository):
        expected_shopping_cart = ShoppingCartMother.create()

        shopping_cart_repository.save(shopping_cart=expected_shopping_cart)
        shopping_cart = shopping_cart_repository.find_by_id(shopping_cart_id=expected_shopping_cart.id)

        assert shopping_cart.status == ShoppingCartStatus.CREATED
        assert shopping_cart.total_price ==  ShoppingCartTotalPrice(10.10)
        assert shopping_cart.lines[0].id.value() == 1
        assert shopping_cart.lines[0].quantity.value() == 10
        assert shopping_cart.lines[1].id.value() == 2
        assert shopping_cart.lines[1].quantity.value() == 20


    def test_should_update_shopping_cart(self, shopping_cart_repository):
        expected_shopping_cart = ShoppingCartMother.create()
        shopping_cart_repository.save(shopping_cart=expected_shopping_cart)

        new_expected_lines = [
            ShoppingCartLineMother.create(id=3, quantity=30),
            ShoppingCartLineMother.create(id=4, quantity=40),
        ]
        expected_shopping_cart = ShoppingCartMother.create(
            status=ShoppingCartStatus.COMPLETED,
            total_price=20.20,
            lines=new_expected_lines
        )
        shopping_cart_repository.save(expected_shopping_cart)
        shopping_cart = shopping_cart_repository.find_by_id(expected_shopping_cart.id)

        assert shopping_cart.id == ShoppingCartId(1)
        assert shopping_cart.status == ShoppingCartStatus.COMPLETED
        assert shopping_cart.total_price ==  ShoppingCartTotalPrice(20.20)
        assert len(shopping_cart.lines) == 2
        assert shopping_cart.lines[0].id.value() == 3
        assert shopping_cart.lines[0].quantity.value() == 30
        assert shopping_cart.lines[1].id.value() == 4
        assert shopping_cart.lines[1].quantity.value() == 40

    # def test_should_fail_when_shopping_cart_lines_are_incorrect(self):
    #     expected_shopping_lines = [
    #         ShoppingCartLine(ShoppingCartLineId(1), ShoppingCartLineQuantity(1)),
    #         ShoppingCartLine(ShoppingCartLineId(1), ShoppingCartLineQuantity(42)),
    #     ]
    #
    #     expected_shopping_cart = ShoppingCart(
    #         id=ShoppingCartId(4),
    #         status=ShoppingCartStatus.COMPLETED,
    #         total_price=ShoppingCartTotalPrice(7.31),
    #         lines=expected_shopping_lines
    #     )
    #     self.shopping_cart_repository.save(shopping_cart=expected_shopping_cart)
    #     expected_value = self.shopping_cart_repository.find_by_id(expected_shopping_cart.id)
    #     assert expected_value is None


