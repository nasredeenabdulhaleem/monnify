from . import BASE_URL
from .root import MonnifyAPI
from .transaction import Transaction
from .customer import Customer
from .invoice import Invoice
from .limitprofile import LimitProfile
from .recurringpayment import RecurringPayment
from .settlements import Settlements
from .subaccount import SubAccount
from .transfers import Transfers
from .verificationapi import VerificationApi
from .paycodeapi import PayCodeApi
from .refund import Refund
from .wallet import Wallet


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

    def __init__(self, api_key, secret_key, contract_code, base_url=None):
        if base_url is None:
            base_url = BASE_URL
        super().__init__(self, secret_key, api_key, contract_code, base_url, timeout=10)

        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = base_url
        self.contract_code = contract_code
        self.transaction = Transaction
        self.customer = Customer
        self.invoice = Invoice
        self.limit_profile = LimitProfile
        self.recurring_payment = RecurringPayment
        self.settlements = Settlements
        self.sub_account = SubAccount
        self.transfers = Transfers
        self.verification_api = VerificationApi
        self.pay_code_api = PayCodeApi
        self.refund = Refund
        self.wallet = Wallet
