import os, pymysql

host = os.getenv("MYSQL_HOST")
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")
db = pymysql.connect(
    host=host,
    user=user,
    password=password,
    db=database,
    cursorclass=pymysql.cursors.DictCursor,
)
