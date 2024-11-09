import uuid
from flask import Flask, jsonify, render_template
from flask_socketio import SocketIO, send, emit
from controllers.game_controller import game_bp
from controllers.action_controller import action_bp
from controllers.player_controller import player_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
socketio = SocketIO(app)

app.register_blueprint(game_bp, url_prefix='/game')
app.register_blueprint(action_bp, url_prefix='/action')
app.register_blueprint(player_bp, url_prefix='/player')

@app.route('/')
def index():
    return render_template('index.html')  # HTML page with the client-side WebSocket code

# Handle messages sent from the client
@socketio.on('message')
def handle_message(message):
    print('Received message:', message)
    send('Server received: ' + message)  # Echo message back to the client

# Custom event example
@socketio.on('custom_event')
def handle_custom_event(data):
    print('Received custom event data:', data)
    emit('response_event', {'data': 'Data received successfully'})

@app.route('/data')
def get_data():
    data = {
        "message": "Hello, World!",
        "status": "success",
        "data": {"key1": "value1", "key2": "value2"}
    }
    return jsonify(data)

if __name__ == '__main__':
    socketio.run(app, debug=True)