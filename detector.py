import os
import cv2
import face_recognition
import numpy as np

def analizar_imagen(nombre_imagen):
    carpeta_desaparecidos = "personas-buscadas"
    rostros_desaparecidos = []
    nombres = []

    for archivo in os.listdir(carpeta_desaparecidos):
        ruta = os.path.join(carpeta_desaparecidos, archivo)
        imagen = face_recognition.load_image_file(ruta)
        encoding = face_recognition.face_encodings(imagen)
        if encoding:
            rostros_desaparecidos.append(encoding[0])
            nombres.append(os.path.splitext(archivo)[0])

    ruta_imagen = os.path.join("imagenes-analizar", nombre_imagen)
    if not os.path.exists(ruta_imagen):
        print(f"Error: No se encuentra la imagen {nombre_imagen}")
        return None, []

    imagen = face_recognition.load_image_file(ruta_imagen)
    imagen_cv = cv2.imread(ruta_imagen)
    if imagen_cv is None:
        print(f"Error: No se pudo cargar la imagen: {ruta_imagen}")
        return None, []

    face_locations = face_recognition.face_locations(imagen)
    encodings_encontrados = face_recognition.face_encodings(imagen, face_locations)

    encontrados = []

    for (top, right, bottom, left), encoding in zip(face_locations, encodings_encontrados):
        resultados = face_recognition.compare_faces(rostros_desaparecidos, encoding)
        
        if True in resultados:
            index = resultados.index(True)
            nombre = nombres[index]
            encontrados.append(nombre)
            cv2.rectangle(imagen_cv, (left, top), (right, bottom), (0, 0, 255), 2)
            etiqueta = f"Desaparecido: {nombre}"
            (w, h), _ = cv2.getTextSize(etiqueta, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
            overlay = imagen_cv.copy()
            cv2.rectangle(overlay, (left, bottom), (left + w + 12, bottom + 25), (0, 0, 255), -1)
            cv2.addWeighted(overlay, 0.5, imagen_cv, 0.5, 0, imagen_cv)
            cv2.putText(imagen_cv, etiqueta, (left + 6, bottom + 18), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        else:
            cv2.rectangle(imagen_cv, (left, top), (right, bottom), (0, 255, 0), 2)

    output_path = os.path.join("static", "resultados", f"resultado_{nombre_imagen}")
    cv2.imwrite(output_path, imagen_cv)

    return f"resultado_{nombre_imagen}", encontrados
