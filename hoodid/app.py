import uuid

from controllers.action_controller import action_bp
from controllers.game_controller import game_bp
from controllers.player_controller import player_bp
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from flask_socketio import SocketIO, emit, send
from models.action import Action
from models.player import Player
from services.game_service import GameService

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})
app.config['SECRET_KEY'] = 'my_secret_key'

socketio = SocketIO(app, cors_allowed_origins="*")

game_service = GameService()

characters = [
    "Professor Plum",
    "Miss Scarlet",
    "Mrs. Peacock",
    "Mr. Green",
    "Colonel Mustard",
    "Mrs. White"
]

# global num_players
# global num_disproves

num_players = 0
num_disproves = 0
disproves = []


assigned_characters = {}


@app.route('/')
def index():
    # HTML page with the client-side WebSocket code
    return render_template('index.html')


@app.route('/start_game', methods=['GET'])
def start_game():
    # Logic to start the game goes here
    game_flow = game_service.start_game()

    return jsonify({"message": "Game started!"})


@socketio.on('player_connected')
def broadcast_game_state():
    print("Broadcasting Game state for initial player connection")
    if len(characters) > 0:
        # Get a character and remove it from the list
        assigned_character = characters.pop(0)
    else:
        assigned_character = None  # Or handle cases where no characters are available

    # Store the assignment with the session ID as a unique identifier
    assigned_characters[request.sid] = assigned_character

    # Send the assigned character to the client
    emit('character_assignment', {'character': assigned_character})
    print(f"Assigned character {assigned_character} to client {request.sid}")

    # Add player using the GameService
    new_player = Player(request.sid, assigned_character)
    game_service.add_player(new_player)

    global num_players
    num_players += 1

    # Update game state
    game_service.game.last_action_taken = f"Player {request.sid} joined as character {assigned_character}"
    emit('game_state', {
         'data': game_service.game.get_game_state()}, broadcast=True)

    if len(characters) == 3:
        # TODO: Enable start game button
        start_game()


# Get player action (move, suggest, accuse)
@socketio.on('player_action')
def handle_player_action(action: Action):
    print("Processing player action")
    print(action)

    game_service.game.action = action["message"]


# Get player move location (to connecting location)
@socketio.on('player_move_location')
def handle_player_move_location(location: str):
    print("Processing Move Location")
    print(location)

    # Update players move locations
    game_service.game.move_to = location


# Get player suggestion
@socketio.on('player_suggestion')
def handle_player_suggestion(suggestion: object):
    print("Processing Player Suggestion")

    # Update current suggestion
    game_service.game.suggestion = suggestion


# Disprove Finished
@socketio.on('disprove')
def handle_disprove(disprove: str):
    global num_players
    global num_disproves
    global disproves

    print(f"RECEIVED DISPROVE {disprove} \n\n\n")

    disproves.append(disprove)

    num_disproves += 1

    if num_disproves == (num_players - 1):
        game_service.game.disprove_finished = True
        game_service.game.disproves = disproves
        num_disproves = 0
        disproves = []

# Function to handle the accusation


@socketio.on('get_accusation')
def get_accusation(data):
    global game
    accusation = data.get('accusation')

    if accusation:
        guessed_character = accusation.get('character')
        guessed_weapon = accusation.get('weapon')
        guessed_location = accusation.get('location')

        # Verify the accusation against the solution
        result = game.accuse(
            game.current_player, guessed_character, guessed_weapon, guessed_location)

        # Send the result back to the frontend
        emit('accuse_result', result)


@socketio.on('disconnect')
def on_disconnect():
    character = assigned_characters.pop(request.sid, None)
    if character:
        characters.append(character)
    print(
        f"Client {request.sid} disconnected and released character {character}")


@socketio.on('prompt_player_action')
def prompt_action():
    # Emit the prompt for the player's next action (Accuse, Move, Suggest)
    action_prompt = game.prompt_player_action()
    emit('player_action_prompt', action_prompt)  # Send options to frontend


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
