"""
    File:       wsgi.py
    Date:       23/11/2020
    Summary:    To forward requests from a NGINX web server to Flask Application
"""

from app import app
from rest.routes import app as find_server_app

app.register_blueprint(find_server_app, url_prefix='/{}'.format(find_server_app.name))

if __name__ == "__main__":
    app.run()
