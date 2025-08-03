#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Debug: Check if DATABASE_URL is set
echo "Checking DATABASE_URL..."
if [ -n "$DATABASE_URL" ]; then
    echo "DATABASE_URL is set: ${DATABASE_URL:0:20}..."
else
    echo "DATABASE_URL is NOT set"
    echo "Available environment variables:"
    env | grep -E "(DATABASE|SECRET|DEBUG)" || echo "No relevant env vars found"
fi

# Run database migrations (only if DATABASE_URL is set)
if [ -n "$DATABASE_URL" ]; then
    echo "Running database migrations..."
    python manage.py migrate --verbosity=2
    echo "Migrations completed successfully"
else
    echo "DATABASE_URL not set, skipping migrations"
    exit 1
fi

# Create superuser with predefined credentials (only after migrations)
if [ -n "$DATABASE_URL" ]; then
    echo "Creating superuser..."
    python manage.py create_superuser
    echo "Superuser creation completed"
else
    echo "DATABASE_URL not set, skipping superuser creation"
fi 