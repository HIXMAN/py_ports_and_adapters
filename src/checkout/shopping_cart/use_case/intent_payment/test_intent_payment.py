import pytest
from unittest import mock

from checkout.shopping_cart.domain.error.shopping_cart_invalid_status import ShoppingCartInvalidStatus
from checkout.shopping_cart.domain.error.shopping_cart_not_found import ShoppingCartNotFound
from checkout.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository
from checkout.shopping_cart.domain.shopping_cart_status import ShoppingCartStatus
from checkout.shopping_cart.test.mother.command.intent_payment_command_mother import IntentPaymentCommandMother
from checkout.shopping_cart.test.mother.domain.shopping_cart_mother import ShoppingCartMother
from checkout.shopping_cart.use_case.intent_payment.intent_payment import IntentPayment
from checkout.shopping_cart.use_case.intent_payment.intent_payment_command import IntentPaymentCommand


class TestIntentPayment:

    @pytest.fixture
    def shopping_cart_repository_mock(self) -> mock.MagicMock:
        shopping_cart_repo_mock = mock.MagicMock(spec=ShoppingCartRepository)
        shopping_cart_repo_mock.find_by_id = mock.MagicMock(return_value=None)
        return shopping_cart_repo_mock

    def test_intent_payment(self, shopping_cart_repository_mock):
        shopping_cart = ShoppingCartMother.create(status=ShoppingCartStatus.IN_PROGRESS)
        shopping_cart_repository_mock.find_by_id.return_value = shopping_cart
        intent_payment_command = IntentPaymentCommandMother.create()
        intent_payment = IntentPayment(shopping_cart_repository_mock)

        intent_payment.execute(intent_payment_command)

        expected_shopping_cart = ShoppingCartMother.create(status=ShoppingCartStatus.COMPLETED)
        shopping_cart_repository_mock.save.assert_called_once_with(expected_shopping_cart)


    def test_should_not_intent_payment_with_not_found_id(self, shopping_cart_repository_mock):
        intent_payment_command = IntentPaymentCommandMother.create()

        intent_payment = IntentPayment(shopping_cart_repository_mock)
        with pytest.raises(ShoppingCartNotFound):
            intent_payment.execute(intent_payment_command)


    @pytest.mark.parametrize("status", [
        ShoppingCartStatus.COMPLETED,
        ShoppingCartStatus.CANCELLED,
        ShoppingCartStatus.CREATED
    ])
    def test_should_not_intent_payment_without_in_progress_status(self, status, shopping_cart_repository_mock):
        shopping_cart = ShoppingCartMother.create(status=status)
        shopping_cart_repository_mock.find_by_id.return_value = shopping_cart
        intent_payment_command = IntentPaymentCommand(1)

        intent_payment = IntentPayment(shopping_cart_repository_mock)
        with pytest.raises(ShoppingCartInvalidStatus):
            intent_payment.execute(intent_payment_command)