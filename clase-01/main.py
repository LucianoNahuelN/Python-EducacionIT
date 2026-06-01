print("Hola mundo")

print("Comentario en una linea")
# Una sola linea
# Otra linea

print("Comentario en varias lineas")
""" Alt + shift + A
En
varias 
lineas """

print("Variables")

nombre = "Maxi"
print(nombre) # Cadena (String)
print(type(nombre)) # str

edad = 22
print(edad)
print(type(edad)) # int

is_teacher = True # snake_case -> palabra1_palabra2_palabra3
print(is_teacher)
print(type(is_teacher)) # bool
is_teacher = False
print(is_teacher)

precio = 33.99
print(precio)
print(type(precio)) # float

print("Concatenacion de cadenas")
# Juntar texto
segundo_nombre = "Luis"
apellido = "Principe"

nombre_completo = nombre + " " + segundo_nombre + " " + apellido
print(nombre_completo)

# F-STRINGS (PARECIDO AL TEMPLATE STRINGS DE JS)
nombre_completo = f"{nombre} {segundo_nombre} {apellido}"
print(nombre_completo)

#join 
nombre_completo = " ".join([nombre, segundo_nombre, apellido])
print(nombre_completo)

texto = "La" * 3
print(texto) #LaLaLa

print("Funcion input(): Para pedir datos al usuario")
dato = input("Escriba aqui su nombre: ")
print(dato)
print(f"Hola {dato}")

print("Casteo (conversion de tipos)")
cantidad_alumnos = input("¿Cuantos alumnos estan en clase?")
print(cantidad_alumnos) #esto es una cadena
cantidad_alumnos = int(cantidad_alumnos) # casteo una cadena a numero
print(type(cantidad_alumnos)) #int
cantidad_personas = cantidad_alumnos + 2
print(cantidad_personas)
print(type(cantidad_personas)) # int

