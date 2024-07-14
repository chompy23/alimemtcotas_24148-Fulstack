import mysql.connector 

class Conexion: 
    def __init__(self, host, user, password, database): 
        self.conn = mysql.connector.connect( 
                                            host=host, 
                                            user=user, 
                                            password=password, 
                                            database=database) 
        self.cursor = self.conn.cursor(dictionary=True) 
        # Intentamos seleccionar la base de datos 
        try: 
            self.cursor.execute("USE mascotas")
        except mysql.connector.Error as err: # Si la base de datos no existe, la creamos 
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR: 
                self.cursor.execute("CREATE DATABASE mascotas") 
                self.conn.database = database 
            else: raise err
        
            
           
