""" 
Ejercicio 1: Variables y tipos

Consigna: Crear un programa que guarde en variables:
* El nombre 
* El apellido
* La altura en metros (decimales)
* Si sos estudiante o no (v o f)

Mpstrar en pantalla todos los datos
 """
print("Ejercicio Uno")

nombre = input("Ingre su nombre: ")
apellido = input("Ingrese su apellido: ")
altura = float(input("Ingrese su altura(mentros): "))
estudiante = input("¿Es estudiante?(si/no) ")
if estudiante == "si":
    estudiante = True
else:
    estudiante = False

dato_completo =  f"Nombre completo: {nombre} {apellido}, altura: {altura}, estudiante: {estudiante} "
print(dato_completo)

