from flask import Flask, send_from_directory
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__,static_folder='../../frontend/dist')
    app.debug = debug
    # secret key for sessions
    app.config['SECRET_KEY'] = 'whatisit?'

    from .api_router import api_router
    app.register_blueprint(api_router,url_prefix="/api")

    socketio.init_app(app,async_mode='threading')

    @app.route('/')
    def index():
        return app.send_static_file("index.html")

    # @app.route('/static/<path:path>')
    # def dist_static(path):
    #     return send_from_directory("../../frontend/dist/static", path)

    @app.route('/css/<path:path>')
    def dist_css(path):
        return send_from_directory("../../frontend/dist/css", path)

    @app.route('/js/<path:path>')
    def dist_js(path):
        return send_from_directory("../../frontend/dist/js", path)

    return app
