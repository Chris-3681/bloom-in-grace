import os
import hmac
import hashlib
import requests

from dotenv import load_dotenv

load_dotenv()

LEMONSQUEEZY_API_KEY = os.getenv("LEMONSQUEEZY_API_KEY")
LEMONSQUEEZY_STORE_ID = os.getenv("LEMONSQUEEZY_STORE_ID")
LEMONSQUEEZY_VARIANT_ID = os.getenv("LEMONSQUEEZY_VARIANT_ID")
LEMONSQUEEZY_WEBHOOK_SECRET = os.getenv("LEMONSQUEEZY_WEBHOOK_SECRET")
FRONTEND_URL = os.getenv("FRONTEND_URL")


HEADERS = {
    "Accept": "application/vnd.api+json",
    "Content-Type": "application/vnd.api+json",
    "Authorization": f"Bearer {LEMONSQUEEZY_API_KEY}"
}


# ==========================================================
# CREATE CHECKOUT
# ==========================================================

def create_checkout(product):

    payload = {

        "data": {

            "type": "checkouts",

            "attributes": {

                "checkout_data": {

                    "custom": {

                        "slug": product["slug"]

                    }

                },

                "checkout_options": {

                    "embed": False,

                    "media": True,

                    "logo": True

                },

                "product_options": {

                    "enabled_variants": [

                        int(LEMONSQUEEZY_VARIANT_ID)

                    ],

                    "redirect_url": f"{FRONTEND_URL}/success"

                }

            },

            "relationships": {

                "store": {

                    "data": {

                        "type": "stores",

                        "id": str(LEMONSQUEEZY_STORE_ID)

                    }

                },

                "variant": {

                    "data": {

                        "type": "variants",

                        "id": str(LEMONSQUEEZY_VARIANT_ID)

                    }

                }

            }

        }

    }

    response = requests.post(

        "https://api.lemonsqueezy.com/v1/checkouts",

        headers=HEADERS,

        json=payload,

        timeout=30

    )

    response.raise_for_status()

    return response.json()


# ==========================================================
# VERIFY WEBHOOK
# ==========================================================

def verify_signature(raw_body, signature):

    digest = hmac.new(

        LEMONSQUEEZY_WEBHOOK_SECRET.encode(),

        raw_body,

        hashlib.sha256

    ).hexdigest()

    return hmac.compare_digest(

        digest,

        signature

    )