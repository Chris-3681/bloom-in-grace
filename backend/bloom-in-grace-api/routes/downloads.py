from flask import Blueprint, send_from_directory, jsonify
from data.products import PRODUCTS
from services.token_service import validate_token
import os

downloads_bp = Blueprint("downloads", __name__)

PRODUCTS_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "products"
)


@downloads_bp.route("/download/<token>", methods=["GET"])
def download_product(token):

    slug = validate_token(token)

    if not slug:
        return jsonify({
            "error": "Invalid download token"
        }), 403

    product = next(
        (p for p in PRODUCTS if p["slug"] == slug),
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