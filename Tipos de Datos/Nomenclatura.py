# Programa para gestionar información básica de estudiantes
# Permite registrar nombre, edad, promedio y verificar si aprueban
# Uso de clases, subclases, tipos de datos, identificadores y convenciones

class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")


class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, promedio: float):
        super().__init__(nombre, edad)
        self.promedio = promedio
        self.aprobado = self.verificar_aprobacion()

    def verificar_aprobacion(self) -> bool:
        """Devuelve True si el promedio es mayor o igual a 7.0"""
        return self.promedio >= 7.0

    def mostrar_info(self):
        """Muestra toda la información del estudiante"""
        super().mostrar_info()
        print(f"Promedio: {self.promedio}")
        print(f"Aprobado: {self.aprobado}")


# --- Prueba del programa ---
def main():
    # Registro de un estudiante
    nombre_estudiante = "Liz Peña"
    edad_estudiante = 34
    promedio_estudiante = 9.5

    estudiante1 = Estudiante(nombre_estudiante, edad_estudiante, promedio_estudiante)

    print(" Información del estudiante:")
    estudiante1.mostrar_info()

if __name__ == "__main__":
    main()
