#!/usr/bin/env python3
"""
Script to test database connection with the provided Render PostgreSQL URL
"""

import os
import sys
import django
from django.conf import settings

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
os.environ.setdefault('DATABASE_URL', 'postgresql://jewellery_crm_db_user:XpRN4xurPZeQTHAVKWtE3UXGOHs3Fo0T@dpg-d27ebaeuk2gs73e2sbg0-a/jewellery_crm_db')

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configure Django settings
django.setup()

from django.db import connection

def test_database_connection():
    """Test the database connection"""
    try:
        print("Testing database connection...")
        print(f"DATABASE_URL: {os.environ.get('DATABASE_URL')}")
        print()
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")
            version = cursor.fetchone()
            print(f"✅ Database connection successful!")
            print(f"PostgreSQL version: {version[0]}")
            
            # Test a simple query
            cursor.execute("SELECT 1 as test;")
            result = cursor.fetchone()
            print(f"Test query result: {result[0]}")
            
        return True
        
    except Exception as e:
        print(f"❌ Database connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_database_connection()
    sys.exit(0 if success else 1) 