"""
TITLE: server.py
ABOUT: Main entry point to application
AUTHOR: Morgan Reilly
LINKS:
    * https://flask-restful.readthedocs.io/
    * https://flask.palletsprojects.com/en/1.1.x/tutorial/
    * https://realpython.com/flask-connexion-rest-api/
"""
from flask import Flask, render_template
import connexion

# Create application instance
# specification_dir -> Informs connexion what dir to look for config file
app = connexion.App(__name__, specification_dir='./')

# Read swagger.yml file to configure endpoints
app.add_api('swagger.yml')


# Create URL route in application for "/"
@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
