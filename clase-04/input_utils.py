# Controlo:
# 1- Que sea un numero
# 2- Que no sea una palabra
def pedir_gasto():
    while True:
        try:
            gasto = float(input("Ingrese un gasto(0 para terminar): "))
            if gasto < 0:
                print("Error: el gasto no puede ser negativo")
            return gasto
        except ValueError:
            print("Error: ingrese un numero valido.")