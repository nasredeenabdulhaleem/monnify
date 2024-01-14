import base64
import requests
import json
import os

from . import BASE_URL, ENVIRONMENT, TIMEOUT
from datetime import datetime, timedelta
from dateutil.parser import parse
import sys

sys.path.append("/home/abdulhaleem/Documents/monnify/")


class MonnifyAPI:
    """
    MonnifyAPI class represents an API client for interacting with the Monnify payment gateway.

    Args:
        api_key (str): The API key for authentication. If not provided, it will be fetched from the environment variable MONNIFY_API_KEY.
        secret_key (str): The secret key for authentication. If not provided, it will be fetched from the environment variable MONNIFY_SECRET_KEY.
        base_url (str): The base URL of the Monnify API. If not provided, it will be fetched from the environment variable MONNIFY_BASE_URL or use the default value.
        environment (str): The environment for the Monnify API. If not provided, it will be fetched from the environment variable MONNIFY_ENVIRONMENT or use the default value.

    Attributes:
        api_key (str): The API key used for authentication.
        secret_key (str): The secret key used for authentication.
        base_url (str): The base URL of the Monnify API.
        environment (str): The environment for the Monnify API.
        session (requests.Session): The session object for making HTTP requests.
        access_token (str): The access token for authentication.
        expiry_time (datetime.datetime): The expiry time of the access token.

    Methods:
        get_access_token(): Fetches the access token from the Monnify API.
        is_token_expired(): Checks if the access token has expired.
        make_request(endpoint, method, data): Makes an HTTP request to the Monnify API.
        get(endpoint, data): Makes a GET request to the Monnify API.
        post(endpoint, data): Makes a POST request to the Monnify API.
        put(endpoint, data): Makes a PUT request to the Monnify API.
        handle_response(response): Handles the response from the Monnify API.
        handle_error(response): Handles the error response from the Monnify API.
        set_timeout(timeout): Sets the timeout for the HTTP requests.
    """

    def __init__(self, api_key=None, secret_key=None, base_url=None, environment=None):
        self.api_key = api_key or os.getenv("MONNIFY_API_KEY")
        self.secret_key = secret_key or os.getenv("MONNIFY_SECRET_KEY")
        self.base_url = base_url or os.getenv("MONNIFY_BASE_URL") or BASE_URL
        self.environment = (
            environment or os.getenv("MONNIFY_ENVIRONMENT") or ENVIRONMENT
        )

        self.session = requests.Session()
        self.session.base_url = self.base_url
        self.session.timeout = TIMEOUT
        self.access_token, self.expiry_time = self.get_access_token()
        self.session.headers.update({"Authorization": "Bearer " + self.access_token})

    # ...

    def get_access_token(self):
        url = self.base_url + "/api/v1/auth/login"
        AUTHORIZATION = base64.b64encode(
            bytes(self.api_key + ":" + self.secret_key, "utf-8")
        ).decode("utf-8")
        payload = {"AUTHORIZATION": AUTHORIZATION}
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic " + AUTHORIZATION,
        }
        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
            response_data = response.json()
            if response_data["requestSuccessful"]:
                expiry_time = datetime.now() + timedelta(minutes=55)
                access_token = response.json()["responseBody"]["accessToken"]
                return {
                    "success": True,
                    "accessToken": access_token,
                    "expiryTime": expiry_time,
                }
            else:
                res = {
                    "success": False,
                    "error": response_data["responseMessage"],
                    "responseCode": response_data["responseCode"],
                }
                return self.handle_error(res)
        except requests.HTTPError as http_err:
            return {"success": False, "error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"success": False, "error": f"Other error occurred: {err}"}

        # return response.json()["responseBody"]["accessToken"], expiry_time

    def is_token_expired(self):
        return datetime.now() >= parse(self.expiry_time)

    def make_request(self, endpoint, method="GET", data=None, params=None):
        """
        Makes a request to the specified endpoint using the specified HTTP method.

        Args:
            endpoint (str): The endpoint URL to send the request to.
            method (str, optional): The HTTP method to use for the request. Defaults to "GET".
            data (dict, optional): The data to send with the request. Defaults to None.
            params (dict, optional): The URL parameters to send with the request. Defaults to None.
        Returns:
            dict: The response from the API.

        Raises:
            Exception: If the request fails or encounters an error.
        """
        if self.is_token_expired():
            token_response = self.get_access_token()
            if token_response["success"]:
                self.access_token = token_response["accessToken"]
                self.expiry_time = token_response["expiryTime"]
                self.session.headers.update(
                    {"Authorization": "Bearer " + self.access_token}
                )
            else:
                return token_response  # Return the error response from get_access_token

        url = self.session.base_url + endpoint
        response = self.session.request(method, url, data=data, params=params)

        if response.status_code != 200:
            return self.handle_error(response)

        return self.handle_response(response)

    def get(self, endpoint, data=None):
        return self.make_request(endpoint, "GET", data)

    def post(self, endpoint, data=None):
        return self.make_request(endpoint, "POST", data)

    def put(self, endpoint, data=None):
        return self.make_request(endpoint, "PUT", data)

    def handle_response(self, response):
        return json.loads(response.text)

    def handle_error(self, response):
        return json.loads(response.text)

    def set_timeout(self, timeout):
        self.session.timeout = timeout
