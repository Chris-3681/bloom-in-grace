import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

ADMIN_EMAIL = os.getenv(
    "ADMIN_EMAIL",
    "bloomingrace.org@gmail.com"
)


# ==========================================================
# SEND EMAIL
# ==========================================================

def send_email(
    recipient,
    subject,
    html
):

    print("========== EMAIL DEBUG ==========")
    print("SMTP SERVER:", SMTP_SERVER)
    print("SMTP PORT:", SMTP_PORT)
    print("SMTP EMAIL:", SMTP_EMAIL)
    print("RECIPIENT:", recipient)

    message = MIMEMultipart("alternative")

    message["Subject"] = subject
    message["From"] = SMTP_EMAIL
    message["To"] = recipient

    message.attach(
        MIMEText(
            html,
            "html"
        )
    )

    try:

        server = smtplib.SMTP(
            SMTP_SERVER,
            int(SMTP_PORT),
            timeout=30
        )

        print("SMTP CONNECTED")

        server.ehlo()

        server.starttls()

        print("TLS STARTED")

        server.ehlo()

        server.login(
            SMTP_EMAIL,
            SMTP_PASSWORD
        )

        print("SMTP LOGIN SUCCESS")

        server.sendmail(
            SMTP_EMAIL,
            recipient,
            message.as_string()
        )

        print("EMAIL SENT SUCCESSFULLY")

        server.quit()

        print("SMTP CONNECTION CLOSED")

    except Exception as e:

        print("EMAIL ERROR:", str(e))

        raise
def send_customer_receipt(

    customer_email,
    customer_name,
    receipt_number,
    product_name,
    amount,
    currency,
    purchase_date,
    download_url,
    downloads_remaining,
    expiry_date

):

    html = f"""

    <html>

    <body style="margin:0;padding:40px;background:#F8F5F1;font-family:Arial,sans-serif;color:#333;">

        <div style="max-width:650px;margin:auto;background:#FFFFFF;border:1px solid #E8E2DA;border-radius:12px;overflow:hidden;">

            <div style="background:#7C5A3A;padding:30px;text-align:center;">

                <h1 style="margin:0;color:white;">
                    Bloom in Grace
                </h1>

                <p style="margin-top:10px;color:#F4EBDD;">
                    Digital Christian Resources
                </p>

            </div>

            <div style="padding:35px;">

                <h2 style="margin-top:0;color:#7C5A3A;">
                    Thank you for your purchase ❤️
                </h2>

                <p>
                    Hi <strong>{customer_name}</strong>,
                </p>

                <p>

                    Thank you for purchasing
                    <strong>{product_name}</strong>.

                    Your payment has been received successfully, and your digital product is now ready to download.

                </p>

                <hr style="border:none;border-top:1px solid #EEE;margin:30px 0;">

                <h3 style="color:#7C5A3A;">
                    Receipt Details
                </h3>

                <table style="width:100%;border-collapse:collapse;">

                    <tr>

                        <td style="padding:10px 0;">
                            <strong>Receipt #</strong>
                        </td>

                        <td style="padding:10px 0;">
                            {receipt_number}
                        </td>

                    </tr>

                    <tr>

                        <td style="padding:10px 0;">
                            <strong>Product</strong>
                        </td>

                        <td style="padding:10px 0;">
                            {product_name}
                        </td>

                    </tr>

                    <tr>

                        <td style="padding:10px 0;">
                            <strong>Amount Paid</strong>
                        </td>

                        <td style="padding:10px 0;">
                            {currency} {amount}
                        </td>

                    </tr>

                    <tr>

                        <td style="padding:10px 0;">
                            <strong>Purchase Date</strong>
                        </td>

                        <td style="padding:10px 0;">
                            {purchase_date.strftime("%d %B %Y %H:%M UTC")}
                        </td>

                    </tr>

                    <tr>

                        <td style="padding:10px 0;">
                            <strong>Downloads Remaining</strong>
                        </td>

                        <td style="padding:10px 0;">
                            {downloads_remaining}
                        </td>

                    </tr>

                    <tr>

                        <td style="padding:10px 0;">
                            <strong>Link Expires</strong>
                        </td>

                        <td style="padding:10px 0;">
                            {expiry_date.strftime("%d %B %Y")}
                        </td>

                    </tr>

                </table>

                <div style="text-align:center;margin:40px 0;">

                    <a
                        href="{download_url}"
                        style="background:#C9A66B;color:white;padding:16px 28px;text-decoration:none;border-radius:8px;font-weight:bold;display:inline-block;"
                    >

                        Download Your Product

                    </a>

                </div>
                                <p>

                    This download link can be used

                    <strong>{downloads_remaining}</strong>

                    more time(s) before

                    <strong>{expiry_date.strftime("%d %B %Y")}</strong>.

                </p>

                <p>

                    If you experience any issues accessing your purchase,
                    simply reply to this email and we'll be happy to help.

                </p>

                <hr style="border:none;border-top:1px solid #EEE;margin:30px 0;">

                <p style="font-size:13px;color:#777;text-align:center;line-height:1.6;">

                    Thank you for supporting Bloom in Grace.
                    We pray these resources encourage you to grow in faith every day.

                </p>

            </div>

        </div>

    </body>

    </html>

    """

    send_email(

        customer_email,

        f"Your Bloom in Grace Receipt ({receipt_number})",

        html

    )


