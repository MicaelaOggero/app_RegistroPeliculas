import mysql.connector
from tkinter import messagebox
from .conexion_db import ConexionDB

def crear_tabla():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE IF NOT EXISTS pelicula (
        id_pelicula INT PRIMARY KEY AUTO_INCREMENT,
        nombre VARCHAR(100) NOT NULL,
        duracion VARCHAR(10) NOT NULL,
        genero VARCHAR(100) NOT NULL,
        fecha_estreno DATE
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_conexion()
    except mysql.connector.Error as e:
        titulo = 'Crear Tabla'
        mensaje = f'Error en la base de datos: {e}'
        messagebox.showwarning(titulo, mensaje)

class Pelicula:
    def __init__(self, nombre, duracion, genero, fecha_estreno):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
        self.fecha_estreno = fecha_estreno
        
    # Estado de este objeto
    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}, {self.fecha_estreno}]'

def guardarDatos(pelicula):
    conexion = ConexionDB()

    sql = """INSERT INTO pelicula (nombre, duracion, genero, fecha_estreno) 
             VALUES (%s, %s, %s, %s)"""

    try:
        conexion.cursor.execute(sql, (pelicula.nombre, pelicula.duracion, pelicula.genero, pelicula.fecha_estreno))
        conexion.cerrar_conexion()
        titulo = 'Guardar Datos'
        mensaje = 'Los datos se guardaron correctamente'
        messagebox.showinfo(titulo, mensaje)
    except mysql.connector.Error as e:
        titulo = 'Guardar Datos'
        mensaje = f'Error al guardar los datos: {e}'
        messagebox.showerror(titulo, mensaje)

def obtenerDatos():
    conexion = ConexionDB()

    lista_peliculas = []

    sql = 'SELECT * FROM pelicula'

    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar_conexion()
    except mysql.connector.Error as e:
        titulo = 'Obtener Datos'
        mensaje = f'Error al obtener los datos: {e}'
        messagebox.showerror(titulo, mensaje)

    return lista_peliculas

def editarDatos(pelicula, id_pelicula):
    conexion = ConexionDB()

    sql = """UPDATE pelicula
             SET nombre = %s, duracion = %s, genero = %s, fecha_estreno = %s WHERE id_pelicula = %s"""

    try:
        conexion.cursor.execute(sql, (pelicula.nombre, pelicula.duracion, pelicula.genero, pelicula.fecha_estreno, id_pelicula))
        conexion.cerrar_conexion()
    except mysql.connector.Error as e:
        titulo = 'Editar Datos'
        mensaje = f'Error al editar los datos: {e}'
        messagebox.showerror(titulo, mensaje)

def eliminarDatos(id_pelicula):
    conexion = ConexionDB()

    sql = 'DELETE FROM pelicula WHERE id_pelicula = %s'

    try:
        conexion.cursor.execute(sql, (id_pelicula,))
        conexion.cerrar_conexion()
    except mysql.connector.Error as e:
        titulo = 'Eliminar Datos'
        mensaje = f'Error al eliminar los datos: {e}'
        messagebox.showerror(titulo, mensaje)
