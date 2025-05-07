# Tajik Rumi Poetry Website

A Tajik-language web application showcasing the works of Mawlana Jalaluddin Balkhi (Rumi) with searchable poems, filters, and a biography section.

## Features

- Browse Rumi's works by book, volume, and section
- Search through poems in Tajik language
- Daily verse feature
- Biography of Rumi in Tajik
- Social media sharing functionality
- Mobile-responsive design
- Tajik language interface

## Technology Stack

- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript
- **Styling**: Custom CSS with Tailwind

## Setup and Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables:
   - `DATABASE_URL`: PostgreSQL connection string
   - `FLASK_SECRET_KEY`: Secret key for session management
4. Run migrations: `flask db upgrade`
5. Start the application: `gunicorn --bind 0.0.0.0:5000 main:app`

## Project Structure

- `main.py`: Application entry point
- `models.py`: Database models
- `routes.py`: URL routes and view functions
- `utils.py`: Utility functions
- `templates/`: HTML templates
- `static/`: Static files (CSS, JavaScript, images)

## Database Structure

- Books → Volumes → Sections → Poems
- Biography sections
- Daily verses

## License

All rights reserved. This project was created to showcase Rumi's poetry in Tajik language.