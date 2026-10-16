from gameboy import *
from ctr import *

from PIL import Image
import numpy as np

def pedir_ruta():
    ruta = input("Ingrese la ruta de la imagen: ")
    #si ruta no se encuentra devuelve None
    return ruta


def pedir_metodo():
    metodo = input("Seleccione la pantalla (gameboy/crt): ")
    if metodo.lower() == "gameboy":
        return "gameboy"
    elif metodo.lower() == "ctr":
        return "ctr"
    return None

def guardar_imagen():
    ruta = input("Seleccione la ruta para guardar la imagen procesada:")
    return ruta


def main():
    ruta = pedir_ruta()
    if ruta is None:
        print('No se encontró la imagen. Por favor, verifique la ruta e intente nuevamente.')
        return
    metodo = pedir_metodo()
    guardar=guardar_imagen()
    if metodo=="gameboy":
        matriz = convertir_imagen(ruta)
        punto_0, punto_1, mascara = dimension_pantalla()
        resultado = pantalla_gameboy(matriz, punto_0, punto_1, mascara)
        resultado.show()

    elif metodo=="ctr":
        ""#completar
    else:
        print("Pantalla inválida. Las opciones son 'gameboy' o 'crt'.")

    print(f"Imagen guardada en {guardar}")

main()