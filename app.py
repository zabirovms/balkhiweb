import os
import logging
from urllib.parse import urlparse

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from extensions import db

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "tajik_rumi_app_secret_key")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1) # needed for url_for to generate with https

# configure the database
database_url = os.environ.get("DATABASE_URL")
if database_url:
    # Fix for Heroku database URL format
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
else:
    # Fallback to SQLite for local development
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

# initialize the app with the extension
db.init_app(app)

# Import routes to register them with the app
with app.app_context():
    # Import models to ensure tables are created
    import models  # noqa: F401
    from routes import register_routes

    register_routes(app)
    
    # Create tables if they don't exist
    db.create_all()
