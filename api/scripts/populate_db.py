#!/usr/local/bin/python

import sys
from pathlib import Path

from dotenv import load_dotenv

code_path = Path("../")
sys.path.append(code_path / "/src")
load_dotenv(dotenv_path=code_path / ".env")


import django

django.setup()

from users import functions

user = functions.register_user(
    email="contact@gamersplane.com", username="Keleth", password="test1234"
)
user.activate()
