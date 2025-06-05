from flask import Flask, render_template, request, redirect, url_for
import os
from detector import analizar_imagen

app = Flask(__name__)

UPLOAD_FOLDER = 'imagenes-analizar'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('static/resultados', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    archivo = request.files['imagen']
    if archivo.filename == '':
        return redirect(url_for('index'))

    ruta_guardar = os.path.join(UPLOAD_FOLDER, archivo.filename)
    archivo.save(ruta_guardar)

    nombre_resultado, alertas = analizar_imagen(archivo.filename)
    return render_template('resultado.html', 
                            imagen_resultado=nombre_resultado,
                            alertas=alertas)

if __name__ == '__main__':
    app.run(debug=True)
