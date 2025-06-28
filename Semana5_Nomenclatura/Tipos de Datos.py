# Programa para gestionar compras en la casa Comercial RM
# Este programa usa Programación Orientada a Objetos (POO)
# Aplica: Abstracción, Herencia, Encapsulamiento
# Utiliza: Tipos de datos (str, int, float, bool)

# --------------------------
# Clase base: Persona
# --------------------------
class Persona:
    """
    Clase base que representa a una persona (ABSTRACCIÓN).
    Se usa como modelo general para clientes u otras personas.
    """

    def __init__(self, nombre: str, edad: int):
        """
        Constructor de la clase Persona.
        - nombre: str (tipo de dato string)
        - edad: int (tipo de dato entero)
        Se usan atributos encapsulados (prefijo _).
        """
        self._nombre = nombre          # Atributo privado (ENCAPSULAMIENTO)
        self._edad = edad              # Atributo privado

    def mostrar_datos_persona(self):
        """
        Método que imprime los datos personales.
        """
        print(f"Nombre: {self._nombre}")
        print(f"Edad: {self._edad}")


# --------------------------
# Subclase: Cliente (HERENCIA)
# --------------------------
class Cliente(Persona):
    """
    Clase que representa a un cliente que realiza una compra.
    Hereda de Persona (HERENCIA).
    Contiene lógica para aplicar descuentos según la compra.
    """

    def __init__(self, nombre: str, edad: int, total_compra: float):
        """
        Constructor del Cliente.
        - nombre: str
        - edad: int
        - total_compra: float
        Usa super() para heredar atributos de Persona.
        """
        super().__init__(nombre, edad)              # HERENCIA
        self._total_compra = total_compra           # Atributo privado (float)
        self._descuento_aplicado = self._verificar_descuento()  # boolean

    def _verificar_descuento(self) -> bool:
        """
        Método privado que determina si el cliente recibe descuento.
        Si la compra es mayor o igual a 100, aplica un 15%.
        Devuelve: True o False (tipo de dato boolean).
        """
        return self._total_compra >= 100.0

    def calcular_total_con_descuento(self) -> float:
        """
        Calcula el total con descuento si corresponde.
        Si aplica, se descuenta el 15% (0.15).
        Retorna: total a pagar (float).
        """
        if self._descuento_aplicado:
            return self._total_compra - (self._total_compra * 0.15)
        return self._total_compra

    def mostrar_info_cliente(self):
        """
        Muestra toda la información del cliente:
        datos personales, total de la compra, si aplica descuento
        y total a pagar final.
        """
        self.mostrar_datos_persona()
        print(f"Total de la compra: ${self._total_compra:.2f}")
        print(f"Descuento aplicado: {self._descuento_aplicado}")  # bool
        print(f"Total a pagar: ${self.calcular_total_con_descuento():.2f}")


# --------------------------
# Función principal
# --------------------------
def main():
    """
    Función principal del programa.
    Crea un cliente con datos fijos y muestra su información.
    """
    # Tipos de datos utilizados: str, int, float
    nombre_cliente = "Liz Peña"        # str
    edad_cliente = 34                  # int
    valor_compra = 256.75              # float

    # Crear objeto de tipo Cliente
    cliente1 = Cliente(nombre_cliente, edad_cliente, valor_compra)

    print("🧾 Información del Cliente:")
    cliente1.mostrar_info_cliente()


# Ejecuta el programa si este archivo es el principal
if __name__ == "__main__":
    main()