from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()


produtos : List[Dict[str, any]] = [
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
    return {"Hello": "World"}

@app.get("/produtos")
def buscar_produtos():
    return produtos