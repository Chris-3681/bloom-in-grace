from flask import Blueprint, jsonify
from data import products


products_bp = Blueprint("products", __name__)

PRODUCTS = [
    {
        "id": 1,
        "slug": "bible-study-workbook",
        "name": "30-Day Daily Bible Study Method Pages",
        "description": "A guided workbook to help women study Scripture consistently and deeply.",
        "price": 9.99,
        "type": "single",
        "category": "bible-study",
        "files": [
            "bible-study-workbook.pdf"
        ],
        "is_active": True
    },

    {
        "id": 2,
        "slug": "gratitude-journal",
        "name": "30-Day Gratitude Journal for Women",
        "description": "Develop a habit of thankfulness through daily guided reflections.",
        "price": 7.99,
        "type": "single",
        "category": "gratitude",
        "files": [
            "gratitude-journal.pdf"
        ],
        "is_active": True
    },

    {
        "id": 3,
        "slug": "scripture-memory-pages",
        "name": "30-Day Scripture Memory Pages",
        "description": "Build a lasting habit of hiding God's Word in your heart through guided memorization and reflection.",
        "price": 6.99,
        "type": "single",
        "category": "scripture-memory",
        "files": [
            "scripture-memory-pages.pdf"
        ],
        "is_active": True
    },

    {
        "id": 4,
        "slug": "prayer-tracker",
        "name": "30-Day Prayer Tracker",
        "description": "Track prayers, answered prayers, and spiritual growth over 30 days.",
        "price": 4.99,
        "type": "single",
        "category": "prayer",
        "files": [
            "prayer-tracker.pdf"
        ],
        "is_active": True
    }
]

@products_bp.route("/products", methods=["GET"])
def get_products():
    return jsonify(PRODUCTS)