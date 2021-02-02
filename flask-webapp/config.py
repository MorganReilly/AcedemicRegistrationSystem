"""
TITLE: config.py
ABOUT: Handles import and config of necessary modules
AUTHOR: Morgan Reilly
"""
import os
import connexion
from flask_mysqldb import MySQL

# Point to directory where program is running in
basedir = os.path.abspath(os.path.dirname(__file__))

# Create Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get underlying Flask app instance
app = connex_app.app

"""MySQL Local Configuration"""
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'morgan'
# app.config['MYSQL_PASSWORD'] = 'rootpassword'
# app.config['MYSQL_DB'] = 'academicdb'

"""MySQL AWS Configuration"""
app.config['MYSQL_HOST'] = 'academic-database.cykgq28ntsef.eu-west-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'rootpassword'
app.config['MYSQL_DB'] = 'academicdb'

# Create MySQL db instance
db = MySQL(app)
