from copy import deepcopy
import pytest
from unittest import mock

from checkout.shopping_cart.domain.error.shopping_cart_invalid_line_quanitty import ShoppingCartLineInvalidLineQuantity
from checkout.shopping_cart.domain.error.shopping_cart_invalid_status import ShoppingCartInvalidStatus
from checkout.shopping_cart.domain.error.shopping_cart_not_found import ShoppingCartNotFound
from checkout.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository
from checkout.shopping_cart.domain.shopping_cart_status import ShoppingCartStatus
from checkout.shopping_cart.test.mother.command.add_to_shopping_cart_command_mother import AddToShoppingCartCommandMother
from checkout.shopping_cart.test.mother.command.intent_payment_command_mother import IntentPaymentCommandMother
from checkout.shopping_cart.test.mother.domain.shopping_cart_line_mother import ShoppingCartLineMother
from checkout.shopping_cart.test.mother.domain.shopping_cart_mother import ShoppingCartMother
from checkout.shopping_cart.use_case.add_to_shopping_cart.add_to_shopping_cart import AddToShoppingCart
from checkout.shopping_cart.use_case.intent_payment.intent_payment import IntentPayment


class TestAddToShoppingCart:

    @pytest.fixture
    def shopping_cart_repository_mock(self) -> mock.MagicMock:
        shopping_cart_repo_mock = mock.MagicMock(spec=ShoppingCartRepository)
        shopping_cart_repo_mock.find_by_id = mock.MagicMock(return_value=None)
        shopping_cart_repo_mock.save = mock.MagicMock(return_value=None)

        return shopping_cart_repo_mock

    def test_add_to_cart(self, shopping_cart_repository_mock):
        shopping_cart = ShoppingCartMother.create(status=ShoppingCartStatus.IN_PROGRESS)
        shopping_cart_repository_mock.find_by_id.return_value = shopping_cart
        add_to_cart_command = AddToShoppingCartCommandMother.create()
        add_to_cart = AddToShoppingCart(shopping_cart_repository_mock)

        add_to_cart.execute(add_to_cart_command)

        expected_list = shopping_cart.lines
        expected_list.append(ShoppingCartLineMother.create(id=1, quantity=1))

        expected_shopping_cart = ShoppingCartMother.create(status=ShoppingCartStatus.IN_PROGRESS, lines=expected_list)
        shopping_cart_repository_mock.save.assert_called_once_with(expected_shopping_cart)

    @pytest.mark.parametrize("status", [
        ShoppingCartStatus.COMPLETED,
        ShoppingCartStatus.CANCELLED,
        ShoppingCartStatus.CREATED
    ])
    def test_raise_when_status_is_completed(self, status, shopping_cart_repository_mock):
        shopping_cart = ShoppingCartMother.create(status=status)
        shopping_cart_repository_mock.find_by_id.return_value = shopping_cart
        add_to_cart_command = AddToShoppingCartCommandMother.create()
        add_to_cart = AddToShoppingCart(shopping_cart_repository_mock)

        with pytest.raises(ShoppingCartInvalidStatus):
            add_to_cart.execute(add_to_cart_command)

    def test_raise_when_quantity_is_above_5(self, shopping_cart_repository_mock):
        shopping_cart = ShoppingCartMother.create(status=ShoppingCartStatus.IN_PROGRESS)
        shopping_cart_repository_mock.find_by_id.return_value = shopping_cart
        add_to_cart_command = AddToShoppingCartCommandMother.create(quantity=6)
        add_to_cart = AddToShoppingCart(shopping_cart_repository_mock)

        with pytest.raises(ShoppingCartLineInvalidLineQuantity):
            add_to_cart.execute(add_to_cart_command)
