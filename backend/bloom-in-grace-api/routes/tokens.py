from flask import Blueprint, jsonify
from services.token_service import generate_token

tokens_bp = Blueprint("tokens", __name__)


@tokens_bp.route("/generate-token/<slug>", methods=["GET"])
def create_token(slug):

    token = generate_token(slug)

    return jsonify({
        "token": token
    })