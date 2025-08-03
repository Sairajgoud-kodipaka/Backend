#!/usr/bin/env python3
"""
Script to help set up database configuration for Render deployment
"""

import os
from decouple import config

def main():
    """Set up database configuration"""
    
    # Your Render PostgreSQL URL
    DATABASE_URL = "postgresql://jewellery_crm_db_user:XpRN4xurPZeQTHAVKWtE3UXGOHs3Fo0T@dpg-d27ebaeuk2gs73e2sbg0-a/jewellery_crm_db"
    
    print("Database Configuration for Render:")
    print("=" * 50)
    print(f"DATABASE_URL: {DATABASE_URL}")
    print()
    
    # Parse the URL to show individual components
    if DATABASE_URL.startswith('postgresql://'):
        parts = DATABASE_URL.replace('postgresql://', '').split('@')
        if len(parts) == 2:
            credentials = parts[0].split(':')
            host_db = parts[1].split('/')
            
            if len(credentials) >= 2 and len(host_db) >= 2:
                username = credentials[0]
                password = credentials[1]
                host_port = host_db[0].split(':')
                host = host_port[0]
                port = host_port[1] if len(host_port) > 1 else '5432'
                database = host_db[1]
                
                print("Individual components:")
                print(f"  DB_USER: {username}")
                print(f"  DB_PASSWORD: {password}")
                print(f"  DB_HOST: {host}")
                print(f"  DB_PORT: {port}")
                print(f"  DB_NAME: {database}")
    
    print()
    print("To set this in Render:")
    print("1. Go to your Render dashboard")
    print("2. Select your web service")
    print("3. Go to Environment tab")
    print("4. Add environment variable:")
    print(f"   Key: DATABASE_URL")
    print(f"   Value: {DATABASE_URL}")
    print()
    print("Or update your render.yaml to include:")
    print("  - key: DATABASE_URL")
    print("    value: postgresql://jewellery_crm_db_user:XpRN4xurPZeQTHAvKWtE3UXGOHs3FoOT@dpg-d27ebaeuk2gs73e2sbg0-a/jewellery_crm_db")

if __name__ == "__main__":
    main() 