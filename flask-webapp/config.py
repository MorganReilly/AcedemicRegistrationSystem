"""
TITLE: config.py
ABOUT: Handles import and config of necessary modules
AUTHOR: Morgan Reilly
"""
import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Point to directory where program is running in
basedir = os.path.abspath(os.path.dirname(__file__))

# Create Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get underlying Flask app instance
app = connex_app.app

# Build Sqlite URL
sqlite_url = "sqlite:///" + os.path.join(basedir, "academic.db")

# Configure SQLAlchemy part of app instance
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialise Marshmallow
ma = Marshmallow(app)
