
class Persona:
    def __init__(self, edad, nombre, telefono):
        self.__edad = edad
        self.__nombre = nombre
        self.__telefono = telefono

    def getEdad(self):
        return self.__edad
    def setEdad(self, edad):
        self.__edad = edad
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
    def getTelefono(self):
        return self.__telefono
    def setTelefono(self, telefono):
        self.__telefono = telefono

if __name__ == "__main__":
    persona = Persona(21, "Pedro", 666666666)
    persona.setEdad(21)
    persona.setNombre("Pedro")
    persona.setTelefono("6666""-""6666")

    print("Nombre: ", persona.getNombre())
    print("Edad: ", persona.getEdad())
    print("Telefono: ", persona.getTelefono())