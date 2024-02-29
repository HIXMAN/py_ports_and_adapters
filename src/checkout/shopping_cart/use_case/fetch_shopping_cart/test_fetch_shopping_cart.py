import pytest
from unittest import mock

from checkout.shopping_cart.domain.shopping_cart import ShoppingCart
from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from checkout.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository
from checkout.shopping_cart.domain.shopping_cart_status import ShoppingCartStatus
from checkout.shopping_cart.domain.shopping_cart_total_price import ShoppingCartTotalPrice
from checkout.shopping_cart.use_case.fetch_shopping_cart.fetch_shopping_cart import FetchShoppingCart
from checkout.shopping_cart.use_case.fetch_shopping_cart.fetch_shopping_cart_query import FetchShoppingCartQuery


class TestFetchShoppingCart:

    @pytest.fixture
    def shopping_cart_repository_mock(self) -> mock.MagicMock:
        shopping_cart_repo_mock = mock.MagicMock(spec=ShoppingCartRepository)
        shopping_cart_repo_mock.find_by_id = mock.MagicMock(return_value=None)
        return shopping_cart_repo_mock

    @pytest.fixture
    def fetch_shopping_cart_adapter_mock(self) -> mock.MagicMock:
        fetch_shopping_cart_adapter = mock.MagicMock(spec=ShoppingCartRepository)
        fetch_shopping_cart_adapter.parse = mock.MagicMock(return_value=[])
        return fetch_shopping_cart_adapter

    def test_fetch_shopping_cart(self, shopping_cart_repository_mock, fetch_shopping_cart_adapter_mock):
        shopping_cart = ShoppingCart(
            id=ShoppingCartId(1),
            status=ShoppingCartStatus.IN_PROGRESS,
            total_price=ShoppingCartTotalPrice(10),
            lines=[]
        )
        shopping_cart_repository_mock.find_by_id.return_value = shopping_cart
        fetch_shopping_cart_query = FetchShoppingCartQuery(1)
        fetch_shopping_cart = FetchShoppingCart(shopping_cart_repository_mock, fetch_shopping_cart_adapter_mock)

        fetch_shopping_cart.execute(fetch_shopping_cart_query)
        shopping_cart_3 = ShoppingCart(
            id=ShoppingCartId(1),
            status=ShoppingCartStatus.IN_PROGRESS,
            total_price=ShoppingCartTotalPrice(10),
            lines=[]
        )
        fetch_shopping_cart_adapter_mock.parse.assert_called_once_with(shopping_cart_3)