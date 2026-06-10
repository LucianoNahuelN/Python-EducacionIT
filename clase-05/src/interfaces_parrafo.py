import tkinter as tk

# Creo ventana
ventana = tk.Tk()

# Configuro ventana
ventana.title("Trabajando con parrafos")
ventana.geometry("400x300")

# Area de texto
texto = tk.Text(ventana, height=5 , width=30) # Text area
texto.pack()

def obtener_todo():
    contenido = texto.get("1.0", tk.END) # desde el inicio hasta el fin
    print(contenido)

boton = tk.Button(ventana, text="Ver texto", command=obtener_todo)
boton.pack()

ventana.mainloop()

""" Gestion layout:
1- pack(): apilar widgets (arriba-abajo -izq-der)
2- grid(): coloca en filas y columnas
3- place(): posicion exacta (menos comun)
 """
