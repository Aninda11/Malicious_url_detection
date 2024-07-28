import smtplib
from app_vars import Sender, Recipient
from email.message import EmailMessage


def send_notification(url):
    msg = EmailMessage()
    msg.set_content(f"Malicious URL detected: {url}")

    msg['Subject'] = 'Malicious URL Detected'
    msg['From'] = Sender
    msg['To'] = Recipient

    # Set up SMTP server and send email
    with smtplib.SMTP('smtp.example.com', 587) as smtp:
        smtp.starttls()
        smtp.login('username', 'password')
        smtp.send_message(msg)