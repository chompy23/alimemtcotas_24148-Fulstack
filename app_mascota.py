
from app_conexion import Conexion



class Mascota: 
       
    def tabla_mascota():
        conexion = Conexion('127.0.0.1','root', 'root', 'mascotas')
        conexion.cursor.execute('''CREATE TABLE IF NOT EXISTS mascota (
                            id INT AUTO_INCREMENT PRIMARY KEY, 
                            nombre VARCHAR(255) NOT NULL, 
                            especie VARCHAR(255) NOT NULL, 
                            edad  VARCHAR(255) NOT NULL, 
                            raza VARCHAR(255) NOT NULL,
                            imagen_url VARCHAR(255), 
                            id_secundario  INT(4))''') 
        conexion.conn.commit()
        conexion.conn.close()
           
    
    def agregar_mascota(self, nombre, especie, edad, raza, imagen_url, id_secundario): 
        conexion = Conexion('127.0.0.1','root', 'root', 'mascotas')
        sql = ("INSERT INTO mascota" 
               "(nombre, especie, edad, raza, imagen_url, id_secundario)" 
               "VALUES (%s, %s, %s, %s, %s, %s)")
        valores = (nombre, especie, edad, raza, imagen_url, id_secundario)
        conexion.cursor.execute(sql,valores)
        conexion.conn.commit()
        val = conexion.cursor.lastrowid
        conexion.conn.close()
        return val
    
    def consultar_mascota(self,id):
        conexion = Conexion('127.0.0.1','root', 'root', 'mascotas')
        conexion.cursor.execute(f"SELECT * FROM mascota WHERE id={id}")
        val = conexion.cursor.fetchone()
        conexion.conn.close()
        return val

    def listar_mascotas(self):
        conexion = Conexion('127.0.0.1','root', 'root', 'mascotas')
        conexion.cursor.execute(f"SELECT * FROM mascota")
        val = conexion.cursor.fetchall()
        conexion.conn.close()
        return val
        
            
    def modificar_mascota(self, id_a_buscar, nuevo_nombre, nueva_especie, nueva_edad, nueva_raza, nueva_imagen_url, nuevo_id_secundario):
        conexion = Conexion('127.0.0.1','root', 'root', 'mascotas')
        valores = (nuevo_nombre, nueva_especie, nueva_edad, nueva_raza, nueva_imagen_url, nuevo_id_secundario, id_a_buscar)
        sql = ("UPDATE mascota  SET nombre=%s, especie=%s, edad=%s, raza=%s, imagen_url=%s, id_secundario=%s WHERE id=%s")
        conexion.cursor.execute(sql,valores)
        conexion.conn.commit()
        val = conexion.cursor.rowcount>0
        conexion.conn.close()
        return val
    
    def eliminar_mascota(self):
        conexion = Conexion('127.0.0.1','root', 'root', 'mascotas')
        id = int(input("Ingrese el id de la mascota a eliminar : "))
        conexion.cursor.execute(f"DELETE FROM mascota WHERE id={id}")
        conexion.conn.commit()
        val = conexion.cursor.rowcount>0
        conexion.conn.close()
        return val
    