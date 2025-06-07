# Importamos la clase base Animal desde el módulo abstraccion.animal
from abstraccion.animal import Animal


class AnimalTerrestre(Animal):
    """
    Clase que representa a un animal terrestre.

    Hereda de la clase Animal y especializa su comportamiento para animales que caminan.

    Aplica:
    - Herencia: Extiende la clase Animal.
    - Encapsulación: Protege el atributo 'num_patas' con doble guion bajo (__).
    - Polimorfismo: Sobrescribe los métodos 'moverse' y 'hacer_sonido'.
    """

    def __init__(self, nombre, edad, num_patas):
        """
        Constructor de la clase AnimalTerrestre.
        :param nombre: Nombre del animal (heredado de Animal).
        :param edad: Edad del animal (heredado de Animal).
        :param num_patas: Número de patas que tiene el animal terrestre.

        Utiliza super() para inicializar los atributos de la clase base.
        """
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base Animal
        self.__num_patas = num_patas  # Atributo privado que representa el número de patas

    def obtener_num_patas(self):
        """
        Método para acceder al número de patas del animal.
        Devuelve el valor del atributo privado __num_patas.
        """
        return self.__num_patas

    def moverse(self):
        """
        Sobrescribe el método moverse de la clase base.
        Especifica cómo se mueve un animal terrestre, indicando el número de patas.
        """
        print(f"{self.obtener_nombre()} camina con {self.__num_patas} patas.")

    def hacer_sonido(self):
        """
        Sobrescribe el método hacer_sonido de la clase base.
        Especifica el tipo de sonidos que haría un animal terrestre.
        """
        print(f"{self.obtener_nombre()} hace un sonido terrestre (ladra, ruge, etc).")

