"""Arquivo de API."""

from typing import Dict, List

from fastapi import FastAPI

app = FastAPI()


produtos: List[Dict[str, any]] = [
    {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um telefone com funcionamento de computador",
        "preco": 1500.00,
        "disponivel": True,
    },
    {
        "id": 2,
        "nome": "Notebook",
        "descricao": "Um computador com tela de 15 polegadas",
        "preco": 3000.00,
        "disponivel": False,
    },
    {
        "id": 3,
        "nome": "Tablet",
        "descricao": "Um tablet com tela de 10 polegadas",
        "preco": 2000.00,
        "disponivel": True,
    },
]


@app.get("/")
def ola_mundo():
    """Rota raiz da API."""
    return {"Hello": "World"}


@app.get("/produtos")
def buscar_produtos():
    """Rota de Buscar Todos os Produtos da API."""
    return produtos


@app.get("/produtos/{id}")
def buscar_um_produto(id: int):
    """
    Rota de Buscar Um Produto da API.

    Args:
        id (int): ID do Produto.

    Returns:
        Dict[str, any]: Dicionário com os dados do Produto.
    """
    for produto in produtos:
        if produto["id"] == id:
            return produto
    return {"Status": 404, "Mensagem": "Produto não encontrado"}
