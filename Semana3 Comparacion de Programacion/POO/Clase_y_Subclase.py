# Clase base que representa la temperatura de un día
class DiaClima:
    """Clase que representa la temperatura de un día específico."""

    def __init__(self, dia, temperatura=0.0):
        self._dia = dia  # Encapsulamiento del nombre del día
        self._temperatura = temperatura  # Encapsulamiento de la temperatura

    def set_temperatura(self, temperatura):
        """Asigna una nueva temperatura al día."""
        self._temperatura = temperatura

    def get_temperatura(self):
        """Retorna la temperatura del día."""
        return self._temperatura

    def get_dia(self):
        """Retorna el nombre del día."""
        return self._dia

    def __str__(self):
        """Representación en texto del día y su temperatura."""
        return f"{self._dia}: {self._temperatura}°C"


# Subclase para representar días especiales (ej. fines de semana)
class DiaEspecial(DiaClima):
    """Subclase que representa un día especial (ej. fin de semana)."""

    def __str__(self):
        """Representación modificada para resaltar días especiales."""
        return f"{self._dia} (Especial): {self._temperatura}°C"


# Clase que agrupa todos los días de la semana
class SemanaClima:
    """Clase que representa una semana con temperaturas diarias."""

    def __init__(self):
        # Lista con los días reales de la semana
        nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        # Se utiliza la subclase para Sábado y Domingo (demostrando herencia/polimorfismo)
        self.dias = []
        for nombre in nombres_dias:
            if nombre in ["Sábado", "Domingo"]:
                self.dias.append(DiaEspecial(nombre))
            else:
                self.dias.append(DiaClima(nombre))

    def ingresar_datos(self):
        """Solicita al usuario que ingrese la temperatura de cada día."""
        print("Ingrese la temperatura de cada día de la semana:")
        for dia in self.dias:
            temp = float(input(f"{dia.get_dia()}: "))
            dia.set_temperatura(temp)

    def calcular_promedio(self):
        """Calcula el promedio de temperatura semanal."""
        total = sum(dia.get_temperatura() for dia in self.dias)
        return total / len(self.dias)

    def mostrar_resumen(self):
        """Muestra todas las temperaturas ingresadas, día por día."""
        print("\nResumen semanal de temperaturas:")
        for dia in self.dias:
            print(dia)

    def obtener_dia_mas_caluroso(self):
        """Devuelve el día con la temperatura más alta."""
        return max(self.dias, key=lambda d: d.get_temperatura())

    def obtener_dia_mas_frio(self):
        """Devuelve el día con la temperatura más baja."""
        return min(self.dias, key=lambda d: d.get_temperatura())


# Función principal que coordina el flujo del programa
def main():
    semana = SemanaClima()  # Crear objeto SemanaClima
    semana.ingresar_datos()  # Ingresar datos por método de la clase
    semana.mostrar_resumen()  # Mostrar temperaturas
    promedio = semana.calcular_promedio()  # Calcular promedio usando método de la clase
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

    # Mostrar días con extremos de temperatura (uso de métodos adicionales)
    dia_max = semana.obtener_dia_mas_caluroso()
    dia_min = semana.obtener_dia_mas_frio()
    print(f"Día más caluroso: {dia_max}")
    print(f"Día más frío: {dia_min}")

# Ejecutar el programa
main()
