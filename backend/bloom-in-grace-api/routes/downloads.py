from flask import Blueprint, send_from_directory, jsonify
from data.products import PRODUCTS
from models import Purchase
import os

downloads_bp = Blueprint("downloads", __name__)

PRODUCTS_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "products"
)


@downloads_bp.route("/download/<token>", methods=["GET"])
def download_product(token):

    purchase = Purchase.query.filter_by(
        download_token=token
    ).first()

    if not purchase:
        return jsonify({
            "error": "Invalid download token"
        }), 403

    product = next(
        (
            p for p in PRODUCTS
            if p["slug"] == purchase.product_slug
        ),
        None
    )

    if not product:
        return jsonify({
            "error": "Product not found"
        }), 404

    filename = product["files"][0]

    return send_from_directory(
        PRODUCTS_FOLDER,
        filename,
        as_attachment=True
    )