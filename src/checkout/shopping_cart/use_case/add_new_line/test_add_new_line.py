import pytest
from unittest import mock

from checkout.shopping_cart.domain.error.shopping_cart_not_found import ShoppingCartNotFound
from checkout.shopping_cart.domain.shopping_cart_line import ShoppingCartLine
from checkout.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository
from checkout.shopping_cart.test.mother.domain.shopping_cart_mother import ShoppingCartMother
from checkout.shopping_cart.test.mother.query.fetch_shopping_cart_query_mother import FetchShoppingCartQueryMother
from checkout.shopping_cart.use_case.add_new_line.add_new_line import AddLineToShoppingCart
from checkout.shopping_cart.use_case.fetch_shopping_cart.fetch_shopping_cart import FetchShoppingCart


class TestAddNewLine:

    @pytest.fixture
    def shopping_cart_repository_mock(self) -> mock.MagicMock:
        shopping_cart_repo_mock = mock.MagicMock(spec=ShoppingCartRepository)
        shopping_cart_repo_mock.find_by_id = mock.MagicMock(return_value=None)
        return shopping_cart_repo_mock


    def test_add_line_to_shopping_cart(self, shopping_cart_repository_mock):
        shopping_cart = ShoppingCartMother.create()
        shopping_cart_repository_mock.find_by_id.return_value = shopping_cart
        line = ShoppingCartLine(id=1, quantity=1)
        AddLineToShoppingCart(shopping_cart_repository_mock).execute(shopping_cart.id, line)


        shopping_cart_repository_mock.save.assert_called_once_with(shopping_cart)
        assert len(shopping_cart.lines) == 3

