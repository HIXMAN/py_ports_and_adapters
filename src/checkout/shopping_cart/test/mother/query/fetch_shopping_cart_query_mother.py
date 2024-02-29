from checkout.shopping_cart.use_case.fetch_shopping_cart.fetch_shopping_cart_query import FetchShoppingCartQuery


class FetchShoppingCartQueryMother:
    @staticmethod
    def create(
        id: int = 1,
    ):
        return FetchShoppingCartQuery(id)