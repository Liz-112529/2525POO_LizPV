# Importamos la clase base Animal desde el módulo abstraccion.animal
from abstraccion.animal import Animal


class AnimalAereo(Animal):
    """
    Clase que representa a un animal que se desplaza por el aire.

    Hereda de la clase Animal y sobrescribe algunos de sus métodos.
    Aplica:
    - Herencia: Extiende el comportamiento general de la clase Animal.
    - Encapsulación: Protege el atributo 'distancia' usando doble guion bajo (__).
    - Polimorfismo: Redefine los métodos 'moverse' y 'hacer_sonido' para animales aéreos.
    """

    def __init__(self, nombre, edad, distancia):
        """
        Constructor de la clase AnimalAereo.
        :param nombre: Nombre del animal (heredado de Animal).
        :param edad: Edad del animal (heredado de Animal).
        :param distancia: Distancia que puede volar el animal (en metros).

        Llama al constructor de la clase padre usando super() para inicializar nombre y edad.
        """
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.__distancia = distancia  # Atributo privado que representa la distancia de vuelo

    def obtener_distancia(self):
        """
        Método de acceso (getter) para obtener la distancia de vuelo.
        Devuelve el valor del atributo encapsulado __distancia.
        """
        return self.__distancia

    def moverse(self):
        """
        Sobrescribe el método moverse de la clase base.
        Muestra cómo se mueve un animal aéreo, indicando la distancia que puede volar.
        """
        print(f"{self.obtener_nombre()} vuela con una distancia de {self.__distancia} metros.")

    def hacer_sonido(self):
        """
        Sobrescribe el método hacer_sonido de la clase base.
        Muestra el tipo de sonido que típicamente haría un animal aéreo.
        """
        print(f"{self.obtener_nombre()} hace un sonido aéreo (canta, habla, etc).")

