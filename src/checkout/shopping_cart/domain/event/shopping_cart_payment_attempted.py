from shared.domain.event.event import Event


class ShoppingCartPaymentAttempted(Event):

    def name(self) -> str:
        return 'checkout.shopping_cart.event.shopping_cart_payment_attempted'
