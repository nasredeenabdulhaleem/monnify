import unittest
from unittest.mock import patch, Mock
from monnify.customer import Customer


class CustomerTestCase(unittest.TestCase):
    @patch.object(Customer, "make_request")
    def test_create_reserved_account(self, mock_make_request):
        mock_response = Mock()
        mock_response.json.return_value = {"success": True}
        mock_make_request.return_value = mock_response

        params = {
            "accountReference": "1234567890",
            "accountName": "John Doe",
            "currencyCode": "NGN",
            "contractCode": "1234567890",
            "customerEmail": "test@user.com",
            "bvn": "1234567890",
            "getAllAvailableBanks": True,
            "preferredBanks": ["001", "002"],
            "incomeSplitConfig": {},
            "restrictPaymentSource": False,
            "allowedPaymentSource": {},
            "nin": "1234567890",
        }

        response = Customer.create_reserved_account(**params)

        mock_make_request.assert_called_once_with(
            "/api/v2/bank-transfer/reserved-accounts", "POST", data=params
        )
        self.assertEqual(response.json(), {"success": True})

    @patch.object(Customer, "make_request")
    def test_create_reserved_account_invoice(self, mock_make_request):
        mock_response = Mock()
        mock_response.json.return_value = {"success": True}
        mock_make_request.return_value = mock_response

        params = {
            "contractCode": "1234567890",
            "accountName": "John Doe",
            "currencyCode": "NGN",
            "accountReference": "1234567890",
            "customerName": "John Doe",
            "customerEmail": "test@user.com",
            "reservedAccountType": "INVOICE",
            "bvn": "1234567890",
            "nin": "1234567890",
        }

        response = Customer.create_reserved_account_invoice(**params)

        mock_make_request.assert_called_once_with(
            "/api/v1/bank-transfer/reserved-accounts", "POST", data=params
        )
        self.assertEqual(response.json(), {"success": True})

    @patch.object(Customer, "make_request")
    def test_get_reserved_account_detail(self, mock_make_request):
        mock_response = Mock()
        mock_response.json.return_value = {"success": True}
        mock_make_request.return_value = mock_response

        accountReference = "1234567890"

        response = Customer.get_reserved_account_detail(accountReference)

        mock_make_request.assert_called_once_with(
            f"/api/v2/bank-transfer/reserved-accounts/{accountReference}",
            "GET",
            data={},
        )
        self.assertEqual(response.json(), {"success": True})

    @patch.object(Customer, "make_request")
    def test_get_linked_accounts(self, mock_make_request):
        mock_response = Mock()
        mock_response.json.return_value = {"success": True}
        mock_make_request.return_value = mock_response

        params = {
            "getAllAvailableBanks": True,
            "preferredBanks": ["001", "002"],
            "accountReference": "1234567890",
        }

        response = Customer.get_linked_accounts(**params)

        mock_make_request.assert_called_once_with(f"/api/v1/bank-transfer/reserved-accounts/add-linked-accounts/{params['accountReference']}","PUT",data=params)
        self.assertEqual(response.json(), {"success": True})
    
    @patch.object(Customer, "make_request")
    def test_update_bvn_for_reserved_account(self, mock_make_request):
        mock_response = Mock()
        mock_response.json.return_value = {"success": True}
        mock_make_request.return_value = mock_response

        reservedAccountReference = "1234567890"
        bvn = "1234567890"

        response = Customer.update_bvn_for_reserved_account(
            reservedAccountReference, bvn
        )

        mock_make_request.assert_called_once_with(
            f"/api/v1/bank-transfer/reserved-accounts/update-customer-bvn/{reservedAccountReference}",
            "PUT",
            data={"bvn": bvn},
        )
        self.assertEqual(response.json(), {"success": True})

    @patch.object(Customer, "make_request")
    def test_update_allowed_payment_sources(self, mock_make_request):
        mock_response = Mock()
        mock_response.json.return_value = {"success": True}
        mock_make_request.return_value = mock_response

        params = {
            "accountReference": "1234567890",
            "restrictPaymentSource": False,
            "allowedPaymentSource": {},
        }

        response = Customer.update_allowed_payment_sources(**params)

        mock_make_request.assert_called_once_with(f"/api/v1/bank-transfer/reserved-accounts/update-payment-source-filter/{params['accountReference']}", "PUT", data=params)
        self.assertEqual(response.json(), {"success": True})



if __name__ == "__main__":
    unittest.main()
