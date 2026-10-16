from gameboy import *
from ctr import *

from PIL import Image
import numpy as np



def pedir_metodo()->str: 
    metodo = input("Selecione la pantalla (gameboy/crt)").strip().lower()
    while metodo != "gameboy" and metodo != "crt": 
        print("Opcion invalida")
        metodo = input("Selecione la pantalla (gameboy/crt)").strip().lower()
    return metodo

def pedir_despla() ->int:
    res = input("Ingrese desplazamiento (ingrese Enter para usar 3)").strip()
    if res == "": 
        return 3 
    while not res.isdecimal() or int(res) <= 0:
        print("debe ser un numero entero y positivo")
        res = input("Ingrese desplazamiento (ingrese Enter para usar 3)").strip()
        if res == "": 
        return 3 
    return int(res)

def main(): 
    ruta = input("Ingresa la ruta de la imagen a processar: ").strip()
    




