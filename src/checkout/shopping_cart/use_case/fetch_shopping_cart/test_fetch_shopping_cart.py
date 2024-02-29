import pytest
from unittest import mock

from checkout.shopping_cart.domain.error.shopping_cart_not_found import ShoppingCartNotFound
from checkout.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository
from checkout.shopping_cart.test.mother.domain.shopping_cart_mother import ShoppingCartMother
from checkout.shopping_cart.test.mother.query.fetch_shopping_cart_query_mother import FetchShoppingCartQueryMother
from checkout.shopping_cart.use_case.fetch_shopping_cart.fetch_shopping_cart import FetchShoppingCart


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
        shopping_cart = ShoppingCartMother.create()
        shopping_cart_repository_mock.find_by_id.return_value = shopping_cart
        fetch_shopping_cart_query = FetchShoppingCartQueryMother.create()
        fetch_shopping_cart = FetchShoppingCart(shopping_cart_repository_mock, fetch_shopping_cart_adapter_mock)

        fetch_shopping_cart.execute(fetch_shopping_cart_query)

        fetch_shopping_cart_adapter_mock.parse.assert_called_once_with(shopping_cart)

    def test_should_not_intent_payment_with_not_found_id(
            self,
            shopping_cart_repository_mock,
            fetch_shopping_cart_adapter_mock
    ):
        fetch_shopping_cart_query = FetchShoppingCartQueryMother.create()
        fetch_shopping_cart = FetchShoppingCart(shopping_cart_repository_mock, fetch_shopping_cart_adapter_mock)
        with pytest.raises(ShoppingCartNotFound):
            fetch_shopping_cart.execute(fetch_shopping_cart_query)