from shared.domain.query.query import Query


class FetchShoppingCartQuery(Query):

    def __init__(
            self,
            shopping_cart_id: int,
    ) -> None:
        self.shopping_cart_id = shopping_cart_id

    def name(self) -> str:
        return 'checkout.shopping_cart.use_case.fetch_shopping_cart'
