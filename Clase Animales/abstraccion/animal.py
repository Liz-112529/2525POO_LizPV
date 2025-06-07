class Animal:
    """
    Clase base que representa un animal domésticoo.
    Esta clase aplica:
    - Abstracción: Define las características y comportamientos comunes a todos los animales.
    - Encapsulación: Protege los atributos usando doble guion bajo (__), para que no se acceda directamente desde fuera.
    """

    def __init__(self, nombre, edad):
        """
        Constructor de la clase Animal.
        :param nombre: Nombre del animal (string).
        :param edad: Edad del animal (entero).

        Se encapsulan los atributos con doble guion bajo (__), para evitar el acceso directo desde fuera de la clase.
        """
        self.__nombre = nombre  # Nombre del animal (atributo privado)
        self.__edad = edad  # Edad del animal (atributo privado)

    def obtener_nombre(self):
        """
        Método para acceder al nombre del animal.
        Devuelve el nombre almacenado en el atributo privado __nombre.
        """
        return self.__nombre

    def obtener_edad(self):
        """
        Método para acceder a la edad del animal.
        Devuelve la edad almacenada en el atributo privado __edad.
        """
        return self.__edad

    def describir(self):
        """
        Muestra una descripción básica del animal (nombre y edad).
        Utiliza los atributos encapsulados para imprimir la información.
        """
        print(f"{self.__nombre} tiene {self.__edad} años.")

    def moverse(self):
        """
        Método que representa el movimiento del animal.
        Es un comportamiento genérico que puede ser redefinido en clases hijas (polimorfismo).
        """
        print("El animal se mueve de alguna manera.")

    def hacer_sonido(self):
        """
        Método que representa el sonido que hace un animal.
        Este comportamiento es genérico y será sobreescrito por las subclases.
        """
        print("El animal hace un sonido.")

