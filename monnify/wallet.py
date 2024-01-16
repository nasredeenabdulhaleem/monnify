from .root import MonnifyAPI


class Wallet(MonnifyAPI):
    def __init__(self):
        super().__init__()

    @classmethod
    def create_wallet(cls, **kwargs):
        """
        Create Wallet
        This endpoint creates wallets for merchants' customers

        Args:
            walletReference (str): A unique identifier for the wallet
            walletName (str): The desired wallet name
            customerName (str): The customer's name
            customerEmail (str): The customer's email
            bvn (str): The customer's bvn
            bvnDateOfBirth (str): The date of birth associated with the bvn in the format yyyy-mm-dd

        Returns:
            dict: JSON response from Monnify API
        """
        return cls.make_request("/api/v1/disbursements/wallet", "POST", data=kwargs)

    @classmethod
    def wallet_balance(cls, walletReference):
        """
        Wallet Balance
        This endpoint returns the balance associated with a wallet

        Args:
            walletReference (str): The unique identifier of the wallet

        Returns:
            dict: JSON response from Monnify API
        """
        params = {"walletReference": walletReference}

        return cls.make_request(
            "/api/v1/disbursements/wallet/balance", "GET", params=params
        )

    @classmethod
    def get_wallets(cls, customerEmail, pageSize, pageNo):
        """
        Get Wallets
        This endpoint returns all the wallets created by a merchant

        Args:
            customerEmail (str): The customer's email
            pageSize (int): The number of records to return
            pageNo (int): The current page from the total

        Returns:
            dict: JSON response from Monnify API
        """
        data = {"customerEmail": customerEmail}
        params = {"pageSize": pageSize, "pageNo": pageNo}

        return cls.make_request(
            "/api/v1/disbursements/wallet", "GET", data=data, params=params
        )

    @classmethod
    def wallet_transactions(cls, accountNumber, pageSize, pageNo):
        """
        Wallet Transactions
        This endpoint returns all the transactions performed by a wallet

        Args:
            accountNumber (str): The walletAccountNumber
            pageSize (int): The number of wallet records to return
            pageNo (int): A number specifying what page of wallets to be retrieved

        Returns:
            dict: JSON response from Monnify API
        """

        data = {"accountNumber": accountNumber}

        params = {"pageSize": pageSize, "pageNo": pageNo}

        return cls.make_request(
            "/api/v1/disbursements/wallet/transactions", "GET", data=data, params=params
        )
