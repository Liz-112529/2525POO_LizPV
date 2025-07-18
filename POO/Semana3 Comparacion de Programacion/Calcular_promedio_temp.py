# Función para ingresar temperaturas diarias con nombre de día
def ingresar_temperaturas():
    # Ingresamos los dias de la semana
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = []

    print("Ingrese la temperatura correspondiente para cada día de la semana:")

    # Se pide al usuario ingresar la temperatura para cada día
    for dia in dias_semana:
        temp = float(input(f"{dia}: "))
        temperaturas.append(temp)
    #  Se retorna tanto la lista de temperaturas como la de días
    return temperaturas, dias_semana


# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    # Se suma todas las temperaturas y se las divide por la cantidad de días
    return sum(temperaturas) / len(temperaturas)


# Función principal del programa
def main():
    # Se obtienen las temperaturas ingresadas y los días de la semana
    temperaturas, dias = ingresar_temperaturas()

    # Muestra en la consola todas las temperaturas ingresadas junto con su día correspondiente
    print("\nTemperaturas registradas:")
    for i in range(7):
        print(f"{dias[i]}: {temperaturas[i]}°C")

    # Calculamos el promedio semanal de las temperaturas
    promedio = calcular_promedio(temperaturas)
    # Se imprime el resultado del promedio
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")


# Ejecutar el programa
main()
