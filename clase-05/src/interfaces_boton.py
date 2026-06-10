import tkinter as tk

# Creo ventana
ventana = tk.Tk()

# Configuro ventana
ventana.title("Mi app")
ventana.geometry("800x600")

# Funcione q queremos q se ejecute cuando se presione el boton
def al_presionar():
    print("Presionaste el boton")

# Construimos el boton
boton = tk.Button(ventana, text="Presione aqui" , command=al_presionar)
boton.pack()

# Iniciamos la app
ventana.mainloop()
