from shared.domain.command.command import Command


class AddToShoppingCartCommand(Command):

    def __init__(self, shopping_cart_id: int, product_id: int, quantity: int):
        self.shopping_cart_id = shopping_cart_id
        self.product_id = product_id
        self.quantity = quantity

    def name(self) -> str:
        return 'checkout.shopping_cart.use_case.add_to_shopping_cart'
