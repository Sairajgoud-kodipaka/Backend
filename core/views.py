from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
import os
from django.db import connection

@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """
    Health check endpoint for monitoring and deployment verification
    """
    try:
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            db_status = "healthy"
    except Exception as e:
        db_status = f"unhealthy: {str(e)}"
    
    return Response({
        'status': 'healthy',
        'database': db_status,
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'debug': os.getenv('DEBUG', 'False'),
        'timestamp': '2024-01-01T00:00:00Z'  # You can use actual timestamp if needed
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def api_info(request):
    """
    API information endpoint
    """
    return Response({
        'name': 'Jewellery CRM API',
        'version': '1.0.0',
        'description': 'A comprehensive CRM system for jewelry businesses',
        'endpoints': {
            'health': '/api/health/',
            'docs': '/api/schema/swagger-ui/',
            'auth': '/api/auth/',
            'admin': '/admin/'
        }
    }, status=status.HTTP_200_OK) 