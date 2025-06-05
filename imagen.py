import face_recognition
from PIL import Image
import os

image_path = "imagenes-analizar/img.jpg"
image = face_recognition.load_image_file(image_path)

face_locations = face_recognition.face_locations(image)
os.makedirs("rostros", exist_ok=True)

for i, (top, right, bottom, left) in enumerate(face_locations):
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.save(f"rostros/rostro_{i+1}.jpg")

print(f"{len(face_locations)} rostros detectados y guardados en la carpeta 'rostros'.")
