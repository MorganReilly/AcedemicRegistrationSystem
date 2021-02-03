"""
TITLE: courses.py
ABOUT: WSGI Entry Point
AUTHOR: Morgan Reilly
LINKS:
    * https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-20-04
"""
from server import connex_app as app

if __name__ == "__main__":
    app.run()
