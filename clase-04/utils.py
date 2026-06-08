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