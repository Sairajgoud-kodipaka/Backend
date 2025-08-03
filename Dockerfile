FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Create necessary directories
RUN mkdir -p /app/media /app/staticfiles /app/logs

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE $PORT

# Create a startup script
RUN echo '#!/bin/bash\n\
set -e\n\
echo "🚀 Starting Django application..."\n\
echo "📊 Running database migrations..."\n\
python manage.py migrate --verbosity=2\n\
echo "👤 Creating superuser..."\n\
python manage.py create_superuser\n\
echo "🔧 Setting up demo data..."\n\
python setup_users.py || echo "Demo users setup completed or skipped"\n\
echo "🌐 Starting Gunicorn..."\n\
exec gunicorn core.wsgi:application --bind 0.0.0.0:$PORT --workers 3 --timeout 120 --access-logfile -\n\
' > /app/start.sh && chmod +x /app/start.sh

# Run the startup script
CMD ["/app/start.sh"] 