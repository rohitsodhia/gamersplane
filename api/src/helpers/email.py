import os, smtplib, ssl

from email.message import EmailMessage
from email.headerregistry import Address


uri = os.getenv("EMAIL_URI")
port = os.getenv("EMAIL_PORT")
login = os.getenv("EMAIL_LOGIN")
password = os.getenv("EMAIL_PASSWORD")

context = ssl.create_default_context()


def email(to, subject, content):
    email = EmailMessage()
    email["From"] = Address(
        display_name="No Reply (Gamers' Plane)",
        username="no-reply",
        domain="gamersplane.com",
    )
    email["To"] = to
    email["Subject"] = subject
    email.set_content(content, subtype="html")

    with smtplib.SMTP_SSL(uri, port, context=context) as server:
        server.login(login, password)
        server.sendmail(email)
