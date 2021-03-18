#!/usr/local/bin/python

import os
from pathlib import Path

from dotenv import load_dotenv
from MySQLdb import _mysql as mysql

root_path = Path("../")
load_dotenv(dotenv_path=root_path / ".env")

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

db = mysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE)

db.query("DROP DATABASE gamersplane;")
db.query("CREATE DATABASE gamersplane;")

print("Dropped and recreated database\n")
