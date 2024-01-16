from .root import MonnifyAPI


class RecurringPayment(MonnifyAPI):
    def __init__(self):
        super().__init__()

    @classmethod
    def charge_card_token(cls, **kwargs):
        """
        Charge Card Token
        This method allows you to charge an already tokenized card with it’s card token.

        Args:
            cardToken (str): The card token.
        amount (float): The amount to be charged.
        customerName (str): Full name of the customer.
        customerEmail (str): The customer's email address.
        paymentReference (str): A unique reference for the payment.
        paymentDescription (str): Description for the payment.
        currencyCode (str): The currency of the transaction.
        contractCode (str): Merchant's contract code.
        apiKey (str): Your API key.
        metaData (dict): Additional data related to the transaction.

        Returns:
            dict: JSON response from Monnify API
        """

        return cls.make_request(
            "/api/v1/merchant/cards/charge-card-token", "POST", data=kwargs
        )
