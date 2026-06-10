import tkinter as tk

# Creo ventana
ventana = tk.Tk()

# Configuro ventana
ventana.title("Mi app con label")
ventana.geometry("800x600")

# Creamos la etiqueta
etiqueta = tk.Label(ventana, text="Hola mundo")
etiqueta.pack() # mostrar en la interfaz la etiqueta

ventana.mainloop()

