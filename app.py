import os
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
# create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "tajik_rumi_app_secret_key")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1) # needed for url_for to generate with https

# configure the database - use Heroku database if available, otherwise fall back to local
heroku_db_url = os.environ.get("HEROKU_DATABASE_URL")
if heroku_db_url and heroku_db_url.startswith('postgres://'):
    # Fix for Heroku database URL format
    heroku_db_url = heroku_db_url.replace('postgres://', 'postgresql://', 1)
app.config["SQLALCHEMY_DATABASE_URI"] = heroku_db_url or os.environ.get("DATABASE_URL")
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
