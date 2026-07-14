import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID")
PAYPAL_SECRET = os.getenv("PAYPAL_SECRET")
PAYPAL_BASE_URL = os.getenv("PAYPAL_BASE_URL")

if not all([PAYPAL_CLIENT_ID, PAYPAL_SECRET, PAYPAL_BASE_URL]):
    raise RuntimeError("Missing PayPal environment variables.")


def get_access_token():

    print("\n========== PAYPAL ACCESS TOKEN ==========")
    print("Base URL:", PAYPAL_BASE_URL)

    response = requests.post(
        f"{PAYPAL_BASE_URL}/v1/oauth2/token",
        auth=(PAYPAL_CLIENT_ID, PAYPAL_SECRET),
        headers={
            "Accept": "application/json",
            "Accept-Language": "en_US",
        },
        data={
            "grant_type": "client_credentials"
        },
        timeout=30
    )

    print("Status:", response.status_code)
    print("Response:", response.text)

    response.raise_for_status()

    token = response.json()["access_token"]

    print("Access token acquired.")

    return token


def create_order(product):

    access_token = get_access_token()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Prefer": "return=representation"
    }

    body = {
        "intent": "CAPTURE",
        "purchase_units": [
            {
                "description": product["name"],
                "amount": {
                    "currency_code": "USD",
                    "value": f"{product['price']:.2f}"
                }
            }
        ],
        "application_context": {
            "shipping_preference": "NO_SHIPPING",
            "user_action": "PAY_NOW"
        }
    }

    print("\n========== CREATE PAYPAL ORDER ==========")
    print(json.dumps(body, indent=4))

    response = requests.post(
        f"{PAYPAL_BASE_URL}/v2/checkout/orders",
        headers=headers,
        json=body,
        timeout=30
    )

    print("\n========== PAYPAL RESPONSE ==========")
    print("Status:", response.status_code)
    print(response.text)

    if response.status_code >= 400:
        raise Exception(
            f"PayPal Error {response.status_code}\n{response.text}"
        )

    return response.json()


def capture_order(order_id):

    access_token = get_access_token()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Prefer": "return=representation"
    }

    print("\n========== CAPTURE ORDER ==========")
    print(order_id)

    response = requests.post(
        f"{PAYPAL_BASE_URL}/v2/checkout/orders/{order_id}/capture",
        headers=headers,
        timeout=30
    )

    print("\n========== CAPTURE RESPONSE ==========")
    print("Status:", response.status_code)
    print(response.text)

    if response.status_code >= 400:
        raise Exception(
            f"PayPal Capture Error {response.status_code}\n{response.text}"
        )

    return response.json()