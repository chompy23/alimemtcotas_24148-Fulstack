
from app_conexion import Conexion

class Usuario:
###############################################
#   Creamos la tabla usuarios
##############################################
    
    def tabla_usuario(self):
        conexion = Conexion('127.0.0.1','root', 'root', 'mascotas')
        conexion.cursor.execute('''CREATE TABLE IF NOT EXISTS usuario (
                            id INT AUTO_INCREMENT PRIMARY KEY, 
                            nombre VARCHAR(255) NOT NULL, 
                            apellido VARCHAR(255) NOT NULL, 
                            calle  VARCHAR(255) NOT NULL, 
                            direccion VARCHAR(255) NOT NULL,
                            ciudad VARCHAR(255) NOT NULL,
                            codigo_postal VARCHAR(255) NOT NULL, 
                            telefono VARCHAR(255) NOT NULL, 
                            e_mail VARCHAR(255) NOT NULL)''')  # crear la tabla en la base de datos 
                             
        conexion.conn.commit()
        conexion.conn.close()

##############################################
#   Definimos la funciòn para agregar usuarios
##############################################

    def agregar_usuario(self, nombre, apellido, calle, direccion, ciudad, codigo_postal, telefono, e_mail): 
        conexion = Conexion('127.0.0.1','root', 'root', 'mascotas')
        valores = (nombre, apellido, calle, direccion, ciudad, codigo_postal, telefono, e_mail)
        sql = ("INSERT INTO usuario" 
               "(nombre, apellido, calle, direccion, ciudad, codigo_postal, telefono, e_mail)" 
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        conexion.cursor.execute(sql,valores)
        conexion.conn.commit()
        val = conexion.cursor.lastrowid
        conexion.conn.close()
        return val
    

# -----------------------------------------------------

##############################################
#  Consultamos por usuarios
##############################################

    def consultar_usuario(self, codigo, nombre ):
        conexion = Conexion('127.0.0.1','root', 'root', 'mascotas')
        #nombre = input("Ingrese el nombre del usuario a buscar : ")
        conexion.cursor.execute(f"SELECT * FROM usuario WHERE {codigo}='{nombre}'")
        val = conexion.cursor.fetchone()
        conexion.conn.close()
        return val
    
# ------------------------------------------------------   

##############################################
# Modificamos un usuario
##############################################

    def modificar_usuario(self, nombre, apellido, calle, direccion, ciudad, codigo_postal, telefono, e_mail, id):
        conexion = Conexion('127.0.0.1','root', 'root', 'mascotas')
        valores = (nombre, apellido, calle, direccion, ciudad, codigo_postal, telefono, e_mail, id)
        sql = ("UPDATE usuario SET nombre=%s, apellido=%s, calle=%s, direccion=%s, ciudad=%s, codigo_postal=%s, telefono=%s, e_mail=%s WHERE id=%s")
        conexion.cursor.execute(sql,valores)
        conexion.conn.commit()
        val = conexion.cursor.rowcount>0
        conexion.conn.close()
        return val
        
# -----------------------------------------------------
 
##############################################
# Listar usuarios
##############################################   
    def listar_usuarios(self):
        conexion = Conexion('127.0.0.1','root', 'root', 'mascotas')
        conexion.cursor.execute(f"SELECT * FROM usuario")
        val = conexion.cursor.fetchall()
        conexion.conn.close()
        return val
        
        
# -----------------------------------------------------  

##############################################
#  Eliminamos usuarios
##############################################
    def eliminar_usuario(self,id):
        conexion = Conexion('127.0.0.1','root', 'root', 'mascotas')
        conexion.cursor.execute(f"DELETE FROM usuario WHERE id={id}")
        conexion.conn.commit()
        val = conexion.cursor.rowcount>0
        conexion.conn.close()
        return val