import os
import face_recognition
import cv2

def cargar_rostros(carpeta):
    rostros = []
    nombres = []
    for archivo in os.listdir(carpeta):
        ruta = os.path.join(carpeta, archivo)
        imagen = face_recognition.load_image_file(ruta)
        encoding = face_recognition.face_encodings(imagen)
        if encoding:
            rostros.append(encoding[0])
            nombres.append(os.path.splitext(archivo)[0])
    return rostros, nombres

def detectar_en_imagen(ruta_imagen, rostros_conocidos, nombres):
    imagen = face_recognition.load_image_file(ruta_imagen)
    encodings = face_recognition.face_encodings(imagen)
    imagen_cv = cv2.imread(ruta_imagen)

    resultados = []
    for encoding in encodings:
        coincidencias = face_recognition.compare_faces(rostros_conocidos, encoding)
        if True in coincidencias:
            index = coincidencias.index(True)
            nombre = nombres[index]
            mensaje = f"🔴 ALERTA: Persona desaparecida detectada: {nombre}"
            color = (0, 0, 255)
        else:
            nombre = "Desconocido"
            mensaje = "🟢 Persona no desaparecida"
            color = (0, 255, 0)

        resultados.append({
            "mensaje": mensaje,
            "nombre": nombre
        })
        # Dibujar texto
        cv2.putText(imagen_cv, nombre, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    return resultados, imagen_cv
