#!/bin/bash

# Build script for Netlify deployment
echo "🚀 Starting build process..."

# Install Python dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Navigate to Django project directory
cd eventpr

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Create a simple index.html in staticfiles for static deployment
echo "🌐 Creating static site..."
mkdir -p staticfiles
cat > staticfiles/index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Event Management System</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; text-align: center; }
        .container { max-width: 600px; margin: 0 auto; }
        .btn { background: #007bff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎉 Event Management System</h1>
        <p>Welcome to our Django Event Management System!</p>
        <p>This is a static deployment. For full functionality, please visit the development version.</p>
        <a href="https://github.com/saichunduru5/django-event-management" class="btn">View on GitHub</a>
    </div>
</body>
</html>
EOF

echo "✅ Build complete!"
