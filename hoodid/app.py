import uuid
from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, send, emit
from controllers.game_controller import game_bp
from controllers.action_controller import action_bp
from controllers.player_controller import player_bp
from models.action import Action
from services.game_service import GameService
from models.player import Player
from flask_cors import CORS

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


assigned_characters = {}

@app.route('/')
def index():
    return render_template('index.html')  # HTML page with the client-side WebSocket code

@app.route('/start_game', methods=['GET'])
def start_game():
    # Logic to start the game goes here
    game_flow = game_service.start_game()

    return jsonify({"message": "Game started!"})

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

    # Add player using the GameService
    new_player = Player(request.sid, assigned_character)
    game_service.add_player(new_player)

    # TODO: add start game button?s
    if len(characters) == 3:
        start_game()
    
    # Update game state
    emit('game_state', {'data': game_service.game.get_game_state()}, broadcast=True)




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


# Get player move location (to connecting location)
@socketio.on('player_suggestion')
def handle_player_suggestion(suggestion: object):
    print("Processing Player Suggestion")

    # Update current suggestion
    game_service.game.suggestion = suggestion



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
        result = game.accuse(game.current_player, guessed_character, guessed_weapon, guessed_location)
        
        # Send the result back to the frontend
        emit('accuse_result', result)


@socketio.on('disconnect')
def on_disconnect():
    character = assigned_characters.pop(request.sid, None)
    if character:
        characters.append(character)
    print(f"Client {request.sid} disconnected and released character {character}")


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