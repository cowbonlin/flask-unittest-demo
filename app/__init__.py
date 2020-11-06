from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()
socketio = SocketIO()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    socketio.init_app(app, cors_allowed_origins="*")

    from .views import api_bp
    app.register_blueprint(api_bp)
    
    return app

@socketio.on('some_event')
def on_some_event(data):
    print('in some_event, data:', data)
    return {'status': 0}