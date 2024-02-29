import pytest

from unittest import mock


from checkout.shopping_cart.use_case.fetch_shopping_cart.fetch_shopping_cart import FetchShoppingCart
from checkout.shopping_cart.use_case.fetch_shopping_cart.fetch_shopping_cart_query import FetchShoppingCartQuery


class TestFetchShoppingCart:

    @pytest.fixture
    def fetch_shopping_cart_repository_mock(self) -> mock.MagicMock:
        return mock.MagicMock()

    @pytest.fixture
    def fetch_shopping_cart_adapter_mock(self) -> mock.MagicMock:
        return mock.MagicMock()

    def test_fetch_shopping_cart(self, fetch_shopping_cart_repository_mock, fetch_shopping_cart_adapter_mock):
        query_obj = FetchShoppingCartQuery(1)

        pepe = FetchShoppingCart(fetch_shopping_cart_repository_mock, fetch_shopping_cart_adapter_mock).execute(
            query_obj)
        assert pepe is not None