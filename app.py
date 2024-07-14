from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector 
from werkzeug.utils import secure_filename
from app_mascota import Mascota

import os
import time


app = Flask(__name__)
CORS(app) #habilita las referencias a otros servidores

mascota = Mascota()

#carpeta para guardar las imagenes
ruta_destino = './imagen/'

@app.route("/mascota", methods=["GET"])
def listar_mascotas():
    return jsonify(mascota.listar_mascotas())

@app.route("/mascota/<int:id>", methods=["GET"])
def mostrar_mascota(id):
    ver_mascota = mascota.consultar_mascota(id)  
    if ver_mascota:
        return jsonify(ver_mascota)
    else:
        return "Mascota no encontrada", 404  

if __name__ == "__main__":
    app.run(debug=True)