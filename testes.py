import pytest

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_ola_mundo():
    response = client.get("/")
    assert response.status_code == 200

def test_ola_mundo_json():
    response = client.get("/")
    assert response.json() == {"Hello": "World"}


def test_buscar_produtos_status_code():
    reponse = client.get("/produtos")
    assert reponse.status_code == 200

def test_tamanho_buscar_produtos():
    reponse = client.get("/produtos")
    assert len(reponse.json()) == 3

def test_pega_um_produto():
    response = client.get("/produtos/1")
    assert response.json()  == {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um telefone com funcionamento de computador",
        "preco": 1500.00,
        "disponivel": True,
    }