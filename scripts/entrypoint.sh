#!/bin/bash

set -e

server_port=8000

while ! nc -z ${DB_HOST} ${DB_PORT}; do
  echo "Waiting for PostgreSQL..."
  sleep 1
done

echo "✅ Postgres Database Started Successfully ($DB_HOST:$DB_PORT)"

if [ $1 == "prod" ] ; then
  uv run app/manage.py makemigrations
  uv run app/manage.py migrate
  server_port=80
fi

uv run app/manage.py runserver 0.0.0.0:$server_port