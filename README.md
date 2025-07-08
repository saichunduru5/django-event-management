# EventPR - Django Event Management System

A Django-based web application for managing events with user authentication and booking functionality.

## Features

- User registration and authentication
- Event management
- Event booking system
- Responsive web interface
- Admin panel for event management

## Project Structure

```
eventpr/
├── eventapp/          # Main event management app
├── userapp/           # User authentication app
├── template/          # HTML templates
├── static/           # Static files (CSS, images, JS)
├── pic/              # Image uploads
└── manage.py         # Django management script
```

## Requirements

- Python 3.x
- Django 3.2.25
- SQLite (default database)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/eventpr.git
cd eventpr
```

2. Create a virtual environment:
```bash
python -m venv env1
source env1/bin/activate  # On Windows: env1\Scripts\activate
```

3. Install dependencies:
```bash
pip install django
```

4. Run migrations:
```bash
cd eventpr
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Open your browser and navigate to `http://127.0.0.1:8000/`

## Usage

- Visit the homepage to view available events
- Register for a new account or log in
- Browse and book events
- Admin users can manage events through the admin panel at `/admin/`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
