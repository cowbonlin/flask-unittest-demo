from app import create_app, socketio


if __name__ == '__main__':
    app = create_app('development')
    socketio.run(app, port=5000, host='0.0.0.0')
