from datetime import datetime

from database import db


class Purchase(db.Model):
    __tablename__ = "purchases"

    id = db.Column(db.Integer, primary_key=True)

    customer_email = db.Column(
        db.String(255),
        nullable=False
    )

    paypal_email = db.Column(
        db.String(255)
    )

    product_slug = db.Column(
        db.String(100),
        nullable=False
    )

    paypal_order_id = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )
    download_token = db.Column(
    db.String(100),
    unique=True,
    nullable=False
)

    payment_status = db.Column(
        db.String(30),
        default="COMPLETED"
    )

    purchase_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
    