from flask import Flask, render_template, request, redirect, url_for
import os
import uuid
from detector import procesar_imagen
from db import init_db, guardar_deteccion

app = Flask(__name__)
UPLOAD_FOLDER = 'data/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

init_db()  # Inicializa la base de datos si es necesario

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subir', methods=['POST'])
def subir():
    if 'imagen' not in request.files:
        return "No se envió ninguna imagen", 400

    imagen = request.files['imagen']
    if imagen.filename == '':
        return "Nombre de archivo vacío", 400

    nombre_archivo = str(uuid.uuid4()) + ".jpg"
    ruta = os.path.join(app.config['UPLOAD_FOLDER'], nombre_archivo)
    imagen.save(ruta)

    nombre_detectado = procesar_imagen(ruta)

    if nombre_detectado:
        guardar_deteccion(nombre_detectado, ruta)
        return render_template('resultado.html', nombre=nombre_detectado)
    else:
        return render_template('resultado.html', nombre=None)

if __name__ == '__main__':
    app.run(debug=True)
