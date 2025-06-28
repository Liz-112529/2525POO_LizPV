# Programa para calcular el área de un triángulo dados su base y altura.
# El usuario ingresa los datos, el programa valida que sean números positivos
# y devuelve el área calculada. Se usan diferentes tipos de datos (int, float,
# str, bool) y se siguen las buenas prácticas de estilo y documentación.

def es_numero_positivo(valor):
    """
    Función que verifica si el valor ingresado puede convertirse en un número float positivo.
    Retorna True si es válido, de lo contrario False.
    """
    try:
        numero = float(valor)
        return numero > 0
    except ValueError:
        return False


def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo usando la fórmula: (base * altura) / 2
    Parámetros:
        base (float): La base del triángulo.
        altura (float): La altura del triángulo.
    Retorna:
        float: El área del triángulo.
    """
    return (base * altura) / 2


# Inicio del programa
print("CÁLCULO DEL ÁREA DE UN TRIÁNGULO")
print("---------------------------------")

# Pedir al usuario la base y la altura del triángulo
base_valida = False
altura_valida = False

# Obtener una base válida
while not base_valida:
    entrada_base = input("Ingrese la base del triángulo (en cm): ")
    base_valida = es_numero_positivo(entrada_base)
    if not base_valida:
        print("  Error: Ingrese un número positivo válido para la base.")

# Obtener una altura válida
while not altura_valida:
    entrada_altura = input("Ingrese la altura del triángulo (en cm): ")
    altura_valida = es_numero_positivo(entrada_altura)
    if not altura_valida:
        print("  Error: Ingrese un número positivo válido para la altura.")

# Convertir entradas a tipo float
base = float(entrada_base)
altura = float(entrada_altura)

# Calcular el área de un triángulo
area = calcular_area_triangulo(base, altura)

# Mostrar el resultado
print(f"\n✅ El área del triángulo con base {base} cm y altura {altura} cm es: {area:.2f} cm²")
