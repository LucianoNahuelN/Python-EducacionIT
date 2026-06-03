""" Ejercicio Dos: 
Crear un programa que simule una maquina de cambios de divisas
El programa debe:
1- Pedir una cantidad de pesos Argentinos
2- Convertir en la moneda indicada (dolar o euro) [hits: condicioles (if, match)]
3- Mostrar cuantos dolares o euros puede comprar (concatenando)
    Ejemplos de omo se deberia ver en pantalla:
    3.1 Se veria: "COn 15000 pesos se compran 100 dolares
    3.2 Se veria: "Con 15000 pesos se comprar 100 euros """

monto = float(input("Ingrese su monto a cambiar en pesos: "))
moneda = input("Seleccione la moneda por la que desea cambiar dolar/euro: ").lower()

match moneda:
    case "dolar" | "dolares":
        cambio = round(monto / 1426.98, 2)
        print(f"Con {monto} pesos se compran {cambio} dolares")
    case "euro" | "euros":
        cambio = round(monto / 1655.43, 2)
        print(f"Con {monto} pesos se compran {cambio} euros")
    case _:
        print("La opcion ingresada no es correcta, indique la moneda en dolar o euro")

