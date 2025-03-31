import cv2
import numpy as np
import os
import random
import string
import argparse

import utilscript as u

def generar_nombre(prefijo, extension=".png", indice=None):
    """Genera un nombre de archivo con sufijo aleatorio o numerado."""
    if indice is not None:
        return f"{prefijo}_{indice}{extension}"
    else:
        sufijo = ''.join(random.choices(string.ascii_lowercase, k=6))
        return f"{prefijo}_{sufijo}{extension}"

def rotar_si_necesario(imagen):
    """Rota la imagen 90° a la izquierda si es más ancha que alta."""
    alto, ancho = imagen.shape[:2]
    if ancho > alto:
        return cv2.rotate(imagen, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return imagen

def procesar_imagenes(ruta_carpeta, prefijo, convertir_a_jpg=False, modo_enum=False, rotar=False):
    if not os.path.exists(ruta_carpeta):
        print(f" \n{u._A} La carpeta no existe.")
        return

    ruta_guardado = os.path.join(ruta_carpeta, "procesadas")
    os.makedirs(ruta_guardado, exist_ok=True)  # Crear carpeta de salida para evitar pérdida de archivos

    imagenes_png = [f for f in os.listdir(ruta_carpeta) if f.lower().endswith(".png")]
    imagenes_jpg = [f for f in os.listdir(ruta_carpeta) if f.lower().endswith(".jpg")]

    if not imagenes_png and not imagenes_jpg:
        print(f" \n{u._A} No se encontraron imágenes en la carpeta.")
        return

    contador = 1  # Contador para la enumeración secuencial

    # Procesar imágenes PNG
    for imagen in imagenes_png:
        ruta_imagen = os.path.join(ruta_carpeta, imagen)
        img = cv2.imread(ruta_imagen, cv2.IMREAD_UNCHANGED)

        if img is None or img.shape[2] != 4:
            print(f" {u._Q} Omitiendo {imagen}, no tiene canal alfa.")
            continue

        _, _, _, alpha = cv2.split(img)
        coords = cv2.findNonZero(alpha)

        if coords is None:
            print(f" {u._Q} Omitiendo {imagen}, es completamente transparente.")
            continue

        x, y, w, h = cv2.boundingRect(coords)
        recorte = img[y:y+h, x:x+w]

        if convertir_a_jpg:
            recorte = cv2.cvtColor(recorte, cv2.COLOR_BGRA2BGR)  # Quitar transparencia

        if rotar:
            recorte = rotar_si_necesario(recorte)

        extension_salida = ".jpg" if convertir_a_jpg else ".png"
        nuevo_nombre = generar_nombre(prefijo, extension_salida, contador if modo_enum else None)
        ruta_salida = os.path.join(ruta_guardado, nuevo_nombre)

        if cv2.imwrite(ruta_salida, recorte):  # Verificar si la imagen se guardó correctamente
            print(f" {u._V} Saved:{u.Y} {nuevo_nombre}")
            try:
                os.remove(ruta_imagen)
            except Exception as e:
                print(f" {u._A} No se pudo eliminar {ruta_imagen}: {e}")
        else:
            print(f" {u._A} Error al guardar {ruta_salida}, no se eliminó el original.")

        contador += 1

    # Procesar imágenes JPG
    for imagen in imagenes_jpg:
        ruta_imagen = os.path.join(ruta_carpeta, imagen)
        img = cv2.imread(ruta_imagen)

        if img is None:
            print(f" {u._Q} Omitiendo {imagen}, no se pudo cargar.")
            continue

        if rotar:
            img = rotar_si_necesario(img)

        nuevo_nombre = generar_nombre(prefijo, ".jpg", contador if modo_enum else None)
        ruta_salida = os.path.join(ruta_guardado, nuevo_nombre)

        if cv2.imwrite(ruta_salida, img):
            print(f" {u._V} Saved:{u.Y} {nuevo_nombre}")
            try:
                os.remove(ruta_imagen)
            except Exception as e:
                print(f" {u._A} No se pudo eliminar {ruta_imagen}: {e}")
        else:
            print(f" {u._A} Error al guardar {ruta_salida}, no se eliminó el original.")

        contador += 1

if __name__ == '__main__':
    u.clear()
    print(u.banner)

    parser = argparse.ArgumentParser(description="Recorta imágenes PNG, renombra JPG y puede rotarlas.")
    parser.add_argument("directory", type=str, help="Directorio donde están las imágenes.")
    parser.add_argument("prefix", type=str, help="Prefijo para los nombres de los archivos procesados.")
    parser.add_argument("--jpg", action="store_true", help="Convertir las imágenes PNG a JPG.")
    parser.add_argument("--enum", action="store_true", help="Activar modo enumeración (_1, _2, _3 en vez de aleatorio).")
    parser.add_argument("--rotate", action="store_true", help="Rotar imágenes horizontales para que queden verticales.")

    args = parser.parse_args()

    u.bar(1, "Finding")
    print('')
    procesar_imagenes(args.directory, args.prefix, args.jpg, args.enum, args.rotate)
