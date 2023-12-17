import unittest
import os
from unittest.mock import patch, Mock
from monnify.root import MonnifyAPI
from monnify.transaction import Transaction  # Assuming Transaction is the class containing the initiate method

class TransactionTestCase(unittest.TestCase):
    def setUp(self):
        self.api_key = os.getenv('MONNIFY_TEST_API_KEY',"Default")
        self.secret_key = os.getenv('MONNIFY_TEST_SECRET_KEY',"Default")
        self.base_url = os.getenv('MONNIFY_TEST_BASE_URL',"Default")
        self.environment = "sandbox"
        self.monnify_api = MonnifyAPI(self.api_key, self.secret_key, self.base_url, self.environment)

    @patch.object(Transaction, 'make_request')
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
            "contractCode":"123456",
            "redirectUrl": "https://example.com/redirect",
            "paymentMethods":["CARD","ACCOUNT_TRANSFER"]
        }

        response = Transaction.initiate(**params)

        mock_make_request.assert_called_once_with('/api/v1/merchant/transactions/init-transaction', 'POST', data=params)
        self.assertEqual(response.json(), {"success": True})

if __name__ == '__main__':
    unittest.main()