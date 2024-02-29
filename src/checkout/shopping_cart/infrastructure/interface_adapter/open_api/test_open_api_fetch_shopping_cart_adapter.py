from checkout.shopping_cart.infrastructure.interface_adapter.open_api.open_api_fetch_shopping_cart_adapter import \
    OpenApiFetchShoppingCartAdapter
from checkout.shopping_cart.test.mother.domain.shopping_cart_mother import ShoppingCartMother
from checkout.shopping_cart.test.mother.response.open_api_fetch_shopping_cart_adapter_mother import \
    OpenApiFetchShoppingCartAdapterMother


class TestOpenApiFetchShoppingCartAdapter:

    def test_should_parse_to_open_api(self):
        expected_shopping_cart = ShoppingCartMother.create()
        open_api_fetch_shopping_cart_adapter = OpenApiFetchShoppingCartAdapter()

        result = open_api_fetch_shopping_cart_adapter.parse(expected_shopping_cart)

        assert result == OpenApiFetchShoppingCartAdapterMother.create()
