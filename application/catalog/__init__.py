# application/catalog/__init__.py
from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates')

from application.catalog import routes
