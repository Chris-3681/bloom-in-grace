from flask import Blueprint, jsonify
from data.products import PRODUCTS

products_bp = Blueprint("products", __name__)


@products_bp.route("/products", methods=["GET"])
def get_products():
    return jsonify(PRODUCTS)


@products_bp.route("/products/<slug>", methods=["GET"])
def get_product(slug):
    product = next(
        (product for product in PRODUCTS if product["slug"] == slug),
        None
    )

    if product:
        return jsonify(product)

    return jsonify({
        "error": "Product not found"
    }), 404