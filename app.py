from flask import Flask,request,jsonify
from flask_cors import CORS
import mysql.connector 
from werkzeug.utils import secure_filename
from app_mascota import Mascota

import os
import time



app = Flask(__name__)
CORS(app)

#habilita las referencias a otros servidores
#carpeta para guardar las imagenes
ruta_destino = os.makedirs('./static/imagen/', exist_ok=True)
mascota = Mascota()

    
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

      
@app.route("/mascota", methods=["POST"])    
def  agregar_mascota():
    nombre = request.form.get('nombre')
    especie = request.form.get('especie')
    edad = request.form.get('edad')
    raza = request.form.get('raza')
    imagen_url = request.files.get('imagen_url')
    id_secundario = request.form.get('id_secundario')
    
    nombre_imagen = ""
    
    nombre_imagen = secure_filename('imagen_url')
    nombre_base, extension  = os.path.splitext(nombre_imagen)
    nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"
    
    
    
    nueva_mascota = mascota.agregar_mascota(nombre, especie, edad, raza, nombre_imagen, id_secundario)
    if nueva_mascota:
        #imagen_url.save(os.path.join(ruta_destino, nombre_imagen))
        return jsonify({"mensaje": "Mascota agregada correctamente.", "nombre": nombre, "imagen_url": nombre_imagen}), 201 
    else: return jsonify({"mensaje": "Error al agregar  mascota."}), 500
    
@app.route("/mascota/<int:id>", methods=["PUT"])
def modificar_mascota(id):
    nombre = request.form.get('nombre')
    especie = request.form.get('especie')
    edad = request.form.get('edad')
    raza = request.form.get('raza')
    id_secundario = request.form.get('id_secundario')
    imagen_url = request.files.get('imagen_url')    
    
    nombre_imagen = ""
        
    nombre_imagen = secure_filename('imagen_url')
    nombre_base, extension  = os.path.splitext(nombre_imagen)
    nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"
            
    mascota_modificada =  mascota.modificar_mascota(id, nombre, especie, edad, raza, nombre_imagen, id_secundario)    
    if mascota_modificada: 
            return jsonify({"mensaje": "Mascota modificado"}), 200 
    else: 
            return jsonify({"mensaje": "Mascota no encontrado"}), 403
        
@app.route("/mascota/<int:id>", methods=["DELETE"])
def eliminar_mascota(id):
    
    mascota_eliminada = mascota.eliminar_mascota(id)
    if mascota_eliminada:
        return jsonify({"mensaje": "Mascota eliminada correctamente"}), 200
    else:
        return jsonify({"mensaje": "Error al eliminar mascota."}), 500 
    
    
if __name__ == "__main__":
    app.run(debug=True )