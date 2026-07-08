from flask import Blueprint, jsonify, redirect
from datetime import datetime

from database import db
from models import Purchase
from data.products import PRODUCTS

downloads_bp = Blueprint("downloads", __name__)


@downloads_bp.route("/download/<token>", methods=["GET"])
def download_product(token):

    purchase = Purchase.query.filter_by(
        download_token=token
    ).first()

    if not purchase:

        return jsonify({
            "success": False,
            "error": "Invalid download token."
        }), 403

    if purchase.payment_status != "COMPLETED":

        return jsonify({
            "success": False,
            "error": "Payment not completed."
        }), 403

    if purchase.token_expires < datetime.utcnow():

        return jsonify({
            "success": False,
            "error": "Your download link has expired."
        }), 403

    if purchase.download_count >= purchase.max_downloads:

        return jsonify({
            "success": False,
            "error": "Maximum download limit reached."
        }), 403

    product = next(

        (
            p
            for p in PRODUCTS
            if p["slug"] == purchase.product_slug
        ),

        None

    )

    if not product:

        return jsonify({
            "success": False,
            "error": "Product not found."
        }), 404

    purchase.download_count += 1

    db.session.commit()

    print(
        f"Download #{purchase.download_count} "
        f"for {purchase.customer_email}"
    )

    return redirect(
        product["download_url"]
    )