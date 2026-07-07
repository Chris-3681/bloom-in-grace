import os

from flask import Flask
from flask_cors import CORS
import os
from database import init_db, db
from models import Purchase
from dotenv import load_dotenv

from routes.products import products_bp
from routes.downloads import downloads_bp
from routes.payments import payments_bp

load_dotenv()
print(os.getenv("DATABASE_URL"))

app = Flask(__name__)
init_db(app)

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

app.register_blueprint(products_bp)
app.register_blueprint(downloads_bp)
app.register_blueprint(payments_bp)


@app.route("/")
def home():
    return {
        "message": "Bloom in Grace API is running"
    }

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)