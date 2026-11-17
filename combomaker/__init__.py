from flask import Flask, send_from_directory, render_template
from . import home
import os

def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(home.bp)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                                   'favicon.ico', mimetype='image/vnd.microsoft.icon')

    return app