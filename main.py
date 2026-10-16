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
    elif metodo.lower() == "crt":
        return "crt"
    return None

def guardar_imagen():
    ruta = input("Seleccione la ruta para guardar la imagen procesada:")
    return ruta


def pedir_desplazamiento():
    respuesta = input("INgrese desplazamiento (Enter para usar 3 )")

    while respuesta != "":
        if respuesta.isdecimal():
            if int(respuesta) > 0:
                return int(respuesta)

        print("EL desplazamiento debe de ser un entero positivo. ")
        respuesta = input("INgrese desplazamiento (Enter para usar 3 )")

    return 3 
        
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

    elif metodo=="crt":
        desplazamiento = pedir_desplazamiento()
        matriz = filtro_crt(ruta, desplazamiento)
        punto_0, punto_1 = recorrer_mascara("tv_mascara.png")
        matriz_tv = pantalla_ctr(matriz, punto_0, punto_1)
        resultado = Image.fromarray(matriz_tv)

    else:
        print("Pantalla inválida. Las opciones son 'gameboy' o 'crt'.")

    print(f"Imagen guardada en {guardar}")
    resultado.save(guardar)
    resultado.show()
    print(f"Imagen guardada en {guardar}")

main()