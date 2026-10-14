from PIL import Image
import numpy as np

ruta="monalisa.jpg"
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

resultado=Image.fromarray(convertir_imagen(ruta))
resultado.show()

def dimension_pantalla():
    img= Image.open("gameboy_mascara.png")
    mascara=np.array(img)
    alto,ancho=mascara.shape 
    
    altura_pantalla=[]
    ancho_pantalla=[]
    for y in range(alto):
        for x in range(ancho):
            pixel=mascara[y,x]
            if pixel==255:
                altura_pantalla.append(y)
                ancho_pantalla.append(x)
    punto_0=(ancho_pantalla[0],altura_pantalla[0])
    punto_1=(ancho_pantalla[-1],altura_pantalla[-1])
    return punto_0,punto_1

def pantalla_gameboy(matriz,punto_0,punto_1):
    gameboy= Image.open("gameboy.png")
    mascara=Image.open("gameboy_mascara.png")
    nuevo_ancho=punto_1[0]-punto_0[0]+1
    nuevo_alto=punto_1[1]-punto_0[1]+1
    foto= matriz.resize(nuevo_ancho,nuevo_alto)
    alto,ancho=mascara.shape
    for y in range(alto):
        for x in range(ancho):
            pixel= mascara[y,x]
            if pixel==0:
                pixel=gameboy[y,x]
