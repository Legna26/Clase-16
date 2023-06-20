import pathlib
from paquete.datos_ingresados import cargar_datos, mostrar_datos
from paquete.usuarios import entrada_datos

Base_Dir = pathlib.Path(__file__).resolve().parent
Ruta_Base_datos = Base_Dir / "base_de_datos.json"

def main():
    base_datos: list = cargar_datos(Ruta_Base_datos)
    entrada_datos(Ruta_Base_datos, base_datos)
    mostrar_datos(base_datos)
    
main()