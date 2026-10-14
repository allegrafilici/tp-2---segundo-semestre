import numpy as np
from PIL import Image

# para acceder a cada pizel indicas primero fila y despues columna matriz[fila,columna]
#[rojo,verde,azul]

def ajustar_resolucion(ruta):
    """se abre la imagen recibida y se ajusta con los pixeles corespondinetes y se ocnvierte en un amatriz """
    imagen = Image.open(ruta)
    imagen_ajustada = imagen.resize((320,240))
    matriz = np.array(imagen_ajustada)
    return matriz 

def desplazar_canales(matriz,desplazamiento):
    """dependiendo del desplazamiento , se recore la imagen y se desplaza el rojo y el azul"""
    copia = matriz.copy()
    for y in range(240):
        for x in range(320):
            if x - desplazamiento >=0:
                copia[y,x,0] = matriz[y,x-desplazamiento,0] 
            if x + desplazamiento < 320:
                copia[y,x,2] = matriz[y, x+ desplazamiento,2]
    return copia 

def scanlines(copia):
    for y in range(0,240,2): 
        for x in range(320): 
            pixel = copia[y,x]
            for c in range(3):
                copia[y,x,c] = round(int(pixel[c])/ 2 )
    return copia 


def filtro_crt(ruta,desplazamiento):
    resolucion = ajustar_resolucion(ruta)
    canales_desplazados = desplazar_canales(resolucion,desplazamiento)
    scanlines_resultado = scanlines(canales_desplazados)
    return scanlines_resultado

resultado = filtro_crt("marilyn.jpeg", 3)
imagen_resultado = Image.fromarray(resultado)


#insertar la imagen en la pantalla 
def recorrer_mascara(ruta_mascara):
    mascara = Image.open(ruta_mascara)
    matriz_mascara = np.array(mascara)
    alto,ancho = matriz_mascara.shape
    altura_pantalla = []
    ancho_pantalla = []
    for y in range(alto):
        for x in range(ancho): 
            if matriz_mascara[y,x] == 255:
                altura_pantalla.append(y)
                ancho_pantalla.append(x)
    punto_0 = (min(ancho_pantalla),min(altura_pantalla))
    punto_1 = (max(ancho_pantalla),max(altura_pantalla))
    return punto_0,punto_1

def pantalla_crt(matriz,punto_0,punto1):
    tv_ctr = Image.open("tv.png")
    mascara = Image.open("tv_mascara.png")
    nuevo_ancho = punto_1[0] - punto_0[0] + 1 
    nuevo_alto = punto_1[1] - punto_0[1] + 1 
    foto = Image.fromarray(matriz)
    foto = foto.resize((nuevo_ancho,nuevo_alto))
    matriz_foto = np.array(foto)
    matriz_mascara = np.array(mascara)
    copia_tv = np.array(tv_ctr).copy()
    alto,ancho = matriz_mascara.shape

    for y in range(alto):
        for x in range(ancho):
            if matriz_mascara[y,x] == 255: 
                copia_tv[y,x] = matriz_foto[y - punto_0[1], x - punto_0[0]]
    return copia_tv


resultado = filtro_crt("marilyn.jpeg", 3)
punto_0, punto_1 = recorrer_mascara("tv_mascara.png")
resultado_tv = pantalla_crt(resultado, punto_0, punto_1)

Image.fromarray(resultado_tv).show()

            





