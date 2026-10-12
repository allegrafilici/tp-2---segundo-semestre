from gameboy import *
from ctr import *

from PIL import Image
import numpy as np

def pedir_metodo():
    metodo = input("Seleccione la pantalla (gameboy/crt): ")
    if metodo.lower() == "gameboy":
        return "gameboy"
    elif metodo.lower() == "ctr":
        return "ctr"
    return None

def main():
    ""
main()