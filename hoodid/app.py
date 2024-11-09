from flask import Flask, jsonify
from controllers.game_controller import game_bp
from controllers.action_controller import action_bp
from controllers.player_controller import player_bp

app = Flask(__name__)

app.register_blueprint(game_bp, url_prefix='/game')
app.register_blueprint(action_bp, url_prefix='/action')
app.register_blueprint(player_bp, url_prefix='/player')

@app.route('/')
def index():
    return "App Works!"

@app.route('/data')
def get_data():
    data = {
        "message": "Hello, World!",
        "status": "success",
        "data": {"key1": "value1", "key2": "value2"}
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)