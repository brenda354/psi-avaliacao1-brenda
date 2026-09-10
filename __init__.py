from flask import Blueprint

auth_bp = Blueprint("produtos", __name__, template_folder="templates")

posts_bp = Blueprint("produtos", __name__, template_folder="templates")


from blueprints.produtos import routes