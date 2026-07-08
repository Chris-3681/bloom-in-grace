from flask import Blueprint, jsonify, request
from datetime import datetime, timedelta
import secrets
import traceback

from database import db
from models import Purchase

from services.paypal_service import (
    get_access_token,
    create_order,
    capture_order
)

from data.products import PRODUCTS

payments_bp = Blueprint("payments", __name__)


# ==========================================================
# PAYPAL TEST
# ==========================================================
@payments_bp.route("/paypal/test", methods=["GET"])
def paypal_test():

    try:

        token = get_access_token()

        return jsonify({
            "success": True,
            "token_received": bool(token)
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# ==========================================================
# DATABASE TEST
# ==========================================================
@payments_bp.route("/db-test", methods=["GET"])
def db_test():

    try:

        db.session.execute(db.text("SELECT 1"))

        return jsonify({
            "success": True
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# ==========================================================
# CREATE PAYPAL ORDER
# ==========================================================
@payments_bp.route("/create-paypal-order", methods=["POST"])
def create_paypal_order():

    print("\n========== CREATE PAYPAL ORDER ==========")

    try:

        data = request.get_json()

        slug = data.get("slug")

        if not slug:

            return jsonify({
                "error": "Missing product slug."
            }), 400

        product = next(
            (
                p
                for p in PRODUCTS
                if p["slug"] == slug
            ),
            None
        )

        if not product:

            return jsonify({
                "error": "Product not found."
            }), 404

        print("Product:", product["name"])

        order = create_order(product)

        print("PayPal Order:", order["id"])

        return jsonify(order)

    except Exception as e:

        print("\nCREATE ORDER ERROR")
        traceback.print_exc()

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# ==========================================================
# CAPTURE PAYPAL ORDER
# ==========================================================
@payments_bp.route("/capture-paypal-order", methods=["POST"])
def capture_paypal_order():

    try:

        data = request.get_json()

        order_id = data.get("orderID")
        slug = data.get("slug")
        customer_email = data.get("email")

        if not order_id:

            return jsonify({
                "error": "Missing PayPal Order ID."
            }), 400

        if not slug:

            return jsonify({
                "error": "Missing product slug."
            }), 400

        if not customer_email:

            return jsonify({
                "error": "Missing customer email."
            }), 400

        # --------------------------------------
        # Capture payment from PayPal
        # --------------------------------------

        result = capture_order(order_id)

        if result.get("status") != "COMPLETED":

            return jsonify({
                "success": False,
                "message": "Payment not completed."
            }), 400

        payer = result.get("payer", {})

        paypal_email = payer.get("email_address")

        # --------------------------------------
        # Check if purchase already exists
        # --------------------------------------

        existing = Purchase.query.filter_by(
            paypal_order_id=order_id
        ).first()

        if existing:

            print("Purchase already exists.")

            return jsonify({
                "success": True,
                "download_token": existing.download_token
            })

        # --------------------------------------
        # Generate secure token
        # --------------------------------------

        download_token = secrets.token_urlsafe(32)

        purchase = Purchase(

            customer_email=customer_email,

            paypal_email=paypal_email,

            product_slug=slug,

            paypal_order_id=order_id,

            download_token=download_token,

            payment_status="COMPLETED",

            token_expires=datetime.utcnow() + timedelta(days=7),

            download_count=0,

            max_downloads=5

        )

        db.session.add(purchase)

        db.session.commit()

        print("Purchase saved.")

        return jsonify({

            "success": True,

            "download_token": download_token

        })

    except Exception as e:

        db.session.rollback()

        print("\nCAPTURE ORDER ERROR")
        traceback.print_exc()

        return jsonify({

            "success": False,

            "error": str(e)

        }), 500