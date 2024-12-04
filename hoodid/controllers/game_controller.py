from flask import Blueprint, render_template

game_bp = Blueprint('game', __name__)


@game_bp.route('/')
def index():
    return "GAME"


@game_bp.route('/state')
def game_state():
    return "GAME STATE"
