# FUNCIONES
# Se usa la palabra reservada def en ves de function
# Evitan la repeticion de codigo
# Es una forma de guardar instrucciones con un nombre para poder reutilizar y modificar

print("Clase 03 - Funciones")

# ! Evita esto

""" print("Buen dia Juan")
print("Buen dia Ana")
print("Buen dia Pedro")
print("Buen dia Roberto") """

# ! Arquitectura de unma funcion

def saludar (persona_a_saludar):
    print(f"Hola {persona_a_saludar}")

saludar("Maxi")
saludar("Mauro")
saludar("Judith")
saludar("Lucia")

def sumar(a, b):
    print(a + b)

sumar(2, 5)
sumar(4, 8)
sumar(1, 4)
sumar(3, 5)

# ! Funciones que retornan un numero para poder reutilizarlo
""" 
Crear una funcion: 
- Reciba una lista de numeros
- Devuelva la suma
- Luego imprimir el resultado
 """
def sumar_lista(numeros):
    total = 0
    for n in numeros:
        total += n
        print(n)
    return total

lista_uno = [254, 23, 2, 5, 4, 45]
lista_dos = [32, 123, 42, 25, 34, 15]

resultado_uno = sumar_lista(lista_uno)
print(f"El total de la lista uno es: {resultado_uno}")
print("------------------------------")
resultado_dos = sumar_lista(lista_dos)
print(f"El total de la lista dos es: {resultado_dos}")

print("------------------------------")

""" 
Enunciado:
----------
Una persona anota los gastos del día en una lista de números

Se pide:
    - Guardar los gastos en una lista
    - Calcular el gasto total
    - Calcular el gasto promedio 
    - Mostrar ambos valores por pantalla
 """

# MVC
gastos = [1200, 650, 850, 450] # Modelos

# Controlador
total = sum(gastos)
cant_elementos = len(gastos)
promedio = total / cant_elementos

# Vista
print("Gasto total:", total)
print("Gasto promedio:", promedio)

""" 
Enunciado:
----------
Una persona anota los gastos del día en una lista de números

Se debe:
    - verificar que la lista no esté vacía
    - Verificar que no haya valores negativos
    - Calcular el gasto total si los datos son válidos
    - Calcular el gasto promedio si los datos son válidos
    - Mostrar ambos valores por pantalla
"""

gastos = [1200, 650, 850, 450]
cant_elementos = len(gastos)
val_minimo = min(gastos)

if cant_elementos == 0:
    print("No hay gastos cargados")
elif val_minimo < 0:
    print("Error: hay gastos negativos.")
else: 
    total = sum(gastos)
    promedio = total / cant_elementos
    print("Gasto total:", total)
    print("Gastos promedio:", promedio)


print("------------------------------")

""" El usuario debe ingresar gastos uno por uno 
El ingreso termina cuando escribe 0
El programa debe:
    - Repetir el pedido mientras el gasto sea valido
    - No aceptar numeros negativos
    - Calcular total y promedio """

""" gastos = []
while True:
    gasto = float(input("Ingrese un gasto(0 para terminar): "))
    if gasto == 0:
        print("Entro al break")
        break #me saca del ciclo


    if gasto == 250:
        print("Entro al continue")
        continue #me saca de la iteracion actual

    print("Siguiente iteracion")

print("Fin") """


""" gastos = []
while True:
    gasto = float(input("Ingrese un gasto(0 para terminar): "))
    if gasto == 0:
        break #me saca del ciclo
    elif gasto < 0:
        print("Error: el gasto no puede ser negativo")
    else:
        gastos.append(gasto)

    if len(gastos) == 0:
        print("No se cargaron datos")
    else:
        total = sum(gastos)
        promedio = total / len(gastos)
        print("Gasto total: ", total)
        print("Gasto promedio: ", promedio) """

gastos = []
def agregar_gasto_lista(gasto):
    gastos.append(gasto)

def cantidad_elementos(gastos):
    cant_elementos = len(gastos)
    return cant_elementos

def calcular_total_gastos(gastos):
    total = sum(gastos)
    return total

def calcular_promedio_gastos(total, cant_elementos):
    promedio = total / cant_elementos
    return promedio

def mostrar_total(total):
    print(f"Gasto total: {total}")

def  mostrar_promedio(promedio):
    print(f"Gasto promedio: {promedio}")

while True:
    gasto = float(input("Ingrese un gasto(0 para terminar): "))
    if gasto == 0:
        break #me saca del ciclo
    elif gasto < 0:
        print("Error: el gasto no puede ser negativo")
    else:
       agregar_gasto_lista(gasto)

    if cantidad_elementos(gastos) == 0:
        print("No se cargaron datos")
    else:
        total = calcular_total_gastos(gastos)
        cant_elementos = cantidad_elementos(gastos)
        promedio = calcular_promedio_gastos(total, cant_elementos)
        

mostrar_total(total)
mostrar_promedio(promedio)