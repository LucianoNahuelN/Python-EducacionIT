print("Condicionales (Tomar deciciones)")

edad = 21

print("Inicio del programa")
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
print("Fin del programa")

# En python se trabaja identando nuestras sentencias cuando trabajamos con bloques

print("------------------------------")

print("If sin else")

if edad >= 18:
    print("Mayor de edad")
    print("Podes votar")
print("Fin del programa")

print("------------------------------")

print("3 caminos o mas con el if else -> elif")

nota = 8

if nota < 4:
    print("Desaprobado")
elif nota < 7:
    print("Aprobado")
elif nota < 9:
    print("Muy bien")
else:
    print("Excelente")

print("------------------------------")

print("Operadores logicos")

print("and (y logico)")

edad = 25
tiene_licencia = True

# 1    1 = 1 ----> ambas verdaderas 
# 1    0 = 0
# 0    1 = 0
# 0    0 = 0

if (edad >= 18 and tiene_licencia):
    print("Puedes manejar")
else:
    print("No puedes manejar")

