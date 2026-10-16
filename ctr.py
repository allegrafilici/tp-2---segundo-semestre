import numpy as np
from PIL import Image

# para acceder a cada pizel indicas primero fila y despues columna matriz[fila,columna]
#[rojo,verde,azul]

def ajustar_resolucion(ruta:str) -> np.ndarray:
    """se abre la imagen recibida y se ajusta con los pixeles corespondinetes y se convierte a una
    matriz de Numpy, retorna la matriz de piceles de la imagen redimensionada """
    imagen = Image.open(ruta)
    imagen_ajustada = imagen.resize((320,240))
    matriz = np.array(imagen_ajustada)
    return matriz 

def desplazar_canales(matriz:np.darray,desplazamiento:int)-> np.ndarray:
    """dependiendo del desplazamiento , se recore la imagen y se desplaza el rojo y el azul
    Cada pixel toma el rojode una posiciona su izquierda y el azul de una posicion a la derecha. 
    El verde permanece igual. Si la posicionde origen queda fuera de laimage , conserva el canal original. """
    copia = matriz.copy()
    for y in range(240):
        for x in range(320):
            if x - desplazamiento >=0:
                copia[y,x,0] = matriz[y,x-desplazamiento,0] 
            if x + desplazamiento < 320:
                copia[y,x,2] = matriz[y, x+ desplazamiento,2]
    return copia 

def scanlines(copia:np.darray)-> np.ndarray:
    """Oscurece las filas pares de una imagen. 
    Divide por dos los tres canales de cada pizel de las filas pares y tambien
    redondea el resultado. Retorna la misma matriz pero con las filas pares
    oscurecidas """
    for y in range(0,240,2): 
        for x in range(320): 
            pixel = copia[y,x]
            for c in range(3):
                copia[y,x,c] = round(int(pixel[c])/ 2 )
    return copia 


def filtro_crt(ruta:str,desplazamiento:int)->np.ndarray:
    """Se aplica el filtro ctr s uns imagen, se ajusta la resolucion
    y se desplaza los canales rojo y azul y se oscurecen las filas pares
    para que parezca un televisor de tubo.Retorna la matriz de la imagen
    con el filtro CTR aplicado. """
    resolucion = ajustar_resolucion(ruta)
    canales_desplazados = desplazar_canales(resolucion,desplazamiento)
    scanlines_resultado = scanlines(canales_desplazados)
    return scanlines_resultado

resultado = filtro_crt("marilyn.jpeg", 3)
imagen_resultado = Image.fromarray(resultado)



#insertar la imagen en la pantalla 
def recorrer_mascara(ruta_mascara:str)-> tuple[tuple[int, int], tuple[int, int]]:
    """Recorre la imagen de la mascara de la televiosn y encuntra 
    los pixeles blancos. Retorna dos puntos en formato (columna,fila) que serian
    la esquina superior izquierda y la esquina inferior derecha. """
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

def pantalla_ctr(matriz:np.ndarray,punto_0:tuple[int,int],punto1:tuple[int,int]):
    """Inserta una imagen filtrada en la pantalla de tv.png. 
    Redimensiona la imagen al rectangulo indicado y rempalza los pixeles del televisor donde 
    tv_mascara.png es balnca. Conserva el resto de la foto del aparato. 
    Retorna la matriz de la foto del televisor ocn la imagen insertada """
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
resultado_tv = pantalla_ctr(resultado, punto_0, punto_1)

Image.fromarray(resultado_tv).show()
