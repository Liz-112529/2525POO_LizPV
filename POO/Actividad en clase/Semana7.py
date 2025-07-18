class Vehiculo:
    def __init__(self):
        print("Un vehículo ha ingresado al parqueadero.")

    def __del__(self):
        print("Un vehículo ha salido del parqueadero.")


# Simulación
def simulacion_parqueadero():
    print("=== Inicio del parqueadero ===\n")

    v1 = Vehiculo()

    print("\n>> Vehículos estacionados...\n")

    del v1

    print("\n=== Fin de la simulación ===")


simulacion_parqueadero()
