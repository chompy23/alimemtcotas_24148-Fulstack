from flask import Flask,request,jsonify
from flask_cors import CORS
import mysql.connector 
from werkzeug.utils import secure_filename
from app_mascota import Mascota

import os, pathlib
import time

#carpeta para guardar las imagenes
DIRECCION = './imagen'
DIRECCION2 = './static/imagen/'

app = Flask(__name__)

CORS(app)




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


"""@app.route("/", methods=["POST"])
def crear_tabla():
    tabla_creada = mascota.tabla_mascota()
    if tabla_creada:
        return jsonify({"mensaje": " Tabla Mascota agregada correctamente.", "nombre": nombre, "imagen_url": imagen_url}), 201 
    else: 
        return jsonify({"mensaje": "Error al agregar  la tabla mascota."}), 500
      """
@app.route("/mascota", methods=["POST"])    
def  agregar_mascota():
    nombre = request.form['nombre']
    especie = request.form['especie']
    edad = request.form['edad']
    raza = request.form['raza']
    imagen_url = request.files['imagen_url']
    id_secundario = request.form['id_secundario']
    
    nombre_imagen = ""
    
    nombre_imagen = secure_filename(imagen_url.filename)
    nombre_base, extension  = os.path.splitext(nombre_imagen)
    nombre_imagen_final = f"{DIRECCION2}{nombre_base}_{int(time.time())}{extension}"
    
       
    nueva_mascota = mascota.agregar_mascota(nombre, especie, edad, raza, nombre_imagen_final, id_secundario)
    
    if nueva_mascota:
        imagen_url.save(nombre_imagen_final)
        return jsonify({"mensaje": "Mascota agregada correctamente.", "nombre": nombre, "imagen_url": nombre_imagen_final}), 201 
    else: return jsonify({"mensaje": "Error al agregar  mascota."}), 500
    
@app.route("/mascota/<int:id>", methods=["PUT"])
def modificar_mascota(id):
    nombre = request.form['nombre']
    especie = request.form['especie']
    edad = request.form['edad']
    raza = request.form['raza']
    id_secundario = request.form['id_secundario']
        
    if 'imagen_url' in request.files: 
        imagen = request.files['imagen_url'] 
        #Procesamiento de la imagen 
        nombre_imagen = secure_filename(imagen.filename) 
        nombre_base, extension = os.path.splitext(nombre_imagen) 
        modifica_nombre_imagen = f"{DIRECCION2}{nombre_base}_{int(time.time())}{extension}" 
        # Guardar la imagen en el servidor """
        imagen.save(modifica_nombre_imagen) 
        
        # Busco la imagen anterior del producto en el directorio 
        mascota_encontrada = mascota.consultar_mascota(id) 
        if mascota_encontrada: # Si existe el producto... 
            imagen_vieja =  mascota_encontrada['imagen_url'] 
            # Armo la ruta a la imagen
            ruta_a_borrar = f"{imagen_vieja}"
            # Y si existe la borro.
            os.remove(ruta_a_borrar) 
    
    else: 
         mascota_encontrada = mascota.consultar_mascota(id)  
         if mascota_encontrada: 
             modifica_nombre_imagen = mascota['imagen_url'] 
             
    # Se llama al método modificar_mascota pasando el codigo del producto y los nuevos datos. 
    mascota_modificada =  mascota.modificar_mascota(id, nombre, especie, edad, raza, modifica_nombre_imagen, id_secundario)    
    if mascota_modificada: 
            return jsonify({"mensaje": "Mascota modificado"}), 200 
    else: 
            return jsonify({"mensaje": "Mascota no encontrado"}), 403
        

@app.route("/mascota/<int:id>", methods=["DELETE"])
def eliminar_mascota(id):
    #Borro la imagen en el directorio
    mascota_encontrada = mascota.consultar_mascota(id) 
    if mascota_encontrada: # Si existe el producto... 
            imagen_vieja =  mascota_encontrada['imagen_url'] 
            ruta_a_borrar = f"{imagen_vieja}"
            os.remove(ruta_a_borrar)
             
    #Borro la mascota de la base de datos
    mascota_eliminada = mascota.eliminar_mascota(id)
    if mascota_eliminada:
        return jsonify({"mensaje": "Mascota eliminada correctamente"}), 200
    else:
        return jsonify({"mensaje": "Error al eliminar mascota."}), 500 
    
    
if __name__ == "__main__":
    app.run(debug=True )