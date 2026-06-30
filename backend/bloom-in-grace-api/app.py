from flask import Flask
from flask_cors import CORS

from routes.downloads import downloads_bp
from routes.products import products_bp
from routes.tokens import tokens_bp
from routes.payments import payments_bp

app = Flask(__name__)

CORS(
    app,
    resources={
        r"/*": {
            "origins": "http://localhost:5173"
        }
    }
)

app.register_blueprint(products_bp)
app.register_blueprint(downloads_bp)
app.register_blueprint(tokens_bp)
app.register_blueprint(payments_bp)

@app.route("/")
def home():
    return {
        "message": "Bloom in Grace API is running"
    }

if __name__ == "__main__":
    app.run(debug=True, port=5000)