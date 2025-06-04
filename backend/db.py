import mysql.connector
from datetime import datetime

# Configuración de conexión MySQL
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "12345",
    "database": "sistema_faces"
}

def conectar():
    return mysql.connector.connect(**DB_CONFIG)

def init_db():
    """Crea la tabla si no existe."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS coincidencias (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            fecha DATETIME NOT NULL,
            ruta_imagen VARCHAR(255)
        )
    """)
    conexion.commit()
    cursor.close()
    conexion.close()

def guardar_deteccion(nombre, ruta_imagen):
    """Guarda una coincidencia en la base de datos."""
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO coincidencias (nombre, fecha, ruta_imagen) VALUES (%s, %s, %s)",
        (nombre, fecha, ruta_imagen)
    )
    conexion.commit()
    cursor.close()
    conexion.close()

def obtener_historial():
    """Devuelve una lista de coincidencias."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, fecha, ruta_imagen FROM coincidencias ORDER BY fecha DESC")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados
