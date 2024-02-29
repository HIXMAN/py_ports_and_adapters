from checkout.shopping_cart.domain.shopping_cart import ShoppingCart
from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from checkout.shopping_cart.domain.shopping_cart_line import ShoppingCartLine
from checkout.shopping_cart.domain.shopping_cart_line_id import ShoppingCartLineId
from checkout.shopping_cart.domain.shopping_cart_line_quantity import ShoppingCartLineQuantity
from checkout.shopping_cart.domain.shopping_cart_status import ShoppingCartStatus
from checkout.shopping_cart.domain.shopping_cart_total_price import ShoppingCartTotalPrice
from checkout.shopping_cart.infrastructure.sqlalchemy.alchemy_shopping_cart_repository import \
    AlchemyShoppingCartRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from checkout.shopping_cart.infrastructure.sqlalchemy.entity.base import Base


class TestAlchemyShoppingCartRepository:

    def setup_class(self):
        engine = create_engine('mysql+pymysql://root:root@database:3306/test_mercaclean'  ,  echo=True)
        Base.metadata.create_all(bind=engine)
        create_session = sessionmaker(bind=engine)
        self.session = create_session()
        self.shopping_cart_repository = AlchemyShoppingCartRepository(self.session)

    def teardown_class(self):
        self.session.rollback()
        self.session.close()

    def test_should_return_none_when_not_found_shopping_cart(self):
        shopping_cart = self.shopping_cart_repository.find_by_id(ShoppingCartId(10))
        assert shopping_cart is None

    def test_should_create_a_shopping_cart(self):
        expected_shopping_lines = [
            ShoppingCartLine(ShoppingCartLineId(1), ShoppingCartLineQuantity(2)),
            ShoppingCartLine(ShoppingCartLineId(2), ShoppingCartLineQuantity(2)),
        ]

        expected_shopping_cart = ShoppingCart(
            id=ShoppingCartId(1),
            status=ShoppingCartStatus.COMPLETED,
            total_price=ShoppingCartTotalPrice(7.31),
            lines=expected_shopping_lines
        )
        self.shopping_cart_repository.save(shopping_cart=expected_shopping_cart)
        shopping_cart = self.shopping_cart_repository.find_by_id(expected_shopping_cart.id)
        assert shopping_cart == expected_shopping_cart
        assert shopping_cart.status == ShoppingCartStatus.COMPLETED
        assert shopping_cart.total_price == expected_shopping_cart.total_price
        assert shopping_cart.lines == expected_shopping_lines


    def test_should_update_shopping_cart(self):
        expected_shopping_lines = [
            ShoppingCartLine(ShoppingCartLineId(1), ShoppingCartLineQuantity(70)),
            ShoppingCartLine(ShoppingCartLineId(2), ShoppingCartLineQuantity(80)),
        ]

        expected_shopping_cart = ShoppingCart(
            id=ShoppingCartId(7),
            status=ShoppingCartStatus.COMPLETED,
            total_price=ShoppingCartTotalPrice(7.31),
            lines=expected_shopping_lines
        )
        self.shopping_cart_repository.save(shopping_cart=expected_shopping_cart)
        shopping_cart = self.shopping_cart_repository.find_by_id(expected_shopping_cart.id)

        shopping_cart.status = ShoppingCartStatus.IN_PROGRESS
        shopping_cart.total_price = ShoppingCartTotalPrice(20.21)
        new_expected_lines = [
            ShoppingCartLine(ShoppingCartLineId(3), ShoppingCartLineQuantity(20)),
            ShoppingCartLine(ShoppingCartLineId(4), ShoppingCartLineQuantity(30)),
        ]
        shopping_cart.lines = new_expected_lines

        self.shopping_cart_repository.save(shopping_cart)

        shopping_cart = self.shopping_cart_repository.find_by_id(expected_shopping_cart.id)

        assert shopping_cart == expected_shopping_cart
        assert shopping_cart.status == ShoppingCartStatus.IN_PROGRESS
        assert shopping_cart.total_price ==  ShoppingCartTotalPrice(20.21)
        assert shopping_cart.lines == new_expected_lines

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


