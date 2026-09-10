# models.py — Camada Model da Quitanda da Esquina (dados em memória)

usuarios = [
    {"id": 1, "nome": "admin", "senha": "1234"},
]

produtos = [
    {"id": 1, "nome": "Banana", "categoria": "Fruta", "preco": 5.50, "unidade": "kg"},
    {"id": 2, "nome": "Maçã", "categoria": "Fruta", "preco": 7.90, "unidade": "kg"},
    {"id": 3, "nome": "Alface", "categoria": "Verdura", "preco": 2.80, "unidade": "un"},
    {"id": 4, "nome": "Cenoura", "categoria": "Legume", "preco": 3.40, "unidade": "kg"},
    {"id": 5, "nome": "Tomate", "categoria": "Legume", "preco": 6.20, "unidade": "kg"},
]


def buscar_produto(produto_id):
    for p in produtos:
        if p["id"] == produto_id:
            return p
    return None


def buscar_por_categoria(categoria):
    return [p for p in produtos if p["categoria"].lower() == categoria.lower()]


def buscar_por_nome(parte):
    return [p for p in produtos if parte.lower() in p["nome"].lower()]


def todas_categorias():
    categorias = []
    for p in produtos:
        if p["categoria"] not in categorias:
            categorias.append(p["categoria"])
    return categorias