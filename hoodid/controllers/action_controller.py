from flask import Blueprint, render_template

action_bp = Blueprint('action', __name__)


@action_bp.route('/')
def index():
    return "Action Controller"


@action_bp.route('/request')
def action_state():
    return "ACTION REQUEST"
