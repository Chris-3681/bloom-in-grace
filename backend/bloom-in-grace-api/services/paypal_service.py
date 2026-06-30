import os
import requests
from dotenv import load_dotenv

load_dotenv()

PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID")
PAYPAL_SECRET = os.getenv("PAYPAL_SECRET")
PAYPAL_BASE_URL = os.getenv("PAYPAL_BASE_URL")

if not all([PAYPAL_CLIENT_ID, PAYPAL_SECRET, PAYPAL_BASE_URL]):
    raise RuntimeError(
        "Missing one or more PayPal environment variables."
    )


def get_access_token():

    response = requests.post(
        f"{PAYPAL_BASE_URL}/v1/oauth2/token",
        auth=(PAYPAL_CLIENT_ID, PAYPAL_SECRET),
        data={
            "grant_type": "client_credentials"
        },
        timeout=30
    )

    response.raise_for_status()

    return response.json()["access_token"]


def create_order(product):

    access_token = get_access_token()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    body = {
        "intent": "CAPTURE",
        "purchase_units": [
            {
                "description": product["name"],
                "amount": {
                    "currency_code": "USD",
                    "value": str(product["price"])
                }
            }
        ]
    }

    response = requests.post(
        f"{PAYPAL_BASE_URL}/v2/checkout/orders",
        headers=headers,
        json=body,
        timeout=30
    )

    response.raise_for_status()

    return response.json()


def capture_order(order_id):

    access_token = get_access_token()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.post(
        f"{PAYPAL_BASE_URL}/v2/checkout/orders/{order_id}/capture",
        headers=headers,
        timeout=30
    )

    response.raise_for_status()

    return response.json()