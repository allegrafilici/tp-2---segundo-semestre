from gameboy import *
from ctr import *

from PIL import Image
import numpy as np

def pedir_ruta():
    ruta = input("Ingrese la ruta de la imagen: ")
    #si ruta not found return none
    return ruta

def pedir_metodo():
    metodo = input("Seleccione la pantalla (gameboy/crt): ")
    if metodo.lower() == "gameboy":
        return "gameboy"
    elif metodo.lower() == "ctr":
        return "ctr"
    return None

def main():
    ruta = pedir_ruta()
    if ruta is None:
        print('No se encontró la imagen. Por favor, verifique la ruta e intente nuevamente.')
        return
    metodo = pedir_metodo()
    
main()