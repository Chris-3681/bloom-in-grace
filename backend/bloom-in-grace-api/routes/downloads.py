from flask import Blueprint, send_from_directory, jsonify
from datetime import datetime
import os

from database import db
from models import Purchase
from data.products import PRODUCTS

downloads_bp = Blueprint("downloads", __name__)

PRODUCTS_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "products"
)


@downloads_bp.route("/download/<token>", methods=["GET"])
def download_product(token):

    # ----------------------------------------
    # Find purchase using download token
    # ----------------------------------------
    purchase = Purchase.query.filter_by(
        download_token=token
    ).first()

    if not purchase:

        return jsonify({
            "success": False,
            "error": "Invalid download token."
        }), 403

    # ----------------------------------------
    # Check if payment is completed
    # ----------------------------------------
    if purchase.payment_status != "COMPLETED":

        return jsonify({
            "success": False,
            "error": "Payment not completed."
        }), 403

    # ----------------------------------------
    # Check expiry
    # ----------------------------------------
    if purchase.token_expires < datetime.utcnow():

        return jsonify({
            "success": False,
            "error": "Your download link has expired."
        }), 403

    # ----------------------------------------
    # Check download limit
    # ----------------------------------------
    if purchase.download_count >= purchase.max_downloads:

        return jsonify({
            "success": False,
            "error": "Maximum download limit reached."
        }), 403

    # ----------------------------------------
    # Find purchased product
    # ----------------------------------------
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

    # ----------------------------------------
    # Check product file exists
    # ----------------------------------------
    filename = product["files"][0]

    filepath = os.path.join(
        PRODUCTS_FOLDER,
        filename
    )

    if not os.path.exists(filepath):

        return jsonify({
            "success": False,
            "error": "Product file is missing on the server."
        }), 404

    # ----------------------------------------
    # Update download count
    # ----------------------------------------
    purchase.download_count += 1

    db.session.commit()

    print(
        f"Download #{purchase.download_count} "
        f"for {purchase.customer_email}"
    )

    # ----------------------------------------
    # Send file
    # ----------------------------------------
    return send_from_directory(
        PRODUCTS_FOLDER,
        filename,
        as_attachment=True
    )