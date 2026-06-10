# Tkinder -> libreria para crear interfaces graficas
# esta dentro del propio lenguaje, no instalo nada

class Persona:
    """ Una clase es un molde para crear personas por ej """

    """ Constructor -> es un metodo por defecto q se ejecuta al instanciar la clase """
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        """ Un metodo es una accion q la persona puede hacer (comportamiento) """
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"

# Creamos 2 instancias a partir del molde

persona1 = Persona("Laura", 25) # una instancia de persona
persona2 = Persona("Eduymar", 20) # otra instancia de persona

print(persona1.presentarse())
print(persona2.presentarse())
