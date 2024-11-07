import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import datetime
from datetime import datetime
from model.pelicula import Pelicula, guardarDatos, obtenerDatos, editarDatos, eliminarDatos
from PIL import Image
from PIL import ImageTk


#crea la barra de menu
def barra_menu(ventana):
    barra_menu = tk.Menu(ventana)
    ventana.config(menu= barra_menu, width=300, height=300)
    
    #agrega la opcion inicio
    menu_inicio=tk.Menu(barra_menu, tearoff=0) 
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio)

class Frame(tk.Frame):
    
    def __init__(self, ventana = None):
        #creacion de la ventana
        super().__init__(ventana,width=450, height=450)
        self.ventana=ventana
        self.pack()
        
        #Para manejar la actualización de un registro
        self.id_pelicula=None
        
        #llamo a los metodos
        self.campos_pelicula()
        
        self.deshabilitar_campos()
        
        self.tabla_peliculas()
        
    #metodo para crear los campos de pelicula
    def campos_pelicula(self):
        
        #Labels de cada campo
        self.label_nombre=tk.Label(self, text="Nombre: ")
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0,column=0, padx=10, pady=10)
        
        self.label_duracion=tk.Label(self, text="Duración: ")
        self.label_duracion.config(font=('Arial', 12, 'bold'))
        self.label_duracion.grid(row=1,column=0, padx=10, pady=10)
        
        self.label_genero=tk.Label(self, text="Género: ")
        self.label_genero.config(font=('Arial', 12, 'bold'))
        self.label_genero.grid(row=2,column=0, padx=10, pady=10)
        
        self.label_fecha_estreno=tk.Label(self, text="Fecha de Estreno: ")
        self.label_fecha_estreno.config(font=('Arial', 12, 'bold'))
        self.label_fecha_estreno.grid(row=3,column=0, padx=10, pady=10)
        
        #Imagen referencial
        self.imagen= Image.open('img/imagen.jpg')
        self.imagen_redimensionada=self.imagen.resize((200,200))
        self.imgen_tk=ImageTk.PhotoImage(self.imagen_redimensionada)
        
        #Label para imagen referencial
        self.label_imagen=tk.Label(self,image=self.imgen_tk)
        self.label_imagen.grid(row=0, column=3, rowspan=4)
        
        #Entrys de cada campo
        self.var_nombre=tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.var_nombre)
        self.entry_nombre.config(width=50, font=('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
        
        self.var_duracion=tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable=self.var_duracion)
        self.entry_duracion.config(width=50, font=('Arial', 12))
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
        
        self.var_genero=tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable=self.var_genero)
        self.entry_genero.config(width=50, font=('Arial', 12))
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)
        
        self.var_date_entry=tk.StringVar()
        self.date_entry=DateEntry(self, width='12', background='darkblue', foreground='whitw', borderwidth=2, textvariable=self.var_date_entry)
        self.date_entry.grid(row=3, column=1, padx=10, pady=10)
        
        #Botones
        self.boton_nuevo=tk.Button(self, text='Nuevo', command=self.limpiar_campos)
        self.boton_nuevo.config(bg="green", width=20, font=('Arial', 12, 'bold'), fg='white', cursor='hand2', activebackground='lightgreen')
        self.boton_nuevo.grid(row=4, column=0, padx=10, pady=10)
        
        self.boton_guardar=tk.Button(self, text='Guardar', command=self.guardar_datos)
        self.boton_guardar.config(bg="blue", width=20, font=('Arial', 12, 'bold'), fg='white', cursor='hand2', activebackground='lightblue')
        self.boton_guardar.grid(row=4, column=1, padx=10, pady=10)
        
        #boton eliminar
        self.boton_eliminar=tk.Button(self, text='Eliminar', command=self.eliminar_datos)
        self.boton_eliminar.config(bg="red", width=20, font=('Arial', 12, 'bold'), fg='white', cursor='hand2', activebackground='#FF6666')
        self.boton_eliminar.grid(row=4, column=2, padx=10, pady=10)
        
        # Asociar los eventos de mouse a los entries
        self.entry_nombre.bind("<Enter>", lambda e: self.cambiar_color(self.entry_nombre))
        self.entry_nombre.bind("<Leave>", lambda e: self.restablecer_color(self.entry_nombre))

        self.entry_duracion.bind("<Enter>", lambda e: self.cambiar_color(self.entry_duracion))
        self.entry_duracion.bind("<Leave>", lambda e: self.restablecer_color(self.entry_duracion))

        self.entry_genero.bind("<Enter>", lambda e: self.cambiar_color(self.entry_genero))
        self.entry_genero.bind("<Leave>", lambda e: self.restablecer_color(self.entry_genero))
    
    #cambiar color
    def cambiar_color(self, entry):
        entry.config(bg='lightblue')

    #restaurar color
    def restablecer_color(self, entry):
        entry.config(bg="white")  
    
    def limpiar_campos(self):
        #Reiniciar el id
        self.id_pelicula=None
        
        self.var_nombre.set('')
        self.var_duracion.set('')
        self.var_genero.set('') 
        self.var_date_entry.set('')
        
        self.habilitar_campos()
    
    def habilitar_campos(self):
        
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')
        self.date_entry.config(state='normal')
        self.boton_guardar.config(state='normal')
        self.boton_eliminar.config(state='normal')
    
    def deshabilitar_campos(self):
        #Reiniciar el id
        self.id_pelicula=None
            
        #limpia los campos
        self.var_nombre.set('')
        self.var_duracion.set('')
        self.var_genero.set('')
        self.var_date_entry.set('')
        
        #dehabilita campos y botones
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')
        self.date_entry.config(state='disabled')
        self.boton_guardar.config(state='disabled')
        self.boton_eliminar.config(state='disabled')
        
    def guardar_datos(self):
        
        pelicula = Pelicula(
            self.var_nombre.get(),
            self.var_duracion.get(),
            self.var_genero.get(),
            self.date_entry.get_date()
        )
        
        #Validación antes de guardar los datos para saber si se trata de una actualización o un nuevo registro 
        
        if self.id_pelicula == None:
            guardarDatos(pelicula)
        else:
            editarDatos(pelicula, self.id_pelicula)
        
        self.tabla_peliculas()
        
        self.deshabilitar_campos()
        
    def tabla_peliculas(self):
        
        #obtener la lista de peliculas
        self.peliculas=obtenerDatos()
        self.lista_peliculas= list(self.peliculas)
        #invertir los datos en la lista para que se muestren en orden ascendente de id
        self.lista_peliculas.reverse()
        
        #Crear la tabla
        self.tabla=ttk.Treeview(self, columns=('Nombre', 'Duración', 'Género', 'FechaEstreno'))
        self.tabla.grid(row=5, column=0, columnspan=4, sticky='nse', pady=10, padx=5)
        
        #Scrollbar para la tabla si excede 10 registros
        self.scroll= ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)
        
        
        #encabezado de la tabla
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='DURACIÓN')
        self.tabla.heading('#3', text='GÉNERO')
        self.tabla.heading('#4', text='FECHA ESTRENO')
        
        #Iterar la lista de peliculas
        for p in self.lista_peliculas:
            #insertar valores a la tabla | los primeros dos son por defecto
            self.tabla.insert('', 0, text=p[0], values=(p[1], p[2], p[3], p[4]))
         
        # Enlazar selección en la tabla a la función editarDatos   
        self.tabla.bind("<<TreeviewSelect>>", self.editar_datos)
        

    def editar_datos(self, event):
        
        #Asegurarse que los entrys esten en blanco 
        self.var_nombre.set('')
        self.var_duracion.set('')
        self.var_genero.set('') 
        self.var_date_entry.set('')
        
        self.item_seleccion=self.tabla.selection()
        
        try:
            self.registro= self.tabla.item(self.item_seleccion)
            #Recuperar los datos del registro seleccionado en la tabla
            self.id_pelicula = self.registro['text']
            self.nombre_pelicula=self.registro['values'][0]
            self.duracion_pelicula=self.registro['values'][1]
            self.genero_pelicula=self.registro['values'][2] 
            self.fecha_estreno=self.registro['values'][3] 
            
            self.habilitar_campos()
            
            #Mostrar los datos en los entrys
            self.entry_nombre.insert(0, self.nombre_pelicula)
            self.entry_duracion.insert(0, self.duracion_pelicula)
            self.entry_genero.insert(0, self.genero_pelicula)
            fecha_obj = datetime.strptime(self.fecha_estreno, '%Y-%m-%d').date()
            self.date_entry.set_date(fecha_obj)
            
        except:
            titulo = 'Editar Datos'
            mensaje = 'No ha seleccionado ningún registro'
            messagebox.showerror(titulo, mensaje)
        

    def eliminar_datos(self):
        #obtengo el id
        self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
        if self.id_pelicula:
            eliminarDatos(self.id_pelicula)
            self.tabla_peliculas()
            self.deshabilitar_campos()
        
            #Reiniciar el id
            self.id_pelicula=None
            
        else:
            titulo = 'Eliminar Datos'
            mensaje = 'No ha seleccionado ningún registro'
            messagebox.showerror(titulo, mensaje)