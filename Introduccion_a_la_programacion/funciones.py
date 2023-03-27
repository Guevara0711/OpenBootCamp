#Primera parte
#Crear una función con tres parámetros que sean números que se suman entre sí
def suma(num1, num2, num3):
    return num1 + num2 + num3

#Llamar a la función en el main y darle valores.
print(suma(20, 30, 50))

#segunda parte
#Crear una clase coche
class Coche():
    #Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene
    num_puertas = 4
    #Una función que incremente el número de puertas que tiene el coche
    def incrementar_puertas(self):
        self.num_puertas += 1
        return self.num_puertas


#Crear un objeto miCoche en el main y añadirle una puerta
miCoche = Coche()
miCoche.incrementar_puertas()

#Mostrar el número de puertas que tiene el objeto
print(miCoche.num_puertas)

    
