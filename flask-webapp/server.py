"""
TITLE: server.py
ABOUT: Main entry point to application
AUTHOR: Morgan Reilly
LINKS:
    * https://flask-restful.readthedocs.io/
    * https://flask.palletsprojects.com/en/1.1.x/tutorial/
    * https://realpython.com/flask-connexion-rest-api/
    * https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html
"""
from flask import Flask
import config  # Load the configuration from config.py

# Get app instance
connex_app = config.connex_app

# Read swagger.yml file to configure endpoints
connex_app.add_api('swagger.yml')

if __name__ == '__main__':
    connex_app.run(host='0.0.0.0', port=5000, debug=True)
