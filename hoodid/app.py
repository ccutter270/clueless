import uuid
from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, send, emit
from controllers.game_controller import game_bp
from controllers.action_controller import action_bp
from controllers.player_controller import player_bp
from services.game_service import GameService

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
socketio = SocketIO(app, cors_allowed_origins='*')

game_service = GameService()

app.register_blueprint(game_bp, url_prefix='/game')
app.register_blueprint(action_bp, url_prefix='/action')
app.register_blueprint(player_bp, url_prefix='/player')

@app.route('/')
def index():
    return render_template('index.html')  # HTML page with the client-side WebSocket code


@app.route('/add_player', methods=['POST'])
def add_player():
    data = request.json
    character = data.get('character')

    if not character or any(player.character == character for player in game_service.players):
        return jsonify({"error": "Missing required fields"}), 400

    # Add player using the GameService
    game_service.add_player(character)
    return jsonify({"message": f"{character} added to the game!"})


@app.route('/start_game', methods=['GET'])
def start_game():
    # Logic to start the game goes here
    game_service.start_game()

    return jsonify({"message": "Game started!"})


# Handle messages sent from the client
@socketio.on('message')
def handle_message(message):
    game_service.start_game()
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