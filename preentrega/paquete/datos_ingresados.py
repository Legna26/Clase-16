import json
def guardar_datos(Ruta_Base_datos, base_datos):
    with open(Ruta_Base_datos, "w") as archivo:
        json.dump(base_datos, archivo, indent=4)

def cargar_datos(Ruta_Base_datos) -> list:
    base_datos = []
    try:
        with open(Ruta_Base_datos, "r") as archivo:
            base_datos = json.load(archivo)
    except json.decoder.JSONDecodeError:
        print("Archivo Corrupto.")
    except FileNotFoundError:
        print("Archivo no encontrado, no se cargaran datos.")
    return base_datos
def mostrar_datos(base_datos):
    print(base_datos)
