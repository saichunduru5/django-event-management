#!/usr/bin/env python
"""
Deployment script for Netlify
This script prepares the Django project for deployment
"""
import os
import sys
import subprocess
from pathlib import Path

def run_command(command, cwd=None):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error running command: {command}")
            print(f"Error output: {result.stderr}")
            return False
        print(f"✓ {command}")
        return True
    except Exception as e:
        print(f"Exception running command {command}: {e}")
        return False

def main():
    """Main deployment function"""
    print("🚀 Starting deployment preparation...")
    
    # Change to eventpr directory
    eventpr_dir = Path(__file__).parent / 'eventpr'
    
    # Install dependencies
    print("\n📦 Installing dependencies...")
    if not run_command("pip install -r ../requirements.txt"):
        return False
    
    # Collect static files
    print("\n📁 Collecting static files...")
    if not run_command("python manage.py collectstatic --noinput", cwd=eventpr_dir):
        return False
    
    # Run migrations
    print("\n🗄️ Running database migrations...")
    if not run_command("python manage.py migrate", cwd=eventpr_dir):
        return False
    
    # Generate static site
    print("\n🌐 Generating static site...")
    if not run_command("python ../build_static.py"):
        return False
    
    print("\n✅ Deployment preparation complete!")
    print("\nNext steps:")
    print("1. Commit and push your changes to GitHub")
    print("2. Connect your GitHub repo to Netlify")
    print("3. Set environment variables in Netlify dashboard")
    print("4. Deploy!")

if __name__ == '__main__':
    main()
