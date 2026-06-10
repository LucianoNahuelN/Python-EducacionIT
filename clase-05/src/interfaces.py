import tkinter as tk

class MiApp:
    """ Constructor """
    def __init__(self, ventana):
        self.ventana = ventana
        # Configuro la ventana
        self.ventana.title("Mi primera aplicacion") # titulo
        self.ventana.geometry("800x600") # dimensiones

    def iniciar(self):
        """  Mostrar ventna """
        self.ventana.mainloop()

# Crear una ventana principal
ventana = tk.Tk()

# Creamos la aplicacion
app = MiApp(ventana) # Instanciamos la clase -> creamos el objeto

# Mostrar
app.iniciar()
