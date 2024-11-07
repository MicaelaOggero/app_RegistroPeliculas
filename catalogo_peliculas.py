import tkinter as tk
from interfaz.gui_app import Frame, barra_menu #importar la clase y la funcion del paquete
from model.pelicula import crear_tabla

def main():
    
    #Crear la tabla en la base de datos
    crear_tabla()
    
    ventana=tk.Tk()
    ventana.title("Catalogo de Películas")
    ventana.iconbitmap('img/logo-ico.ico')
    
    #Agrega la barra de menu
    barra_menu(ventana)
    
    app=Frame(ventana=ventana)
    
    app.mainloop()

if __name__ == '__main__':
    main()