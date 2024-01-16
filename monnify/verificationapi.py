from .root import MonnifyAPI


class VerificationApi(MonnifyAPI):
    def __init__(self):
        super().__init__()

    @classmethod
    def validate_bank_account(cls, accountNumber, bankCode):
        """
        Validate Bank Account
        This endpoint validates a Customer's NUBAN Account.

        Args:
            accountNumber (str): The account number to be validated
            bankCode (str): The bank code of the required account number

        Returns:
            dict: JSON response from Monnify API
        """
        params = {"accountNumber": accountNumber, "bankCode": bankCode}

        return cls.make_request(
            "/api/v1/disbursements/account/validate", "GET", params=params
        )

    @classmethod
    def verify_bvn_information(cls, **kwargs):
        """
        BVN Information Verification
        This endpoint verifies the BVN information of your customers.

        Args:
            bvn (str): The user's bvn
            name (str): The user’s name
            dateOfBirth (str): The user’s date of birth
            mobileNo (str): The user's mobile number

        Returns:
            dict: JSON response from Monnify API
        """

        return cls.make_request("/api/v1/vas/bvn-details-match", "POST", data=kwargs)

    @classmethod
    def verify_bvn_and_account_name_match(cls, **kwargs):
        """
        BVN and Account Name Match
        This endpoint verifies that the Bank verification number and the account number supplied by a user match the BVN and account number linked to that account.

        Args:
            bankCode (str): The user’s bank code
            accountNumber (str): The user's account number
            bvn (str): The user’s bvn

        Returns:
            dict: JSON response from Monnify API
        """

        return cls.make_request("/api/v1/vas/bvn-account-match", "POST", data=kwargs)
