#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run database migrations (only if DATABASE_URL is set)
if [ -n "$DATABASE_URL" ]; then
    echo "Running database migrations..."
    python manage.py migrate
else
    echo "DATABASE_URL not set, skipping migrations"
fi

# Create superuser if it doesn't exist (optional)
# python manage.py createsuperuser --noinput --username admin --email admin@example.com || true 