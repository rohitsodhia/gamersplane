#!/bin/sh

echo "Waiting for MySQL..."

while nc -z $MYSQL_HOST $MYSQL_PORT; do
    sleep 1
    echo "Waiting"
done

echo "Database started"

python manage.py flush --no-input
python manage.py migrate

exec "$@"