from checkout.shopping_cart.use_case.add_to_shopping_cart.add_to_shopping_cart_command import AddToShoppingCartCommand


class AddToShoppingCartCommandMother:
    @staticmethod
    def create(
        cart_id: int = 1,
        product_id: int = 1,
        quantity: int = 1


    ) -> AddToShoppingCartCommand:
        return AddToShoppingCartCommand(cart_id, product_id, quantity)