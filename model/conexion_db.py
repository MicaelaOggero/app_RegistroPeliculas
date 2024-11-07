import pymysql

class ConexionDB:
    def __init__(self):
        self.base_datos = 'peliculas'  # Cambia a tu base de datos
        self.usuario = 'root'  # Usuario que creaste
        self.contraseña = 'Exaktus'  # Contraseña que asignaste

        # Conexión a la base de datos
        self.conexion = pymysql.connect(
            host='localhost',
            user=self.usuario,
            passwd=self.contraseña,
            db=self.base_datos
        )
        self.cursor = self.conexion.cursor()
    
    def cerrar_conexion(self):
        self.conexion.commit()
        self.conexion.close()
