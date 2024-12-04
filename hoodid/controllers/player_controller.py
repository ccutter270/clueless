from flask import Blueprint, render_template

player_bp = Blueprint('player', __name__)


@player_bp.route('/')
def index():
    return "Player Controller"


@player_bp.route('/count')
def player_state():
    return "PLAYER COUNT"
