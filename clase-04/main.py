from utils import cantidad_elementos, calcular_promedio_gastos, calcular_total_gastos, mostrar_promedio, mostrar_total
from input_utils import pedir_gasto

print("Clase-04 Introduccion a Python")   

""" gastos = []
total = 0
promedio = 0
gasto = None

def agregar_gasto_lista(gasto):
    gastos.append(gasto)

while gasto != 0:
    gasto = pedir_gasto()
    
    if gasto != 0:
        agregar_gasto_lista(gasto)


if not gastos:
    print("No se cargaron datos")   
else:
    total = calcular_total_gastos(gastos)
    cant_elementos = cantidad_elementos(gastos)
    promedio = calcular_promedio_gastos(total, cant_elementos)
        

mostrar_total(total)
mostrar_promedio(promedio) """

# ! Gestion de errores
# Errores de sintaxis
## El programa no arranca con estos errores
# Falta :
""" 
if True
    print("Hola")
"""

## Errores en tiempo de ejecucion
# Arranca pero explota
""" print(10 / 0) """

##  Erorres logicos
# Deopende de nosotros. Bugs
# Faltan ()
""" 
precio = 100
descuento = 20
total = precio - descuento / 100 
"""

# ! TRY / EXCEPT

# ! Divido por cero
""" print("Inicio del programa")
try:
    # todo lo que quiero q se ejecute va dentro del try
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    # En caso de error, ejecuta lo que va dentro de except
    print("Error: No se puede dividir por cero")
print("Fin del programa") """

# ! Ingreso caracter a la division 
""" print("Inicio del programa")
try:
    numero = int(input("Ingrese un numero: "))
    print(10 / numero)
except ZeroDivisionError:
    print("No se puede div por cero")
except ValueError:
    print("Ingreso un valor invalido")
print("Fin del programa") """

# ! Generalizado
""" print("Inicio del programa")
try:
    numero = int(input("Ingrese un numero: "))
    print(10 / numero)
except:
    print("No es correcto lo que ingresaste")
print("Fin del programa") """

# ! ELSE Y FINALLY
# else: lo q esta en el cuerpo del else se ejecuta si el bloque try esta bien y no falla

""" try: 
    x = int("5") # si sale todo bien
    print(x)
except ValueError:
    print("Error")
else:
    print('Se pudo castear ese "5" a un entero: ', x) """

# finally: no importa lo q ocurra en try, siempre se ejecuta el finally

""" try:
    print(10 / 0)
except ZeroDivisionError:
    print("No se puede div por cero")
finally:
    print("Esto se ejecuta sin importar si hay excepcion o no. Siempre")
 """

#! ERRORES PERSONALIZADOS
# Es un error q creamos nosotros mismos para una tarea especifica

# EdadInvalidaError.py
# ? IMPORTANTE: todos los errores heredan de Exception

class EdadInvalidaError(Exception):
    pass 

# raise -> palabra reservada para lanzar una excepcion
# validar_edad.py

def validad_edad(edad):
    if (edad < 0):
        raise EdadInvalidaError("La edad no puede ser negativa")
    return edad

# main.py

try: 
    edad = int(input("Ingrese su edad: "))
    edad_validada = validad_edad(edad)
    print("Edad validada: ", edad_validada)
except EdadInvalidaError as e:
    print("Error: ", e)
except ValueError:
    print("Eso no es un numero")