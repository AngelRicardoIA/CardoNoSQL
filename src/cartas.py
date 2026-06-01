import random
from database import db

def obtener_cartas():
    categorias = [
    "situaciones",
    "emociones",
    "lugares",
    "objetos"
]
    categorias_seleccionadas = random.sample(categorias, 3)
    cartas = []
    for categoria in categorias_seleccionadas:
        coleccion = db[categoria]
        carta = coleccion.aggregate([{"$sample": {"size": 1}}]).next()
        cartas.append(carta)
    return cartas
    