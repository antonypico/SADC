# interfaz provisional del sistema SADC
import tkinter as tk
from tkinter import messagebox, ttk

class VentanaPrincipal:
    def __init__(self, root):
        self.root=root
        self.root.title("Bienvenido al sistema de Asignación de Cupos Universitarios")
        self.root.geometry("700x500")
        self.root.configure(bg="#6E6E6E")


#Aqui se define el titulo general de la pestaña principal

        titulo = tk.Label(
            self.root,
            text="Bienvenido al sistema",
            font = ("Arial",30,"bold"),
            fg = "Black",
            bg="#6E6E6E")
            
        titulo.pack(pady=25)

# Creacion de botones
        #boton de periodo
        boton_crear_periodo = tk.Button(
            self.root,
            text = "Crear nuevo periodo",
            font = ("Arial",12,"bold"),
            fg = "Black",
            bg = "#BAFF39")
        
        boton_crear_periodo.pack(pady = 13)

        #boton de configuracion de carreras
        boton_configuracion_carreras =tk.Button(
            self.root,
            text = "Configurar carrera",
            font = ("Arial",12,"bold"),
            fg = "Black",
            bg = "#BAFF39")
        
        boton_configuracion_carreras.pack(pady = 13)

        #boton de cargar archivo excel/csv
        boton_cargar_archivo =tk.Button(
            self.root,
            text = "Cargar archivo",
            font = ("Arial",12,"bold"),
            fg = "Black",
            bg = "#BAFF39")
        
        boton_cargar_archivo.pack(pady = 13)

        #boton de ver resultados
        boton_ver_resultado = tk.Button(
            self.root,
            text = "Ver resultados",
            font = ("Arial",12,"bold"),
            fg = "Black",
            bg = "#BAFF39")
        
        boton_ver_resultado.pack(pady = 13)

        #boton de exportar resultados
        boton_exportar_resultados = tk.Button(
            self.root,
            text = "Exportar resultados",
            font = ("Arial",12,"bold"),
            fg = "Black",
            bg = "#BAFF39")
        
        boton_exportar_resultados.pack(pady = 13)

        #boton salir
        boton_salir = tk.Button(
            root,
            text="Salir",
            font=("Arial", 12, "bold"),
            bg="#BAFF39", 
            fg="Black",
            command=root.destroy)
        
        boton_salir.pack(pady=20)