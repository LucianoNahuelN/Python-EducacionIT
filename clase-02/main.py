print("Clase 02 - Repaso condicionales")
""" Un condicional es una estructura de control que nos permite tomar deciciones y ejecutar codigo u otro dependiendo el resultado de la evaluacion """ 
voy_al_cine_scary_movie = True
if voy_al_cine_scary_movie:
    print("Fui al cine a ver la peli")
else:
    print("No fui a ver la peli")

saldo = 1000
monto = 700

if (monto <= saldo):
    saldo = saldo - monto
    print(f"El saldo actual es: {saldo}")
    print("Pago realizado")
else: 
    print("Fondos insuficientes")

print("---------------------")

rol = "admin"

if rol == "admin":
    print("Acceso total")
elif rol == "editor":
    print("Acceso limitado")
else:
    print("Acceso basico")

print("---------------------")

print("Estructura de control match")
""" Uso match caudno lo que tengo que evaluar son datos conocidos.Opciones, roles, dia de la semana, etc """

rol_match = "editor"

match rol_match:
    case "admin":
        print("Acceso total")
    case "editor":
        print("Acceso limitado")
    case _:
        print("Acceso basico")

print("---------------------")

dia_semana = "sabado"

match dia_semana:
    case "lunes" | "martes" | "miercoles" | "jueves" | "viernes":
        print(f"{dia_semana} es un dia de semana")
    case "sabado" | "domingo":
        print(f"{dia_semana} es un dia fin de semana")
    case _:
        print(f"{dia_semana} no es un dia de la semana valido")

print("---------------------")

print("Listas")
#Almacenan varios valores: arreglo, array, vector.
#Listas homogeneas (mismo tipo de dato) -> recomendado
nombres = ["Pedro", "Carlos", "Ana"]
#             0          1         2
frutas = ["manzana", "banana", "naranja"]
numeros = [10, 20, 30, 40]

#Listas heterogeneas
datos = [25, "Maxi", 1.70, True]

#Lista vacia
lista_vacia = []
print(lista_vacia)

#Quiero imprimir la cadena 'manzana' por la consola
print(frutas[0]) #manzana
print(frutas[2]) #naranja

frutas[1] = "sandia"
print(frutas[1])
print(frutas)
print(len(frutas))
print("Ultimo elemento de la lista")
print(frutas[-1])
print(frutas[len(frutas)-1])

print("---------------------")

animales = ["tigre", "buho", "gato", "caballo", "vizcacha", "serpiente", "perro"]
print(animales)
print(len(animales))

animales[4] = "tortuga"
print(animales)

print("Recorro la lista")

for i in range(len(animales)):
    print(i, animales[i])

print("---------------------")

# Matrices
#           0        1
matriz = [[1, 2], [3, 4]]
#          0  1    0   1
print(matriz) 
print(matriz[1]) # [3, 4]
print(matriz[1][0]) # 3

print("Modifico 2 por 22")

matriz[0][1] = 22
print(matriz)

# Recorro filas
for fila in matriz:
    print(fila)

#Recorro filas y columnas
for fila in matriz:
    for valor in fila:
        print(valor)
