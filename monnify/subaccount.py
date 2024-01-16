from .root import MonnifyAPI


class SubAccount(MonnifyAPI):
    def __init__(self):
        super().__init__()

    @classmethod
    def create_sub_account(cls, **kwargs):
        """
        Create Sub Account(s)
        This method allows you to create a sub account to enable the splitting of payments between different accounts.

        Args:
            currencyCode (str): Settlement currency. "NGN"
            accountNumber (str): The account number that should be created as a sub account.
            bankCode (str): The 3 digit bank code of the bank where the account number is domiciled
            email (str): The email tied to the sub account
            defaultSplitPercentage (float): The default percentage to be split into the sub account on any transaction.

        Returns:
            dict: JSON response from Monnify API
        """

        return cls.make_request("/api/v1/sub-accounts", "POST", data=kwargs)

    @classmethod
    def delete_sub_account(cls, subAccountCode):
        """
        Delete Sub Account
        This method deletes a sub account on your integration.
        Args:
            subAccountCode (str): The subAccountCode of the sub account you want to delete.
        Returns:
            dict: JSON response from Monnify API
        """
        return cls.make_request(f"/api/v1/sub-accounts/{subAccountCode}", "DELETE")

    @classmethod
    def get_sub_accounts(cls):
        """
        Get Sub Accounts
        This method returns the list of sub accounts that have been created on your integration.

        Returns:
            dict: JSON response from Monnify API
        """
        return cls.make_request("/api/v1/sub-accounts", "GET")

    @classmethod
    def update_sub_account(cls, **kwargs):
        """
        Update Sub Account
        This method updates the details of an existing sub account.

        Args:
            currencyCode (str): Settlement currency. "NGN"
            accountNumber (str): The account number that should be created as a sub account.
            bankCode (str): The 3 digit bank code of the bank where the account number is domiciled
            email (str): The email tied to the sub account
            defaultSplitPercentage (float): The default percentage to be split into the sub account on any transaction.
            subAccountCode (str): The sub account code of the account to be updated.

        Returns:
            dict: JSON response from Monnify API
        """

        return cls.make_request("/api/v1/sub-accounts", "PUT", data=kwargs)
