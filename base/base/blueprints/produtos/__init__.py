from flask import Blueprint

produtos_bp = Blueprint("produtos", __name__, template_folder="templates")

from blueprints.produtos import routes