import os
import smtplib
import ssl

from jinja2 import FileSystemLoader, Environment

from email.message import EmailMessage
from email.headerregistry import Address

from envs import ROOT_DIR, ENVIRONMENT

uri = os.getenv("EMAIL_URI")
port = os.getenv("EMAIL_PORT")
login = os.getenv("EMAIL_LOGIN")
password = os.getenv("EMAIL_PASSWORD")

context = ssl.create_default_context()


def get_template(template, **kwargs):
    file_loader = FileSystemLoader(searchpath=ROOT_DIR)
    env = Environment(loader=file_loader)

    template = env.get_template(template)

    output = template.render(**kwargs)
    return output


def send_email(to, subject, content):
    if ENVIRONMENT == "dev":
        return

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
        server.send_message(email)
