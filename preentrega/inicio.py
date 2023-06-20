import json
import pathlib

Base_Dir = pathlib.Path(__file__).resolve().parent
Ruta_Base_datos = Base_Dir / "base_usuarios.json"
base_datos = []
def entrada_datos():
    usuarios = {}
    nombre = input("Nombre: ")
    password = input("Contraseña: ")
    base_datos.append(usuarios)
    usuarios[nombre] = password
    guardar_datos()

def guardar_datos():
    with open(Ruta_Base_datos, "w") as archivo:
        json.dump(base_datos, archivo, indent=4)

def mostrar_datos():
    ...

def main():
    diccionario_datos = entrada_datos()    
    print(diccionario_datos)
    
main()