#!/usr/local/bin/python

import os
from pathlib import Path

from dotenv import load_dotenv


env_path = Path("../app") / ".env"
load_dotenv(dotenv_path=env_path)

import django_conf

from auth.models import User

User.register(email="contact@gamersplane.com", username="Keleth", password="test1234")
