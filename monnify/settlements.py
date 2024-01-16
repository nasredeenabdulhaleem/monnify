from .root import MonnifyAPI


class Settlements(MonnifyAPI):
    def __init__(self):
        super().__init__()

    @classmethod
    def get_transactions_by_settlement_reference(cls, reference, page=0, size=10):
        """
        Get Transactions By Settlement Reference
        This endpoint returns all transactions that made up a settlement.

        Args:
            reference (str): The settlement reference
            page (int, optional): The current page of the record. Defaults to 0.
            size (int, optional): The number of transactions per page. Defaults to 10.

        Returns:
            dict: JSON response from Monnify API
        """
        params = {"reference": reference, "page": page, "size": size}

        return cls.make_request(
            "/api/v1/transactions/find-by-settlement-reference", "GET", params=params
        )

    @classmethod
    def get_settlement_information_for_transaction(cls, transactionReference):
        """
        Get Settlement Information for Transaction
        This endpoint returns settlement information on transactions made to your settlement account.

        Args:
            transactionReference (str): The Monnify transaction reference of the desired transaction.

        Returns:
            dict: JSON response from Monnify API
        """
        params = {"transactionReference": transactionReference}

        return cls.make_request("/api/v1/settlement-detail", "GET", params=params)
