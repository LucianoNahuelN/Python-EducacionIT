""" Ejercicio Listas
Crear una lista de numeros y luego:
[10, 22, 55, 2, 88, 7]

- Imprimir cada numero
- Calcular la suma de todos -> 10+22+55+2+88+7
- Calcular el promedio -> (10+22+55+2+88+7)/cantidad-elementos
- Mostar la suma de los numeros y el promedio
- El formato que necesito es el sgte:
    - La suma de los numeros dentro de la lista es: suma
    - El promedio de los numeros dentro de la lista es: promedio
 """

numeros = [10, 22, 55, 2, 88, 7]
total = 0
promedio = 0

for numero in numeros:
    print(numero)
    total += numero 
promedio = round(total/len(numeros), 2) 
print(f"La suma de los numeros dentro de la lista es: {total}")
print(f"El promedio de los numeros dentro de la lista es: {promedio}")



