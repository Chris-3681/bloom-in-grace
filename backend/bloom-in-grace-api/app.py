import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from database import init_db, db

from routes.products import products_bp
from routes.downloads import downloads_bp
from routes.payments import payments_bp

load_dotenv()


def create_app():

    app = Flask(__name__)

    # --------------------------------------------------
    # Database
    # --------------------------------------------------

    init_db(app)

    # --------------------------------------------------
    # Mail
    # --------------------------------------------------

    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 587
    app.config["MAIL_USE_TLS"] = True
    app.config["MAIL_USE_SSL"] = False

    app.config["MAIL_USERNAME"] = os.getenv("GMAIL_EMAIL")
    app.config["MAIL_PASSWORD"] = os.getenv("GMAIL_APP_PASSWORD")

    app.config["MAIL_DEFAULT_SENDER"] = (
        "Bloom in Grace",
        os.getenv("GMAIL_EMAIL")
    )



    # --------------------------------------------------
    # CORS
    # --------------------------------------------------

    FRONTEND_URL = os.getenv(
        "FRONTEND_URL",
        "http://localhost:5173"
    )

    CORS(
        app,
        resources={
            r"/*": {
                "origins": FRONTEND_URL
            }
        }
    )

    # --------------------------------------------------
    # Routes
    # --------------------------------------------------

    app.register_blueprint(products_bp)
    app.register_blueprint(downloads_bp)
    app.register_blueprint(payments_bp)

    @app.route("/")
    def home():

        return {
            "message": "Bloom in Grace API running."
        }

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)