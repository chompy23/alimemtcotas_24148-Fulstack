
from app_conexion import Conexion



class Mascota: 
      
    def tabla_mascota():
        conexion = Conexion('127.0.0.1','root', 'root', 'mascotas')
        conexion.cursor.execute("CREATE TABLE IF NOT EXIST mascotas.mascota ( `id` INT AUTO_INCREMENT , `nombre` VARCHAR(45) NOT NULL, `especie` VARCHAR(45) NOT NULL, `edad` VARCHAR(45) NOT NULL, `raza` VARCHAR(45) NOT NULL, `imagen_url` VARCHAR(255) NULL, `id_secundario` INT(4) NOT NULL, Primary Key (id))")
        conexion.conn.commit()
        val = conexion.cursor.rowcount>0
        conexion.conn.close()
        return val
           
    
    def agregar_mascota(self, nombre, especie, edad, raza, imagen_url, id_secundario): 
        conexion = Conexion('127.0.0.1','root', 'root', 'mascotas')
        sql = ("INSERT INTO mascota" 
               "(nombre, especie, edad, raza, imagen_url, id_secundario)" 
               "VALUES (%s, %s, %s, %s, %s, %s)")
        valores = (nombre, especie, edad, raza, imagen_url, id_secundario)
        conexion.cursor.execute(sql,valores)
        conexion.conn.commit()
        val = conexion.cursor.rowcount>0
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
        
            
    def modificar_mascota(self, id, nombre, especie, edad, raza, imagen_url, id_secundario):
        conexion = Conexion('127.0.0.1','root', 'root', 'mascotas')
        #valores = (nombre, especie, edad, raza, imagen_url, id_secundario, id)
        sql = (f"UPDATE mascota  SET nombre='{nombre}', especie='{especie}', edad='{edad}', raza='{raza}', imagen_url='{imagen_url}', id_secundario='{id_secundario}' WHERE id='{id}'")
        conexion.cursor.execute(sql)
        conexion.conn.commit()
        val = conexion.cursor.rowcount>0
        conexion.conn.close()
        return val
    
    def eliminar_mascota(self,id):
        conexion = Conexion('127.0.0.1','root', 'root', 'mascotas')
        conexion.cursor.execute(f"DELETE FROM mascota WHERE id={id}")
        conexion.conn.commit()
        val = conexion.cursor.rowcount>0
        conexion.conn.close()
        return val
    