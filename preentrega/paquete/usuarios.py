from .datos_ingresados import guardar_datos
def entrada_datos(Ruta_Base_datos, base_datos: list):
    usuarios = {}
    nombre = input("Nombre: ")
    password = input("Contraseña: ")
    base_datos.append(usuarios)
    usuarios["nombre"] = nombre
    usuarios["password"] = password
    guardar_datos(Ruta_Base_datos, base_datos)
