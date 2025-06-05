import face_recognition
from PIL import Image
import os

# Cargar imagen
image_path = "imagenes-analizar/img.jpg"
image = face_recognition.load_image_file(image_path)

# Detectar ubicaciones de rostros
face_locations = face_recognition.face_locations(image)

# Crear carpeta para rostros si no existe
os.makedirs("rostros", exist_ok=True)

# Recortar y guardar cada rostro
for i, (top, right, bottom, left) in enumerate(face_locations):
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.save(f"rostros/rostro_{i+1}.jpg")

print(f"{len(face_locations)} rostros detectados y guardados en la carpeta 'rostros'.")
