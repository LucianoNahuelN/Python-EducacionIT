""" Ejercicio Listas
Crear una lista de numeros y luego:
[10, 22, 55, 2, 88, 7]

- Imprimir cada numero | -> def imprimir numeros
- Calcular la suma de todos -> 10+22+55+2+88+7 | -> calcular la suma de todos
- Calcular el promedio -> (10+22+55+2+88+7)/cantidad-elementos | -> calcular el promedio de todos
- Mostar la suma de los numeros y el promedio | -> imprimir en pantalla
- El formato que necesito es el sgte:
    - La suma de los numeros dentro de la lista es: suma
    - El promedio de los numeros dentro de la lista es: promedio
 """

def imprimir_numeros(numeros):
    for numero in numeros:
        print(numero)

def calcular_suma(numeros):
    suma = 0
    for numero in numeros:
        suma += numero 
    return suma

def calcular_promedio(numeros):
    total = 0
    promedio = 0
    for numero in numeros:
        total += numero 
    promedio = round(total/len(numeros), 2) 
    return promedio

def imprimir_resultados(numeros):
     imprimir_numeros(numeros)
     print(f"La suma de los numeros dentro de la lista es: {calcular_suma(numeros)}")
     print(f"El promedio de los numeros dentro de la lista es: {calcular_promedio(numeros)}")


lista_uno = [10, 22, 55, 2, 88, 7]
lista_dos = [2, 45, 26, 13, 5, 70]

imprimir_resultados(lista_uno)
imprimir_resultados(lista_dos)

