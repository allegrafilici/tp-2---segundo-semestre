from PIL import Image
import numpy as np

GAMEBOY = [(15, 56, 15), (48, 98, 48), (139, 172, 15), (155, 188, 15)]

def convertir_imagen(ruta):#definir ruta en la main
    BAYER_4 = [
    [ 0,  8,  2, 10],
    [12,  4, 14,  6],
    [ 3, 11,  1,  9],
    [15,  7, 13,  5],
]
    paso=64 
    img= ruta.resize((160, 144))
    for x in range(160):
        for y in range(144):
            pixel= ""#falta definir
            brillo= sum("contenido")/3#revisar como hacer
            ajuste= (((BAYER_4*(x%4)*(y%4))/16)-0.5)*paso
            nuevo_brillo=brillo+ajuste
            indice=nuevo_brillo//paso

            if indice==0:
                pixel= GAMEBOY[0]
            elif indice==1:
                pixel= GAMEBOY[1]
            elif indice==2:
                pixel= GAMEBOY[2]
            else:
                pixel=GAMEBOY[3]

    return img
            