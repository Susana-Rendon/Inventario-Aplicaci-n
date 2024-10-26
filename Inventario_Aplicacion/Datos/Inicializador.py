import json
import os

#cargar el inventario desde un archivo JSON
def cargar_inventario():
    if os.path.exists('inventory.json'):
        with open('inventory.json', 'r') as archivo:
            return json.load(archivo)
    else:
        return {}

#guardar el inventario en el archivo JSON
def guardar_inventario(inventario):
    with open('inventory.json', 'w') as archivo:
        json.dump(inventario, archivo, indent=4)
