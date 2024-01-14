# Monnify Python Package

This package provides a Python interface for the Monnify API. It allows you to interact with the Monnify payment gateway from your Python applications.

## Installation

You can install the Monnify package from PyPI using pip:

Usage
First, import the Monnify class from the monnify package:

Next, create an instance of the Monnify class. You can pass your API key, secret key, and contract code as arguments to the constructor:

If you don't pass these arguments, the Monnify class will try to get them from the environment variables MONNIFY_API_KEY, MONNIFY_SECRET_KEY, and MONNIFY_CONTRACT_CODE.

The Monnify instance has methods for interacting with the Monnify API. For example, you can make a GET request to an API endpoint like this:

```py
response = monnify.get("/path/to/endpoint")
```

The `get` method returns the response from the Monnify API in JSON format.

## Token Management

The `Monnify` class automatically handles access tokens. When you create a `Monnify` instance, it gets an access token from the Monnify API, stores the token and its expiry time, and uses the token for authorization when making requests to the API.

The `Monnify` class also checks if the token is expired before making a request. If the token is expired, it gets a new token from the API.

## Error Handling

The `Monnify` class handles errors by returning the error message in JSON format. If a request to the Monnify API fails, the method making the request will return a JSON object with a `success` field set to `False` and an `error` field containing the error message.

## Timeouts

The `Monnify` class uses a default timeout of 30 seconds for requests to the Monnify API. You can change the timeout by calling the `set_timeout` method:

```python
monnify.set_timeout(60)
```

Checkout
The Monnify class also provides a Checkout class for handling checkout operations. You can use it like this:

The Checkout class provides methods for interacting with the Monnify API's checkout endpoints.

```md
Please replace "your_api_key", "your_secret_key", and "your_contract_code" with your actual API key, secret key, and contract code. Also, replace "/path/to/endpoint" with the actual API endpoint you want to call.
```

### Package Documentation

#### Transaction

##### initiate

- General - This method is called to initiate a transaction and it returns json data with the checkout url and the transaction details - it accepts params passed as \*\*kwargs to the method call - sample

      ```python
      from monnify import transaction
      params = {
              "amount": 100.00,
              "customerName": "Test User",
              "customerEmail": "test@user.com",
              "paymentReference": "123456",
              "paymentDescription": "Test transaction",
              "currencyCode": "USD",
              "contractCode": "123456",
              "redirectUrl": "https://example.com/redirect",
              "paymentMethods": ["CARD", "ACCOUNT_TRANSFER"],
          }

      initiate_transaction = transaction.initiate(**params)

      ```

  - successful response

        ```json

        {
            "requestSuccessful": true,
            "responseMessage": "success",
            "responseCode": "0",
            "responseBody": {
                "transactionReference": "MNFY|20190915200044|000090",
                "paymentReference": "1568577644707",
                "merchantName": "Test Limited",
                "apiKey": "MK_TEST_VR7J3UAACH",
                "enabledPaymentMethod": [
                    "ACCOUNT_TRANSFER",
                    "CARD"
                ],
                "checkoutUrl": "https://sandbox.sdk.monnify.com/checkout/MNFY|20190915200044|000090"
            }

        }

        ```

        - failed response

        ```json
        {
            "requestSuccessful": false,
            "responseMessage": "Duplicate payment reference",
            "responseCode": "99"
        }

        {
            "requestSuccessful": false,
            "responseMessage": "Could not find specified contract",
            "responseCode": "99"
        }

        {
            "requestSuccessful": false,
            "responseMessage": "Unknown sub account code MFY_SUB_32216539305.",
            "responseCode": "99"  
        }

        ```

#### Customer
