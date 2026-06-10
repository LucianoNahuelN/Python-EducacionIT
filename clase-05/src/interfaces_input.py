import tkinter as tk

# Creo ventana
ventana = tk.Tk()

# Configuro ventana
ventana.title("Mi app con input")
ventana.geometry("400x300")

# creo el input y lo incorporo a la interfaz
entrada = tk.Entry(ventana) # input
entrada.pack()

def obtener_texto():
    texto = entrada.get() # obetener lo ingresado
    print(f"Escribiste {texto}")

# Creo el boton y lo incorporo
boton = tk.Button(ventana, text="Enviar" , command=obtener_texto)
boton.pack()

# Arranco la app
ventana.mainloop()
