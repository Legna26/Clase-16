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
    usuarios["nombre"] = nombre
    usuarios["password"] = password
    guardar_datos()

def guardar_datos():
    with open(Ruta_Base_datos, "w") as archivo:
        json.dump(base_datos, archivo, indent=4)

def cargar_datos():
    try:
        with open(Ruta_Base_datos, "r") as archivo:
            global base_datos
            base_datos = json.load(archivo)
    except json.decoder.JSONDecodeError:
        print("Archivo Corrupto", e)
    except FileNotFoundError:
        print("Archivo no encontrado, no se cargaran datos")
def mostrar_datos():
    print(base_datos)

def main():
    cargar_datos()
    entrada_datos()
    
main()