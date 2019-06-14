# application/auth/__init__.py
from flask import Blueprint
authentication = Blueprint('authentication', __name__, template_folder='templates')
from application.auth import routes
