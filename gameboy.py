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
    punto_0=(min(ancho_pantalla),altura_pantalla[0])
    punto_1=(max(ancho_pantalla),altura_pantalla[-1])
    return punto_0,punto_1,mascara

def pantalla_gameboy(matriz,punto_0,punto_1,mascara):
    alto,ancho=mascara.shape
    marco= Image.open("gameboy.png")
    gameboy= np.array(marco.resize((ancho,alto)))

    nuevo_ancho=punto_1[0]-punto_0[0]+1
    nuevo_alto=punto_1[1]-punto_0[1]+1
    filtro=Image.fromarray(matriz)
    foto= np.array(filtro.resize((nuevo_ancho,nuevo_alto)))

    for y in range(alto):
        for x in range(ancho):
            pixel=mascara[y,x]
            if pixel==255:
                gameboy[y, x]=foto[y-punto_0[1],x-punto_0[0]]

    return Image.fromarray(gameboy)

matriz = convertir_imagen(ruta)
punto_0, punto_1, mascara = dimension_pantalla()
resultado = pantalla_gameboy(matriz, punto_0, punto_1, mascara)
resultado.show()