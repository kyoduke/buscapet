#!/bin/bash

set -e

while ! nc -z ${DB_HOST} ${DB_PORT}; do
  echo "Waiting for PostgreSQL..."
  sleep 1
done

echo "✅ Postgres Database Started Successfully ($DB_HOST:$DB_PORT)"

uv run app/manage.py makemigrations
uv run app/manage.py migrate

uv run app/manage.py runserver 0.0.0.0:8000 # TODO: change run server to gunicorn