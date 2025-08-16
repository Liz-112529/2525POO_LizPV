# Clase base: Empleado
# Representa un empleado genérico. Servirá como clase padre (superclase) para otras clases más específicas.
class Empleado:
    def __init__(self, nombre, salario):
        # Encapsulamiento: el salario se define como un atributo protegido (_salario).
        # Aunque no es completamente privado, se indica que no debe ser accedido directamente desde fuera de la clase.
        self.nombre = nombre
        self._salario = salario

    # Método para mostrar información general del empleado
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Salario: ${self._salario}")

    # Método para calcular el bono base (puede ser sobrescrito en clases hijas)
    def calcular_bono(self):
        return self._salario * 0.10


# Clase (hija 1): Programador
# HERENCIA: Hereda de la clase Empleado
class Programador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        # Llamamos al constructor de la clase base con super()
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    # POLIMORFISMO: sobrescribimos el método mostrar_informacion con un comportamiento específico
    def mostrar_informacion(self):
        print(f"Programador: {self.nombre}, Lenguaje: {self.lenguaje}, Salario: ${self._salario}")

    # POLIMORFISMO: sobrescribimos el cálculo del bono para programadores
    def calcular_bono(self):
        return self._salario * 0.20


# Clase (hija 2): Gerente
# HERENCIA: también hereda de la clase Empleado
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    # POLIMORFISMO: sobrescribimos mostrar_informacion para mostrar más detalles específicos
    def mostrar_informacion(self):
        print(f"Gerente: {self.nombre}, Departamento: {self.departamento}, Salario: ${self._salario}")

    # POLIMORFISMO: cálculo del bono diferente para gerentes
    def calcular_bono(self):
        return self._salario * 0.30


# Función principal del programa
def main():
    empleados = []  # Lista para almacenar objetos de tipo Empleado, Programador o Gerente

    while True:
        print("\n--- Registro de Empleado ---")
        tipo = input("Tipo de empleado (Programador/Gerente): ").strip().lower()
        nombre = input("Nombre: ")
        salario = float(input("Salario: "))

        # Dependiendo del tipo de empleado, creamos una instancia de la clase correspondiente
        if tipo == "programador":
            lenguaje = input("Lenguaje de programación: ")
            emp = Programador(nombre, salario, lenguaje)  # Instancia de clase derivada Programador

        elif tipo == "gerente":
            departamento = input("Departamento: ")
            emp = Gerente(nombre, salario, departamento)  # Instancia de clase derivada Gerente

        else:
            print("Tipo inválido. Intenta de nuevo.")
            continue

        empleados.append(emp)  # Agregamos el objeto a la lista

        continuar = input("¿Deseas agregar otro empleado? (s/n): ")
        if continuar.lower() != "s":
            break

    # Mostramos la información y bono de cada empleado
    print("\n=== Reporte de Empleados Registrados ===")
    for emp in empleados:
        # POLIMORFISMO: Aunque usamos el mismo método, el comportamiento depende de la clase del objeto
        emp.mostrar_informacion()
        print(f"Bono: ${emp.calcular_bono()}\n")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
