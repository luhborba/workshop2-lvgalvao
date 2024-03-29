"""Arquivo de Teste."""

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ola_mundo():
    """Teste da Rota raiz da API."""
    response = client.get("/")
    assert response.status_code == 200


def test_ola_mundo_json():
    """Teste da Rota raiz da API."""
    response = client.get("/")
    assert response.json() == {"Hello": "World"}


def test_buscar_produtos_status_code():
    """Teste de Status Code."""
    reponse = client.get("/produtos")
    assert reponse.status_code == 200


def test_tamanho_buscar_produtos():
    """Teste de Tamanho da Lista de Produtos."""
    reponse = client.get("/produtos")
    assert len(reponse.json()) == 3


def test_pega_um_produto():
    """Teste de Buscar Um Produto."""
    response = client.get("/produtos/1")
    assert response.json() == {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um telefone com funcionamento de computador",
        "preco": 1500.00,
        "disponivel": True,
    }
