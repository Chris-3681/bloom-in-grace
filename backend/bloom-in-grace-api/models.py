from datetime import datetime

from database import db


class Purchase(db.Model):
    __tablename__ = "purchases"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    customer_email = db.Column(
        db.String(255),
        nullable=False
    )

    paypal_email = db.Column(
        db.String(255),
        nullable=True
    )

    product_slug = db.Column(
        db.String(100),
        nullable=False
    )

    paypal_order_id = db.Column(
        db.String(100),
        unique=True,
        nullable=False,
        index=True
    )

    download_token = db.Column(
        db.String(100),
        unique=True,
        nullable=False,
        index=True
    )

    payment_status = db.Column(
        db.String(30),
        nullable=False,
        default="COMPLETED"
    )

    purchase_date = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    # --------------------------------------------------
    # Download Security
    # --------------------------------------------------

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

    def to_dict(self):

        return {
            "id": self.id,
            "customer_email": self.customer_email,
            "paypal_email": self.paypal_email,
            "product_slug": self.product_slug,
            "paypal_order_id": self.paypal_order_id,
            "download_token": self.download_token,
            "payment_status": self.payment_status,
            "purchase_date": self.purchase_date.isoformat() if self.purchase_date else None,
            "token_expires": self.token_expires.isoformat() if self.token_expires else None,
            "download_count": self.download_count,
            "max_downloads": self.max_downloads
        }

    def __repr__(self):

        return (
            f"<Purchase "
            f"id={self.id}, "
            f"email={self.customer_email}, "
            f"product={self.product_slug}>"
        )