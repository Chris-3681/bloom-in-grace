from flask import Blueprint, jsonify, request

from database import db
from models import Purchase
from services.token_service import generate_token

from services.paypal_service import (
    get_access_token,
    create_order,
    capture_order
)

from data.products import PRODUCTS

payments_bp = Blueprint("payments", __name__)


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


@payments_bp.route("/create-paypal-order", methods=["POST"])
def create_paypal_order():

    print("========== CREATE ORDER HIT ==========")

    try:

        data = request.get_json()

        print("Request Data:", data)

        slug = data.get("slug")

        product = next(
            (p for p in PRODUCTS if p["slug"] == slug),
            None
        )

        print("Product:", product)

        if not product:
            return jsonify({
                "error": "Product not found"
            }), 404

        order = create_order(product)

        print("PayPal Order Created:", order)

        return jsonify(order)

    except Exception as e:

        print("CREATE ORDER ERROR:", str(e))

        return jsonify({
            "error": str(e)
        }), 500


@payments_bp.route("/capture-paypal-order", methods=["POST"])
def capture_paypal_order():

    data = request.get_json()

    order_id = data.get("orderID")
    slug = data.get("slug")
    customer_email = data.get("email")

    if not order_id:
        return jsonify({
            "error": "Missing order ID"
        }), 400

    if not slug:
        return jsonify({
            "error": "Missing product slug"
        }), 400

    if not customer_email:
        return jsonify({
            "error": "Missing customer email"
        }), 400

    try:

        result = capture_order(order_id)

        if result.get("status") != "COMPLETED":
            return jsonify({
                "success": False,
                "message": "Payment not completed."
            }), 400

        payer = result.get("payer")
        paypal_email = None

        if payer:
            paypal_email = payer.get("email_address")

        existing = Purchase.query.filter_by(
            paypal_order_id=order_id
        ).first()

        if existing:

            token = generate_token(
                existing.customer_email,
                existing.product_slug
            )

            return jsonify({
                "success": True,
                "message": "Purchase already recorded.",
                "token": token
            })

        purchase = Purchase(
            customer_email=customer_email,
            paypal_email=paypal_email,
            product_slug=slug,
            paypal_order_id=order_id,
            payment_status="COMPLETED"
        )

        db.session.add(purchase)
        db.session.commit()

        token = generate_token(
            customer_email,
            slug
        )

        return jsonify({
            "success": True,
            "message": "Purchase saved successfully.",
            "token": token
        })

    except Exception as e:

        db.session.rollback()

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500