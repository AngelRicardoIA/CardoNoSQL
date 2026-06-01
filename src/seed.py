import json
import os
from database import client
from database import db

categorias = [
    "situaciones",
    "emociones",
    "lugares",
    "objetos"
]

for categoria in categorias:
    coleccion = db[categoria]
    ruta_json = os.path.join('semillas', categoria + '.json')
    with open(ruta_json, 'r', encoding='utf-8') as file:
        data = json.load(file)
    if coleccion.count_documents({}) > 0:
        print(f"La colección '{categoria}' ya tiene datos. No se insertarán nuevos datos.")
    else:
        if isinstance(data, list):
            coleccion.insert_many(data)
        else:
            coleccion.insert_one(data)
client.close()

