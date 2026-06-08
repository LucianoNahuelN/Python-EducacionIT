from errores import SaldoInsuficienteError

def retirar_dinero(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficienteError("No tenes saldo suficiente")
    return saldo - monto