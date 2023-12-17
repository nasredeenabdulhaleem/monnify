from .root import MonnifyAPI

class Transaction(MonnifyAPI):

    def __init__(self):
        super().__init__()
        
    @classmethod
    def initiate(cls,**kwargs):
        """
        Initialize transaction.

        Args:
            amount:
            customerName: 
            customerEmail: 
            paymentReference: 
            paymentDescription: 
            currencyCode: 
            contractCode:
            redirectUrl: 
            paymentMethods:

        Returns:
            Json data from monnify API.
        """

        return cls.make_request('/api/v1/merchant/transactions/init-transaction', 'POST', data = kwargs)
