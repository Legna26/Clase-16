{"nombre": str,
 "password": str,}

import json

def entrada_datos():
    usuarios = {}
    nombre = input("Nombre: ")
    password = input("Contraseña: ")
    usuarios[nombre] = password
    return usuarios

def guardar_datos():
    ...

def mostrar_datos():
    ...

def main():
    diccionario_datos = entrada_datos()    
    print(diccionario_datos)
    
main()