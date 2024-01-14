from .root import MonnifyAPI
from urllib.parse import quote


class Transaction(MonnifyAPI):
    def __init__(self):
        super().__init__()

    @classmethod
    def initiate(cls, **kwargs):
        """
        Initialize transaction.

        Args:
            amount (float): Value of  'amount' .
            customerName (str):  The name of the customer .
            customerEmail (str): The customer email.
            paymentReference (str): A unique string of characters that identifies each transaction.
            paymentDescription (str): A description of the payment.
            currencyCode (str): The currency code.
            contractCode (str): The merchant contract code.
            redirectUrl (str): A url to redirect to after payment completion.
            paymentMethods (list): The method of payment collection'.
            incomeSplitConfig (dict, optional): A way to split payments among subAccounts.
            metadata (dict,optional): This field can be used to pass extra information from customers

        Returns:
            Json data from monnify API.
        """

        return cls.make_request(
            "/api/v1/merchant/transactions/init-transaction", "POST", data=kwargs
        )

    @classmethod
    def pay_with_bank_transfer(cls, **kwargs):
        """
        Pay with bank transfer.

        Args:
            transactionReference (str) : A unique Monnify reference returned as part of the response from the initialise transaction endpoint.
            bankCode (str):  A valid bank code to enable the creation of USSD string associated with such bank.
        Returns:
            Json data from monnify API.
        """

        return cls.make_request(
            "/api/v1/merchant/bank-transfer/init-payment", "POST", data=kwargs
        )

    @classmethod
    def charge_card(cls, **kwargs):
        """
        This endpoint allows you to initiate charge on a card.

        Args:

            transactionReference (str) : A unique Monnify reference returned as part of the response from the initialise transaction endpoint.
            collectionChannel (str): This field basically describes the channel of collection.
            card (dict): An object containing the card information.
                number (str): The card pan or number on the card.
                pin (str): The pin associated with the card.
                expiryMonth (str): The card expiry month.
                expiryYear (str): The card expiry year
                cvv (str): The card cvv number.
        Returns:
            Json data from monnify API.
        """

        return cls.make_request("api/v1/merchant/cards/charge", "POST", data=kwargs)

    @classmethod
    def authorize_otp(cls, **kwargs):
        """
        The endpoint authorizes an OTP to complete a charge on a card.

        Args:
            transactionReference (str): The transaction reference gotten from the initialise transaction endpoint.
            collectionChannel (str): This is the channel of collection and should always be "API_NOTIFICATION" in this endpoint.
            tokenId (str): This is an id of the token issued and is always part of the response from the charge card endpoint.
            token (str): This is the token(OTP) sent to the user device by his bank

        Returns:
            Json data from monnify API.
        """
        return cls.make_request("/api/v1/merchant/cards/charge", "POST", data=kwargs)

    @classmethod
    def authorize_3ds_card(cls, kwargs):
        """
        Authorize 3DS Card
            This endpoint authorizes charge on a card that uses 3DS Secure Authentication.

        Args:
            transactionReference (str): The transaction reference gotten from the initialise transaction endpoint.
        collectionChannel (str): This is the channel of collection and should always be "API_NOTIFICATION" in this endpoint.
        card (dict): An object containing the card information.
            number (str): The card pan or number on the card.
            pin (str): The pin associated with the card.
            expiryMonth (str): The card expiry month.
            expiryYear (str): The card expiry year.
            cvv (str): The card cvv number.
        apiKey (str): The merchant API key.
        Returns:
            Json data from monnify API.
        """
        return cls.make_request(
            "/api/v1/sdk/cards/secure-3d/authorize", "POST", data=kwargs
        )

    @classmethod
    def get_all_transactions(cls, page=0, size=10, **kwargs):
        """
        Get All Transactions
        This method returns a list of transactions carried out on your integration.

        Args:
            page (int): The number of page of to be retrieved. It starts from 0.
            size (int): The Size of transactions to be returned per page.
            **kwargs: Other optional parameters including paymentReference, transactionReference, fromAmount, toAmount, amount, customerName, customerEmail, paymentStatus, from, to.

        Returns:
            dict: JSON response from Monnify API
        """
        params = {"page": page, "size": size}
        params.update(kwargs)

        return cls.make_request("/api/v1/transactions/search", "GET", params=params)

    @classmethod
    def get_transaction_status(cls, transactionReference, **kwargs):
        """
        Get Transaction Status
            This endpoint returns the status of a transaction.
        Args:
            transactionReference (str): Urlencoding of the said transaction reference.
        Returns:
            Json data from monnify API.
        """
        encoded_transactionReference = quote(transactionReference)
        cls.make_request(
            f"/api/v2/transactions/status/{encoded_transactionReference}",
            "GET",
            data=kwargs,
        )
