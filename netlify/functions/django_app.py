import os
import sys
import json
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / 'eventpr'))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eventpr.settings')

import django
django.setup()

from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.test import RequestFactory

application = get_wsgi_application()

def handler(event, context):
    """
    Netlify function handler for Django app
    """
    try:
        # Extract request information from Netlify event
        path = event.get('path', '/')
        method = event.get('httpMethod', 'GET')
        headers = event.get('headers', {})
        body = event.get('body', '')
        
        # Create Django request
        factory = RequestFactory()
        
        if method == 'GET':
            request = factory.get(path, **headers)
        elif method == 'POST':
            request = factory.post(path, data=body, content_type='application/json', **headers)
        else:
            request = factory.generic(method, path, data=body, **headers)
        
        # Process request through Django
        response = application(request.environ, lambda status, headers: None)
        
        # Convert Django response to Netlify format
        response_body = b''.join(response).decode('utf-8')
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
            },
            'body': response_body
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
            },
            'body': json.dumps({
                'error': str(e),
                'message': 'Internal server error'
            })
        }
