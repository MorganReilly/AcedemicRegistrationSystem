"""
TITLE: server.py
ABOUT: Main entry point to application
AUTHOR: Morgan Reilly
"""
from flask import Flask, render_template
import config  # Load the configuration from config.py

# Get app instance
connex_app = config.connex_app

# Read swagger.yml file to configure endpoints
connex_app.add_api('swagger.yml')


# Create URL route in application for "/"
@connex_app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    connex_app.run(host='0.0.0.0', port=5000, debug=True)
