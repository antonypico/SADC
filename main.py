# main.py
from interfaz.interfaz_principal import VentanaPrincipal
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()

    