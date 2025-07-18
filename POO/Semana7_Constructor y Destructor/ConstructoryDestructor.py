class Usuario:
    # Constructor: se ejecuta automáticamente al crear un nuevo objeto Usuario
    def __init__(self, nombre, edad, correo):
        # Se inicializan los atributos del usuario
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

        # Mensaje que simula el ingreso del usuario a la base de datos
        print(f"Usuario '{self.nombre}' ingresado a la base de datos.")
        print(f"   Edad: {self.edad} años | Correo: {self.correo}\n")

    # Destructor: se ejecuta automáticamente cuando el objeto se elimina
    def __del__(self):
        # Mensaje que simula la eliminación del usuario de la base de datos
        print(f"Usuario '{self.nombre}' eliminado de la base de datos.\n")


# Función que simula el proceso de ingreso de usuarios a una base de datos
def simulacion_base_datos():
    print("=== INICIO DE LA SIMULACIÓN ===\n")

    # Se crean dos objetos de tipo Usuario: aquí se activa automáticamente __init__
    usuario1 = Usuario("Victor Moreno", 25, "victor.moreno@example.com")
    usuario2 = Usuario("Lesly Castillo", 30, "lesly.castillo@example.com")

    # Mensaje adicional durante la simulación
    print(">> Usuarios activos...\n")
    print("Procesando datos...\n")

    # Al finalizar esta función, los objetos 'usuario1' y 'usuario2' salen del ámbito
    # y se eliminan automáticamente, lo que activa el método __del__.


# Llamada a la función que ejecuta la simulación
simulacion_base_datos()

# Mensaje final de cierre (los destructores ya se han ejecutado al salir de la función)
print("=== FIN DE LA SIMULACIÓN ===")

