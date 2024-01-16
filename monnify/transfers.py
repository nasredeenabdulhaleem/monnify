from .root import MonnifyAPI


class Transfers(MonnifyAPI):
    def __init__(self):
        super().__init__()

    def initiate_transfer_single(self, **kwargs):
        """
        Initiate Transfer (Single)
        This method helps to initiate transfer to desired bank account.

        Args:
            amount (float): Amount to disburse
            reference (str): The unique reference for the transaction
            narration (str): The Narration for the transactions being processed
            destinationBankCode (str): The 3 digit bank code representing the destination bank
            destinationAccountNumber (str): The beneficiary account number
            currency (str): The currency of the transaction being initialised - "NGN"
            sourceAccountNumber (str): Unique identifier of your wallet

        Returns:
            dict: JSON response from Monnify API
        """

        return self.make_request("/api/v2/disbursements/single", "POST", data=kwargs)

    @classmethod
    def initiate_transfer_async(cls, **kwargs):
        """
        Initiate Transfer (Async)
        This method helps initiate transfer asynchronously to desired bank account.

        Args:
            amount (float): Amount to disburse
            reference (str): The unique reference for the transaction
            narration (str): The Narration for the transactions being processed
            destinationBankCode (str): The 3 digit bank code representing the destination bank
            destinationAccountNumber (str): The beneficiary account number
            currency (str): The currency of the transaction being initialised - "NGN"
            sourceAccountNumber (str): Unique identifier of your wallet
            async (bool): An option to process disbursment asynchronously

        Returns:
            dict: JSON response from Monnify API
        """

        return cls.make_request("/api/v2/disbursements/single", "POST", data=kwargs)

    @classmethod
    def initiate_transfer_bulk(cls, **kwargs):
        """
        Initiate Transfer (Bulk)
        This method helps in Initiating Bulk Transfer transactions on your integration.

        Args:
            title (str): The title of the batch disbursement
            batchReference (str): A unique reference identifying the batch disbursement
            narration (str): A narration for the disbursement
            sourceAccountNumber (str): The merchant WALLET ACCOUNT NUMBER.
            onValidationFailure (str): Decision to be taken if any of the disbursement batches fail. Either BREAK or CONTINUE.
            notificationInterval (int): This determines how often Monnify should notify the merchant of its progress when processing a batch transfer
            transactionList (list): A list of transactions to be processed

        Returns:
            dict: JSON response from Monnify API
        """

        return cls.make_request("/api/v2/disbursements/batch", "POST", data=kwargs)

    @classmethod
    def authorize_single_transfer(cls, **kwargs):
        """
        Authorize Single Transfers
        This endpoint authorizes single transfers on your integration.

        Args:
            reference (str): The unique reference for the transfer
            authorizationCode (str): The OTP sent to merchant's email address

        Returns:
            dict: JSON response from Monnify API
        """

        return cls.make_request(
            "/api/v2/disbursements/single/validate-otp", "POST", data=kwargs
        )

    @classmethod
    def authorize_bulk_transfer(cls, **kwargs):
        """
        Authorize Bulk Transfers
        This endpoint authorizes bulk transfers on your integration.

        Args:
            reference (str): The batch reference used in the transfer
            authorizationCode (str): The OTP sent to the merchant's email

        Returns:
            dict: JSON response from Monnify API
        """

        return cls.make_request(
            "/api/v2/disbursements/batch/validate-otp", "POST", data=kwargs
        )

    @classmethod
    def resend_otp(cls, **kwargs):
        """
        Resend OTP
        This endpoint generates a new OTP in the event that there were challenges with the former OTP sent.

        Args:
            reference (str): The reference used for the transfer

        Returns:
            dict: JSON response from Monnify API
        """

        return cls.make_request(
            "/api/v2/disbursements/single/resend-otp", "POST", data=kwargs
        )

    @classmethod
    def single_transfer_status(cls, **kwargs):
        """
        Single Transfer Status
        This endpoint verifies the status of a single transfer on your integration.

        Args:
            reference (str): The reference used for the transfer

        Returns:
            dict: JSON response from Monnify API
        """
        return cls.make_request(
            "/api/v2/disbursements/single/summary", "GET", data=kwargs
        )

    @classmethod
    def list_all_single_transfers(cls, pageSize, pageNo):
        """
        List All Single Transfers
        This endpoint returns the list of all single transfers made on your integration.

        Args:
            pageSize (int): The number of transfer records to return
            pageNo (int): A number specifying what page of transfers to be retrieved

        Returns:
            dict: JSON response from Monnify API
        """
        params = {"pageSize": pageSize, "pageNo": pageNo}

        return cls.make_request(
            "/api/v2/disbursements/single/transactions", "GET", params=params
        )

    @classmethod
    def list_all_bulk_transfers(cls, pageSize, pageNo):
        """
        List All Bulk Transfers
        This endpoint returns the list of all bulk transfers made on your integration.

        Args:
            pageSize (int): The number of transfer records to return
            pageNo (int): A number specifying what page of transfers to be retrieved

        Returns:
            dict: JSON response from Monnify API
        """
        params = {"pageSize": pageSize, "pageNo": pageNo}

        return cls.make_request(
            "/api/v2/disbursements/bulk/transactions", "GET", params=params
        )

    @classmethod
    def get_bulk_transfer_transactions(cls, pageSize, pageNo, batchReference):
        """
        Get Bulk Transfer Transactions
        This endpoint returns the list of all transactions in a bulk transfer batch and their status.

        Args:
            pageSize (int): The number of transfer record to be returned per page
            pageNo (int): A number specifying what page of transfers to be retrieved
            batchReference (str): A unique reference identifying the batch disbursement

        Returns:
            dict: JSON response from Monnify API
        """
        params = {"pageSize": pageSize, "pageNo": pageNo}

        return cls.make_request(
            f"/api/v2/disbursements/bulk/{batchReference}/transactions",
            "GET",
            params=params,
        )

    @classmethod
    def search_disbursement_transactions(
        cls,
        sourceAccountNumber,
        pageSize,
        pageNo,
        startDate,
        endDate,
        amountFrom,
        amountTo,
    ):
        """
        Search Disbursement Transactions
        This endpoint returns the list of all disbursement transactions.

        Args:
            sourceAccountNumber (str): The merchant's WALLET ACCOUNT NUMBER, this parameter is mandatory
            pageSize (int): The number of records to return
            pageNo (int): The current page from the total
            startDate (str): A timestamp value specifying the date to start filtering disbursement transactions by the createdAt field
            endDate (str): A timestamp value specifying the date to stop filtering disbursement transactions by the createdAt field
            amountFrom (str): A number specifying the lower bound for filtering the transactions by the amount field
            amountTo (str): A number specifying the upper bound for filtering the transactions by the amount field

        Returns:
            dict: JSON response from Monnify API
        """
        params = {
            "sourceAccountNumber": sourceAccountNumber,
            "pageSize": pageSize,
            "pageNo": pageNo,
            "startDate": startDate,
            "endDate": endDate,
            "amountFrom": amountFrom,
            "amountTo": amountTo,
        }

        return cls.make_request(
            "/api/v2/disbursements/search-transactions", "GET", params=params
        )

    @classmethod
    def get_wallet_balance(cls, accountNumber):
        """
        Get Wallet Balance
        This endpoint returns the available balance in your monnify wallet.

        Args:
            accountNumber (str): The merchant's WALLET ACCOUNT NUMBER.

        Returns:
            dict: JSON response from Monnify API
        """
        data = {"accountNumber": accountNumber}

        return cls.make_request(
            "/api/v2/disbursements/wallet-balance", "GET", data=data
        )
