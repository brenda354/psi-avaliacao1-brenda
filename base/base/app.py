# app.py — Quitanda da Esquina (versão inicial)
from flask import Flask, render_template, request, redirect, url_for, session
import models


class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco


app = Flask(__name__)
app.secret_key = "quitanda-secreta"


@app.route("/")
def index():
    q = request.args.get("q", "")
    if q:
        lista = [p for p in models.produtos if q.lower() in p["nome"].lower()]
    else:
        lista = models.produtos
    return render_template("index.html", produtos=lista, q=q,
                           categorias=models.todas_categorias())


@app.route("/produto/<int:produto_id>")
def ver_produto(produto_id):
    produto = models.buscar_produto(produto_id)
    if produto is None:
        return "Produto não encontrado", 404
    return f"""
    <h2>{produto['nome']}</h2>
    <p>Categoria: {produto['categoria']}</p>
    <p>Preço: R$ {produto['preco']} por {produto['unidade']}</p>
    <a href='/'>Voltar para a quitanda</a>
    """


@app.route("/categoria/<nome>")
def ver_categoria(nome):
    lista = []
    for p in models.produtos:
        if p["categoria"].lower() == nome.lower():
            lista.append(p)
    return render_template("index.html", produtos=lista, q="",
                           categorias=models.todas_categorias())


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        for u in models.usuarios:
            if u["nome"] == request.form["nome"] and u["senha"] == request.form["senha"]:
                session["usuario"] = u["nome"]
                return redirect(url_for("painel"))
        return render_template("login.html", erro="Usuário ou senha inválidos")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)