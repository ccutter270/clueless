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
# app = Flask(__name__, static_folder='../frontend/dist/frontend')
# CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})
# CORS(app, origins=["https://clueless-ivory.vercel.app"])
CORS(app, resources={r"/*": {"origins": "*"}})
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

game_over_responses = 0
num_players = 0
num_disproves = 0
disproves = []


assigned_characters = {}


@app.route('/', methods=['GET'])
def index():
    # HTML page with the client-side WebSocket code
    return render_template('index.html')


@socketio.on('start_game')
def start_game():
    emit('show_start_button', {'show': False, 'message': ""}, broadcast=True)
    game_service.start_game()


@socketio.on('player_connected')
def broadcast_game_state():
    print("Broadcasting Game state for initial player connection")

    if game_service.started:
        emit('game_error', {'message': "ERROR! The game has already started."})
        return

    if len(game_service.players) >= 6:
        emit('game_error', {
             'message': "ERROR! Maximum players already reached."})
        return

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

    if len(characters) <= 3:
        # Enable Start Game Button
        emit('show_start_button', {
             'show': True, 'message': f"{num_players} players joined. Click to start the game!"}, broadcast=True)


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

    # Update players move locations
    game_service.game.move_to = location


# Get player suggestion
@socketio.on('player_suggestion')
def handle_player_suggestion(suggestion: object):
    print("Processing Player Suggestion")

    # Update current suggestion
    game_service.game.suggestion = suggestion

# Go Back to Previous State


@socketio.on('go_back')
def handle_go_back():

    # Update go back variable
    game_service.game.go_back = True


# Disprove Finished
@socketio.on('disprove')
def handle_disprove(disprove: str):
    global num_players
    global num_disproves
    global disproves

    disproves.append(disprove)

    num_disproves += 1

    if num_disproves == (num_players - 1):
        game_service.game.disprove_finished = True
        game_service.game.disproves = disproves
        num_disproves = 0
        disproves = []


@socketio.on('disconnect')
def on_disconnect():
    global num_players

    # Remove character form the game
    character = assigned_characters.pop(request.sid, None)
    game_service.remove_player(character)

    if character:
        num_players -= 1
        if (num_players >= 3):
            emit('show_start_button', {
                 'show': True, 'message': f"{num_players} players joined. Click to start the game!"}, broadcast=True)
        else:
            emit('show_start_button', {
                 'show': False, 'message': f"Not Enough Players to Start the Game"}, broadcast=True)

    # Make character available again
    if character and (character not in characters):
        characters.append(character)
    print(
        f"Client {request.sid} disconnected and released character {character}")


@socketio.on('game_over')
def on_game_over():

    global game_over_responses
    global num_players

    game_over_responses += 1
    if game_over_responses == num_players:
        # Reset game service
        game_service.new_game()
        game_over_responses = 0
        emit('show_start_button', {
             'show': True, 'message': f"{num_players} players joined. Click to start the game!"}, broadcast=True)


# @socketio.on('prompt_player_action')
# def prompt_action():
#     # Emit the prompt for the player's next action (Accuse, Move, Suggest)
#     action_prompt = game.prompt_player_action()
#     emit('player_action_prompt', action_prompt)  # Send options to frontend

# @app.route('/data')
# def get_data():
#     data = {
#         "message": "Hello, World!",
#         "status": "success",
#         "data": {"key1": "value1", "key2": "value2"}
#     }
#     return jsonify(data)
if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000, debug=True, allow_unsafe_werkzeug=True)
