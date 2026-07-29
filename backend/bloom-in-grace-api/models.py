from datetime import datetime

from database import db


class Purchase(db.Model):
    __tablename__ = "purchases"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    receipt_number = db.Column(
        db.String(50),
        unique=True,
        nullable=False,
        index=True
    )

    payment_provider = db.Column(
        db.String(50),
        nullable=False
    )

    provider_order_id = db.Column(
        db.String(150),
        unique=True,
        nullable=False,
        index=True
    )

    customer_name = db.Column(
        db.String(255),
        nullable=False
    )

    customer_email = db.Column(
        db.String(255),
        nullable=False
    )

    product_slug = db.Column(
        db.String(100),
        nullable=False
    )

    amount_paid = db.Column(
        db.Float,
        nullable=False
    )

    currency = db.Column(
        db.String(10),
        nullable=False,
        default="USD"
    )

    download_token = db.Column(
        db.String(120),
        unique=True,
        nullable=False,
        index=True
    )

    payment_status = db.Column(
        db.String(30),
        nullable=False,
        default="PAID"
    )

    purchase_date = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    token_expires = db.Column(
        db.DateTime,
        nullable=False
    )

    download_count = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    max_downloads = db.Column(
        db.Integer,
        nullable=False,
        default=5
    )

    @property
    def downloads_remaining(self):

        return max(
            self.max_downloads - self.download_count,
            0
        )

    def to_dict(self):

        return {

            "id": self.id,

            "receipt_number": self.receipt_number,

            "payment_provider": self.payment_provider,

            "provider_order_id": self.provider_order_id,

            "customer_name": self.customer_name,

            "customer_email": self.customer_email,

            "product_slug": self.product_slug,

            "amount_paid": self.amount_paid,

            "currency": self.currency,

            "download_token": self.download_token,

            "payment_status": self.payment_status,

            "purchase_date": self.purchase_date.isoformat()
            if self.purchase_date
            else None,

            "token_expires": self.token_expires.isoformat()
            if self.token_expires
            else None,

            "download_count": self.download_count,

            "max_downloads": self.max_downloads,

            "downloads_remaining": self.downloads_remaining

        }

    def __repr__(self):

        return (

            f"<Purchase "

            f"{self.receipt_number} "

            f"{self.customer_email}>"

        )