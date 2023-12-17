from . import BASE_URL
from .root import MonnifyAPI
from .checkout import Checkout

class Monnify(MonnifyAPI):
    """
    Monnify class represents the Monnify API client.

    Args:
        api_key (str): The API key for authentication.
        secret_key (str): The secret key for authentication.
        contract_code (str): The contract code for the Monnify account.
        base_url (str, optional): The base URL for the Monnify API. Defaults to None.

    Attributes:
        api_key (str): The API key for authentication.
        secret_key (str): The secret key for authentication.
        base_url (str): The base URL for the Monnify API.
        contract_code (str): The contract code for the Monnify account.
        checkout (Checkout): An instance of the Checkout class.

    """

    def __init__(self, api_key, secret_key, contract_code, base_url=None ):
        if base_url is None:
            base_url = BASE_URL
        super().__init__(self,secret_key, api_key, contract_code, base_url, timeout=10)

        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = base_url
        self.contract_code = contract_code
        self.checkout = Checkout