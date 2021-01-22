from app import app

from rest.routes import app as find_server_app

app.register_blueprint(find_server_app, url_prefix='/{}'.format(find_server_app.name))

if __name__ == '__main__':
    app.run(port=8085, debug=True)
