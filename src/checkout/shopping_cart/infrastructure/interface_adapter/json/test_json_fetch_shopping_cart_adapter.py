from checkout.shopping_cart.infrastructure.interface_adapter.json.json_fetch_shopping_cart_adapter import \
    JsonFetchShoppingCartAdapter
from checkout.shopping_cart.test.mother.domain.shopping_cart_mother import ShoppingCartMother
from checkout.shopping_cart.test.mother.response.json_fetch_shopping_cart_adapter_mother import \
    JsonFetchShoppingCartAdapterMother


class TestJsonFetchShoppingCartAdapter:

    def test_should_parse_to_json(self):
        expected_shopping_cart = ShoppingCartMother.create()
        json_fetch_shopping_cart_adapter = JsonFetchShoppingCartAdapter()

        result = json_fetch_shopping_cart_adapter.parse(expected_shopping_cart)

        assert result == JsonFetchShoppingCartAdapterMother.create()
