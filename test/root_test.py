import unittest
import os
from unittest.mock import patch, Mock
from datetime import datetime

from monnify.root import MonnifyAPI

class TestMonnifyAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = os.getenv('MONNIFY_TEST_API_KEY',"Default")
        self.secret_key = os.getenv('MONNIFY_TEST_SECRET_KEY',"Default")
        self.base_url = os.getenv('MONNIFY_TEST_BASE_URL',"Default")
        self.environment = "sandbox"
        self.monnify_api = MonnifyAPI(self.api_key, self.secret_key, self.base_url, self.environment)

    @patch('requests.Session')
    def test_init(self, mock_session):
        self.monnify_api = MonnifyAPI(self.api_key, self.secret_key, self.base_url, self.environment)
        self.assertEqual(self.monnify_api.api_key, self.api_key)
        self.assertEqual(self.monnify_api.secret_key, self.secret_key)
        self.assertEqual(self.monnify_api.base_url, self.base_url)
        self.assertEqual(self.monnify_api.environment, self.environment)
        mock_session.assert_called_once()

    @patch('requests.post')
    def test_get_access_token(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "requestSuccessful": True,
            "responseBody": {
                "accessToken": "test_access_token",
                "expiresIn": 3567
            }
        }
        mock_post.return_value = mock_response

        # access_token, expiry_time = self.monnify_api.get_access_token()
        token_response = self.monnify_api.get_access_token()

        # expiry_time = token_response["expiry_time"]
        
        self.assertTrue(token_response["success"])
        self.assertEqual(token_response["accessToken"], "test_access_token")
        self.assertIsInstance(token_response["expiryTime"], datetime)

    # @patch('requests.Session')
    # def test_make_request_get_access_token(self, mock_session):
    #     # mock_response = Mock()
    #     # mock_response.json.return_value = {
    #     #     "success": True,
    #     #     "accessToken": "test_access_token",
    #     #     "expiryTime": datetime.now()
    #     # }
    #     # mock_session.request.return_value = mock_response
    #     token_response = self.monnify_api.get_access_token()

    #     mock_response = Mock()
    #     mock_response.json.return_value = token_response
    #     mock_session.request.return_value = mock_response

    #     response = self.monnify_api.make_request('/test_endpoint')

    #     self.assertEqual(response["accessToken"], "test_access_token")
    #     self.assertIsInstance(response["expiryTime"], datetime)

    # @patch('requests.Session')
    # def test_make_request_handle_error(self, mock_session):
    #     mock_response = Mock()
    #     mock_response.status_code = 400
    #     mock_session.request.return_value = mock_response

    #     response = self.monnify_api.make_request('/test_endpoint')

    #     self.assertEqual(response.status_code, 400)

    
    # @patch('requests.Session')
    # def test_make_request_handle_response(self, mock_session):
    #     mock_response = Mock()
    #     mock_response.status_code = 200
    #     mock_response.json.return_value = {
    #         "success": True,
    #         "data": "test_data"
    #     }
    #     mock_session.request.return_value = mock_response

    #     response = self.monnify_api.make_request('/test_endpoint')

    #     self.assertEqual(response["data"], "test_data")


if __name__ == '__main__':
    unittest.main()