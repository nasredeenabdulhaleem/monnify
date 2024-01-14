import unittest
import os
from unittest.mock import patch, Mock
from monnify.root import MonnifyAPI
from monnify.transaction import (
    Transaction,
)  # Assuming Transaction is the class containing the initiate method


class TransactionTestCase(unittest.TestCase):
    def setUp(self):
        self.api_key = os.getenv("MONNIFY_TEST_API_KEY", "Default")
        self.secret_key = os.getenv("MONNIFY_TEST_SECRET_KEY", "Default")
        self.base_url = os.getenv("MONNIFY_TEST_BASE_URL", "Default")
        self.environment = "sandbox"
        self.monnify_api = MonnifyAPI(
            self.api_key, self.secret_key, self.base_url, self.environment
        )

    @patch.object(Transaction, "make_request")
    def test_initiate(self, mock_make_request):
        mock_response = Mock()
        mock_response.json.return_value = {"success": True}
        mock_make_request.return_value = mock_response
        token_response = self.monnify_api.get_access_token()

        params = {
            "amount": 100.00,
            "customerName": "Test User",
            "customerEmail": "test@user.com",
            "paymentReference": "123456",
            "paymentDescription": "Test transaction",
            "currencyCode": "USD",
            "contractCode": "123456",
            "redirectUrl": "https://example.com/redirect",
            "paymentMethods": ["CARD", "ACCOUNT_TRANSFER"],
        }

        response = Transaction.initiate(**params)

        mock_make_request.assert_called_once_with(
            "/api/v1/merchant/transactions/init-transaction", "POST", data=params
        )
        self.assertEqual(response.json(), {"success": True})

    @patch.object(Transaction, "make_request")
    def test_pay_with_bank_transfer(self, mock_make_request):
        mock_response = Mock()
        mock_response.json.return_value = {"success": True}
        mock_make_request.return_value = mock_response
        params = {
            "transactionReference": "123456",
            "bankCode": "001",
        }
        response = Transaction.pay_with_bank_transfer(**params)
        mock_make_request.assert_called_once_with(
            "/api/v1/merchant/bank-transfer/init-payment", "POST", data=params
        )
        self.assertEqual(response.json(), {"success": True})

    @patch.object(Transaction, "make_request")
    def test_charge_card(self, mock_make_request):
        mock_response = Mock()
        mock_response.json.return_value = {"success": True}
        mock_make_request.return_value = mock_response
        params = {
            "transactionReference": "123456",
            "collectionChannel": "API_NOTIFICATION",
            "card": {
                "number": "4111111111111111",
                "pin": "1234",
                "expiryMonth": "12",
                "expiryYear": "2023",
                "cvv": "123",
            },
        }
        response = Transaction.charge_card(**params)
        mock_make_request.assert_called_once_with(
            "api/v1/merchant/cards/charge", "POST", data=params
        )
        self.assertEqual(response.json(), {"success": True})

    @patch.object(Transaction, "make_request")
    def test_authorize_otp(self, mock_make_request):
        mock_response = Mock()
        mock_response.json.return_value = {"success": True}
        mock_make_request.return_value = mock_response
        params = {
            "transactionReference": "123456",
            "collectionChannel": "API_NOTIFICATION",
            "tokenId": "123456",
            "token": "123456",
        }
        response = Transaction.authorize_otp(**params)
        mock_make_request.assert_called_once_with(
            "/api/v1/merchant/cards/charge", "POST", data=params
        )
        self.assertEqual(response.json(), {"success": True})

    @patch.object(Transaction, "make_request")
    def test_authorize_3ds_card(self, mock_make_request):
        mock_response = Mock()
        mock_response.json.return_value = {"success": True}
        mock_make_request.return_value = mock_response
        params = {
            "transactionReference": "123456",
            "collectionChannel": "API_NOTIFICATION",
            "card": {
                "number": "4111111111111111",
                "pin": "1234",
                "expiryMonth": "12",
                "expiryYear": "2023",
                "cvv": "123",
            },
            "apiKey": "123456",
        }
        response = Transaction.authorize_3ds_card(params)
        mock_make_request.assert_called_once_with(
            "/api/v1/sdk/cards/secure-3d/authorize", "POST", data=params
        )
        self.assertEqual(response.json(), {"success": True})

    @patch.object(Transaction, "make_request")
    def test_get_all_transactions(self, mock_make_request):
        mock_response = Mock()
        mock_response.json.return_value = {"success": True}
        mock_make_request.return_value = mock_response
        params = {
            "page": 0,
            "size": 10,
        }
        response = Transaction.get_all_transactions(**params)
        mock_make_request.assert_called_once_with(
            "/api/v1/transactions/search", "GET", params=params
        )
        print("kai", response)
        self.assertEqual(response.json(), {"success": True})


if __name__ == "__main__":
    unittest.main()
