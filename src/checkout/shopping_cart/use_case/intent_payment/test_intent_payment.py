import pytest
from unittest import mock

from checkout.shopping_cart.domain.error.shopping_cart_invalid_status import ShoppingCartInvalidStatus
from checkout.shopping_cart.domain.error.shopping_cart_not_found import ShoppingCartNotFound
from checkout.shopping_cart.domain.shopping_cart import ShoppingCart
from checkout.shopping_cart.domain.shopping_cart_id import ShoppingCartId
from checkout.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository
from checkout.shopping_cart.domain.shopping_cart_status import ShoppingCartStatus
from checkout.shopping_cart.domain.shopping_cart_total_price import ShoppingCartTotalPrice
from checkout.shopping_cart.use_case.intent_payment.intent_payment import IntentPayment
from checkout.shopping_cart.use_case.intent_payment.intent_payment_command import IntentPaymentCommand


class TestIntentPayment:

    @pytest.fixture
    def shopping_cart_repository_mock(self) -> mock.MagicMock:
        shopping_cart_repo_mock = mock.MagicMock(spec=ShoppingCartRepository)
        shopping_cart_repo_mock.find_by_id = mock.MagicMock(return_value=None)
        return shopping_cart_repo_mock

    def test_intent_payment(self, shopping_cart_repository_mock):
        shopping_cart = ShoppingCart(
            id=ShoppingCartId(1),
            status=ShoppingCartStatus.IN_PROGRESS,
            total_price=ShoppingCartTotalPrice(10),
            lines=[]
        )
        shopping_cart_repository_mock.find_by_id.return_value = shopping_cart
        intent_payment_command = IntentPaymentCommand(1)
        intent_payment = IntentPayment(shopping_cart_repository_mock)

        intent_payment.execute(intent_payment_command)

        # TODO: improve assert comparison
        shopping_cart.status = ShoppingCartStatus.IN_PROGRESS
        shopping_cart_repository_mock.save.assert_called_once_with(shopping_cart)


    def test_should_not_intent_payment_with_not_found_id(self, shopping_cart_repository_mock):
        intent_payment_command = IntentPaymentCommand(1)

        intent_payment = IntentPayment(shopping_cart_repository_mock)
        with pytest.raises(ShoppingCartNotFound):
            intent_payment.execute(intent_payment_command)


    def test_should_not_intent_payment_without_in_progress_status(self, shopping_cart_repository_mock):
        shopping_cart = ShoppingCart(
            id=ShoppingCartId(1),
            status=ShoppingCartStatus.COMPLETED,
            total_price=ShoppingCartTotalPrice(10),
            lines=[]
        )
        shopping_cart_repository_mock.find_by_id.return_value = shopping_cart
        intent_payment_command = IntentPaymentCommand(1)

        intent_payment = IntentPayment(shopping_cart_repository_mock)
        with pytest.raises(ShoppingCartInvalidStatus):
            intent_payment.execute(intent_payment_command)