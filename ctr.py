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
            for c in in range(3):
                copia[y,x,c] = round(int(pixel[c])/ 2 )
    return copia 


def filtro_crt(ruta,desplazamiento):
    resolucion = ajustar_resolucion(ruta)
    canales_desplazados = desplazar_canales(resolucion,desplazamiento)
    scanlines_resultado = scanlines(canales_desplazados)
    return scanlines_resultado

resultado = filtro_crt("marilyn.jpeg", 3)
imagen_resultado = Image.fromarray(resultado)
imagen_resultado.show()


#insertar la imagen en la pantalla 









