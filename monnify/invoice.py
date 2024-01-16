from .root import MonnifyAPI


class Invoice(MonnifyAPI):
    def __init__(self):
        super().__init__()

    @classmethod
    def create_invoice(cls, **kwargs):
        """
        Create an Invoice
        This method creates invoice for payments on your integration.

        Args:
            amount (float): The amount to be paid by the customer
            currencyCode (str): The currency of the transaction being initialized. "NGN"
            invoiceReference (str): Merchant's Unique reference for the invoice
            customerName (str): Full name of the customer
            customerEmail (str): Email of the customer
            contractCode (str): Merchant's contract code
            description (str): Description of the transaction. Will be used as the account name for bank transfer payments
            expiryDate (str): The expiry date for the invoice. The format is:YYYY-MM-DD HH:MM:SS
            incomeSplitConfig (dict): This field contains specifications on how payments to this reserve account should be split.
            redirectUrl (str): A URL which customer will be redirected to when payment is successfully completed

        Returns:
            dict: JSON response from Monnify API
        """

        return cls.make_request("/api/v1/invoice/create", "POST", data=kwargs)

    @classmethod
    def get_invoice_details(cls, invoiceReference):
        """
        View Invoice Details
        This method returns details of an invoice on your integration.

        Args:
            invoiceReference (str): The unique reference used in creating the invoice.

        Returns:
            dict: JSON response from Monnify API
        """
        return cls.make_request(f"/api/v1/invoice/{invoiceReference}/details", "GET")

    @classmethod
    def get_all_invoices(cls):
        """
        Get All Invoices
        This method returns the list of all the invoice available on your integration.

        Returns:
            dict: JSON response from Monnify API
        """
        return cls.make_request("/api/v1/invoice/all", "GET")

    @classmethod
    def cancel_invoice(cls, invoiceReference):
        """
        Cancel an Invoice
        This method cancels an Invoice on your integration.

        Args:
            invoiceReference (str): The unique reference used in creating the invoice.

        Returns:
            dict: JSON response from Monnify API
        """
        return cls.make_request(f"/api/v1/invoice/{invoiceReference}/cancel", "DELETE")

    @classmethod
    def attach_reserved_account_to_invoice(cls, **kwargs):
        """
        Attaching a Reserved Account to an Invoice
        This method attaches a Reserved Account to an Invoice.

        Args:
            amount (float): Amount to be paid
            currencyCode (str): The currency of the transaction being initialized. "NGN"
            invoiceReference (str): Merchant's Unique reference for the invoice.
            customerName (str): Full name of the customer
            customerEmail (str): Email address of the customer
            contractCode (str): Merchant's contract code
            description (str): Description for the transaction.
            expiryDate (str): Expiry date for the invoice
            incomeSplitConfig (dict): This field contains specifications on how payments to this reserve account should be split.
            accountReference (str): Your unique reference used to identify this reserved account

        Returns:
            dict: JSON response from Monnify API
        """

        return cls.make_request("/api/v1/invoice/create", "POST", data=kwargs)
