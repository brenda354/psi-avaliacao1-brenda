# Este arquivo ainda não é usado pela aplicação.
from app import app
from flask import render_template
import models


@auth_bp.route("/produtos")
def listar_produtos():
    return render_template("produtos/index.html", produtos=models.produtos)
