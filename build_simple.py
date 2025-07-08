#!/usr/bin/env python3
"""
Simple static site builder for Netlify deployment
Creates a static version of the Django site
"""
import os
import shutil
from pathlib import Path

def create_static_site():
    """Create a static version of the site"""
    
    # Create dist directory
    dist_dir = Path('dist')
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    dist_dir.mkdir()
    
    # Copy static files
    static_src = Path('eventpr/static')
    if static_src.exists():
        shutil.copytree(static_src, dist_dir / 'static')
        print("✓ Copied static files")
    
    # Copy media files
    media_src = Path('eventpr/pic')
    if media_src.exists():
        shutil.copytree(media_src, dist_dir / 'media')
        print("✓ Copied media files")
    
    # Create main index.html
    index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Event Management System</title>
    <link rel="stylesheet" href="/static/css/style.css">
    <style>
        body { 
            font-family: 'Arial', sans-serif; 
            margin: 0; 
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .hero {
            text-align: center;
            padding: 100px 20px;
            color: white;
        }
        .hero h1 {
            font-size: 3rem;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .hero p {
            font-size: 1.2rem;
            margin-bottom: 30px;
            opacity: 0.9;
        }
        .btn {
            display: inline-block;
            background: #ff6b6b;
            color: white;
            padding: 15px 30px;
            text-decoration: none;
            border-radius: 50px;
            font-weight: bold;
            transition: transform 0.3s ease;
            margin: 10px;
        }
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }
        .features {
            background: white;
            padding: 80px 20px;
            text-align: center;
        }
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            max-width: 1000px;
            margin: 0 auto;
        }
        .feature {
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 40px 20px;
        }
    </style>
</head>
<body>
    <div class="hero">
        <h1>🎉 Event Management System</h1>
        <p>Your one-stop solution for managing events, bookings, and user registration</p>
        <a href="https://github.com/saichunduru5/django-event-management" class="btn">View Source Code</a>
        <a href="#features" class="btn">Learn More</a>
    </div>
    
    <div class="features" id="features">
        <h2>Features</h2>
        <div class="feature-grid">
            <div class="feature">
                <h3>🎪 Event Management</h3>
                <p>Create, edit, and manage events with ease. Full CRUD operations for event organizers.</p>
            </div>
            <div class="feature">
                <h3>👥 User Authentication</h3>
                <p>Secure user registration and login system with Django's built-in authentication.</p>
            </div>
            <div class="feature">
                <h3>📅 Event Booking</h3>
                <p>Allow users to book events with confirmation emails and booking management.</p>
            </div>
            <div class="feature">
                <h3>📱 Responsive Design</h3>
                <p>Mobile-friendly interface that works seamlessly across all devices.</p>
            </div>
            <div class="feature">
                <h3>🔧 Admin Panel</h3>
                <p>Powerful Django admin interface for managing events, users, and bookings.</p>
            </div>
            <div class="feature">
                <h3>📧 Email Integration</h3>
                <p>Automated email confirmations for bookings and user notifications.</p>
            </div>
        </div>
    </div>
    
    <div class="footer">
        <p>&copy; 2024 Event Management System. Built with Django and deployed on Netlify.</p>
        <p>
            <a href="https://github.com/saichunduru5/django-event-management" style="color: #ff6b6b;">GitHub Repository</a> |
            <a href="mailto:chundurusai5@gmail.com" style="color: #ff6b6b;">Contact Developer</a>
        </p>
    </div>
</body>
</html>"""
    
    # Write index.html
    with open(dist_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)
    print("✓ Created index.html")
    
    # Create a simple 404 page
    error_404 = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 100px; }
        h1 { color: #ff6b6b; }
        a { color: #667eea; text-decoration: none; }
    </style>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you're looking for doesn't exist.</p>
    <a href="/">← Back to Home</a>
</body>
</html>"""
    
    with open(dist_dir / '404.html', 'w', encoding='utf-8') as f:
        f.write(error_404)
    print("✓ Created 404.html")
    
    print("🎉 Static site build complete!")
    print(f"📁 Files created in: {dist_dir.absolute()}")

if __name__ == '__main__':
    create_static_site()
