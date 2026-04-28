from flask import Flask, send_from_directory
from . import home
import os

def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(home.bp)

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                                   'favicon.ico', mimetype='image/vnd.microsoft.icon')

    return app