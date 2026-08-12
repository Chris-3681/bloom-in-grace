from flask import Blueprint, jsonify, request
from datetime import datetime, timedelta
import secrets
import traceback

from database import db
from models import Purchase
from threading import Thread

from services.lemonsqueezy_service import (
    create_checkout,
    verify_signature
)

from services.email_service import (
    send_customer_receipt,
    send_admin_notification
)

from data.products import PRODUCTS

payments_bp = Blueprint(
    "payments",
    __name__
)


# ==========================================================
# HELPERS
# ==========================================================

def get_product(slug):

    return next(

        (
            product
            for product in PRODUCTS
            if product["slug"] == slug
        ),

        None

    )


def generate_receipt_number():

    today = datetime.utcnow().strftime("%Y%m%d")

    latest = (

        Purchase.query
        .order_by(Purchase.id.desc())
        .first()

    )

    next_id = latest.id + 1 if latest else 1

    return f"BG-{today}-{next_id:06d}"


# ==========================================================
# CREATE LEMON SQUEEZY CHECKOUT
# ==========================================================

@payments_bp.route(
    "/create-checkout",
    methods=["POST"]
)
def create_lemon_checkout():

    try:

        data = request.get_json()

        slug = data.get("slug")
        customer_name = data.get("name", "").strip()
        customer_email = data.get("email", "").strip()

        if not slug:

            return jsonify({

                "success": False,

                "error": "Missing product slug."

            }), 400

        if not customer_name:

            return jsonify({

                "success": False,

                "error": "Missing customer name."

            }), 400

        if not customer_email:

            return jsonify({

                "success": False,

                "error": "Missing customer email."

            }), 400

        product = get_product(slug)

        if not product:

            return jsonify({

                "success": False,

                "error": "Product not found."

            }), 404

        checkout = create_checkout(
            product,
            customer_name,
            customer_email
        )

        checkout_url = checkout["data"]["attributes"]["url"]

        return jsonify({

            "success": True,

            "checkout_url": checkout_url

        })

    except Exception as e:

        traceback.print_exc()

        return jsonify({

            "success": False,

            "error": str(e)

        }), 500


# ==========================================================
# LEMON SQUEEZY WEBHOOK
# ==========================================================

@payments_bp.route("/api/lemonsqueezy/webhook", methods=["POST"])
def lemonsqueezy_webhook():

    print("WEBHOOK RECEIVED")

    try:

        raw_body = request.data

        signature = request.headers.get(
            "X-Signature",
            ""
        )

        if not verify_signature(
            raw_body,
            signature
        ):

            return jsonify({

                "success": False,

                "error": "Invalid signature."

            }), 403

        payload = request.get_json()

        print(
            "Slug =",
            payload["meta"]["custom_data"]["slug"]
        )

        event = payload["meta"]["event_name"]

        if event != "order_created":

            return jsonify({

                "success": True,

                "message": "Ignored."

            }), 200

        order = payload["data"]["attributes"]
        
        customer_name = order.get("user_name")

        if not customer_name or customer_name == "Bloom in Grace":
            customer_name = "Customer"

        customer_email = order.get(
            "user_email"
        )

        provider_order_id = str(
            payload["data"]["id"]
        )

        amount_paid = float(
            order["total"]
        ) / 100

        currency = order["currency"]

        slug = payload["meta"]["custom_data"]["slug"]

        product = get_product(slug)

        if not product:

            return jsonify({

                "success": False,

                "error": "Unknown product."

            }), 404

        existing = Purchase.query.filter_by(

            provider_order_id=provider_order_id

        ).first()

        if existing:

            return jsonify({

                "success": True,

                "message": "Already processed."

            }), 200

        receipt_number = generate_receipt_number()

        download_token = secrets.token_urlsafe(32)

        purchase = Purchase(

            receipt_number=receipt_number,

            payment_provider="Lemon Squeezy",

            provider_order_id=provider_order_id,

            customer_name=customer_name,

            customer_email=customer_email,

            product_slug=slug,

            amount_paid=amount_paid,

            currency=currency,

            download_token=download_token,

            payment_status="COMPLETED",

            purchase_date=datetime.utcnow(),

            token_expires=datetime.utcnow() + timedelta(days=7),

            download_count=0,

            max_downloads=5

        )

        db.session.add(purchase)

        db.session.commit()

        download_url = (

            request.host_url.rstrip("/")
            + "/download/"
            + download_token

        )

        Thread(

            target=send_customer_receipt,

            kwargs={

                "customer_email": customer_email,

                "customer_name": customer_name,

                "receipt_number": receipt_number,

                "product_name": product["name"],

                "amount": amount_paid,

                "currency": currency,

                "purchase_date": purchase.purchase_date,

                "download_url": download_url,

                "downloads_remaining": purchase.max_downloads,

                "expiry_date": purchase.token_expires

            },

            daemon=True

        ).start()

        Thread(

            target=send_admin_notification,

            kwargs={

                "receipt_number": receipt_number,

                "customer_name": customer_name,

                "customer_email": customer_email,

                "payment_provider": "Lemon Squeezy",

                "provider_order_id": provider_order_id,

                "product_name": product["name"],

                "amount": amount_paid,

                "currency": currency,

                "purchase_date": purchase.purchase_date

            },

            daemon=True

        ).start()

        return jsonify({

            "success": True,

            "message": "Webhook processed."

        }), 200

    except Exception as e:

        db.session.rollback()

        traceback.print_exc()

        return jsonify({

            "success": False,

            "error": str(e)

        }), 500