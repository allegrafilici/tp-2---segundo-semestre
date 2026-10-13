from PIL import Image
import numpy as np

ruta=Image.open("monalisa.jpg")
def convertir_imagen(ruta):
    GAMEBOY = [(15, 56, 15), (48, 98, 48), (139, 172, 15), (155, 188, 15)]
    BAYER_4 = [
    [ 0,  8,  2, 10],
    [12,  4, 14,  6],
    [ 3, 11,  1,  9],
    [15,  7, 13,  5],
]
    paso=64 

    img= Image.open(ruta)
    nuevo_tamaño= img.resize((160, 144))
    matriz=np.array(nuevo_tamaño)

    for y in range(144):
        for x in range(160):
            pixel= matriz[y,x]
            brillo= (int(pixel[0])+int(pixel[1])+int(pixel[2]))/3
            ajuste= ((((BAYER_4[y%4][x%4])+0.5)/16)-0.5)*paso
            nuevo_brillo=brillo+ajuste
            indice=nuevo_brillo//paso

            if indice<=0:
                matriz[y,x]= GAMEBOY[0]
            elif indice==1:
                matriz[y,x]= GAMEBOY[1]
            elif indice==2:
                matriz[y,x]= GAMEBOY[2]
            else:
                matriz[y,x]=GAMEBOY[3]

    return matriz

Image.fromarray(convertir_imagen(ruta)).show
