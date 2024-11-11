import uuid
from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, send, emit
from controllers.game_controller import game_bp
from controllers.action_controller import action_bp
from controllers.player_controller import player_bp
from models.action import Action
from services.game_service import GameService

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
socketio = SocketIO(app, cors_allowed_origins='*')

game_service = GameService()

characters = [
    "Professor Plum",
    "Miss Scarlet",
    "Mrs. Peacock",
    "Mr. Green",
    "Colonel Mustard",
    "Mrs. White"
]

assigned_characters = {}

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


# Custom event example
@socketio.on('player_action')
def handle_player_action(action: Action):
    print("Processing player action")
    print(action)
    # Update game state
    socketio.emit('game_state', {'data': game_service.get_game_state()})


@socketio.on('player_connected')
def broadcast_game_state():
    print("Broadcasting Game state for initial player connection")
    if len(characters) > 0:
        assigned_character = characters.pop(0)  # Get a character and remove it from the list
    else:
        assigned_character = None  # Or handle cases where no characters are available

    # Store the assignment with the session ID as a unique identifier
    assigned_characters[request.sid] = assigned_character

    # Send the assigned character to the client
    emit('character_assignment', {'character': assigned_character})
    print(f"Assigned character {assigned_character} to client {request.sid}")
    # Update game state
    emit('game_state', {'data': game_service.get_game_state()})


@socketio.on('disconnect')
def on_disconnect():
    # Release the character back to the list on client disconnect
    character = assigned_characters.pop(request.sid, None)
    if character:
        characters.append(character)
    print(f"Client {request.sid} disconnected and released character {character}")


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