#!/usr/bin/env python
"""
Static site generator for Django project
This script generates static HTML files from Django templates
"""
import os
import sys
import django
from pathlib import Path

# Add the eventpr directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'eventpr'))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eventpr.settings')
django.setup()

from django.test import Client
from django.urls import reverse
from django.core.management import execute_from_command_line

def generate_static_files():
    """Generate static HTML files"""
    client = Client()
    
    # Create output directory
    output_dir = Path('eventpr/staticfiles')
    output_dir.mkdir(exist_ok=True)
    
    # Pages to generate
    pages = {
        'index.html': '/',
        'about.html': '/about/',
        'events.html': '/events/',
        'contact.html': '/contact/',
        'booking.html': '/booking/',
    }
    
    print("Generating static pages...")
    
    for filename, url in pages.items():
        try:
            response = client.get(url)
            if response.status_code == 200:
                output_file = output_dir / filename
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(response.content.decode('utf-8'))
                print(f"✓ Generated {filename}")
            else:
                print(f"✗ Failed to generate {filename} (status: {response.status_code})")
        except Exception as e:
            print(f"✗ Error generating {filename}: {e}")
    
    print("Static site generation complete!")

if __name__ == '__main__':
    generate_static_files()