# ==========================================================
# ADMIN NOTIFICATION
# ==========================================================

def send_admin_notification(

    receipt_number,
    customer_name,
    customer_email,
    payment_provider,
    provider_order_id,
    product_name,
    amount,
    currency,
    purchase_date

):

    html = f"""

    <html>

    <body style="margin:0;padding:40px;background:#F7F7F7;font-family:Arial,sans-serif;">

        <div style="max-width:650px;margin:auto;background:white;border:1px solid #DDD;border-radius:10px;padding:35px;">

        <h2 style="margin-top:0;color:#7C5A3A;">

            🎉 New Bloom in Grace Order

            </h2>

            <p>

                A new purchase has been completed successfully.

            </p>

            <hr style="border:none;border-top:1px solid #EEE;margin:25px 0;">

            <table style="width:100%;border-collapse:collapse;">

                <tr>

                    <td style="padding:10px 0;">
                        <strong>Receipt</strong>
                    </td>

                    <td style="padding:10px 0;">
                        {receipt_number}
                    </td>

                </tr>

                <tr>

                    <td style="padding:10px 0;">
                        <strong>Customer</strong>
                    </td>

                    <td style="padding:10px 0;">
                        {customer_name}
                    </td>

                </tr>

                <tr>

                    <td style="padding:10px 0;">
                        <strong>Email</strong>
                    </td>

                    <td style="padding:10px 0;">
                        {customer_email}
                    </td>

                </tr>

                <tr>

                    <td style="padding:10px 0;">
                        <strong>Payment Provider</strong>
                    </td>

                    <td style="padding:10px 0;">
                        {payment_provider}
                    </td>

                </tr>

                <tr>

                    <td style="padding:10px 0;">
                        <strong>Provider Order ID</strong>
                    </td>

                    <td style="padding:10px 0;">
                        {provider_order_id}
                    </td>

                </tr>

                <tr>

                    <td style="padding:10px 0;">
                        <strong>Product</strong>
                    </td>

                    <td style="padding:10px 0;">
                        {product_name}
                    </td>

                </tr>

                <tr>

                    <td style="padding:10px 0;">
                        <strong>Amount</strong>
                    </td>

                    <td style="padding:10px 0;">
                        {currency} {amount}
                    </td>

                </tr>

                <tr>

                    <td style="padding:10px 0;">
                        <strong>Purchase Date</strong>
                    </td>

                    <td style="padding:10px 0;">
                        {purchase_date.strftime("%d %B %Y %H:%M UTC")}
                    </td>

                </tr>

            </table>

            <hr style="border:none;border-top:1px solid #EEE;margin:25px 0;">

            <p style="font-size:13px;color:#666;">

                This notification was generated automatically by the
                Bloom in Grace payment system.

            </p>

        </div>

    </body>

    </html>

    """

    send_email(

        ADMIN_EMAIL,

        f"New Order • {receipt_number}",

        html

    )
    send_email(

        ADMIN_EMAIL,

        f"New Order • {receipt_number}",

        html

    )