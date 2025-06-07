# Importamos las subclases desde sus respectivos módulos
from herencia.animal_terrestre import AnimalTerrestre  # Clase para animales terrestres
from herencia.animal_aereo import AnimalAereo          # Clase para animales aéreos

# --- CREACIÓN DE OBJETOS ---

# Creamos un objeto de tipo AnimalTerrestre
# Le pasamos nombre, edad y número de patas
perro = AnimalTerrestre("Benyi", 5, 4)

# Creamos un objeto de tipo AnimalAereo
# Le pasamos nombre, edad y distancia de vuelo
loro = AnimalAereo("Loro Pepe", 2, 3)

# --- DEMOSTRACIÓN DE POLIMORFISMO ---

# Aunque ambos objetos derivan de la clase Animal,
# se comportan de forma distinta al llamar a los mismos métodos
# gracias al polimorfismo (métodos sobrescritos en cada subclase)

# Usamos el método describir() heredado de la clase base Animal
perro.describir()           # Muestra nombre y edad del animal terrestre
perro.moverse()             # Muestra cómo se mueve un animal terrestre (camina)
perro.hacer_sonido()        # Muestra el sonido típico de un animal terrestre

print("-----------")         # Separador visual en la salida

# Repetimos para el animal aéreo
loro.describir()            # Muestra nombre y edad del animal aéreo
loro.moverse()              # Muestra cómo se mueve un animal aéreo (vuela)
loro.hacer_sonido()         # Muestra el sonido típico de un animal aéreo

# --- FIN DEL PROGRAMA ---

"""
Este archivo demuestra:
- La creación de instancias a partir de clases derivadas (AnimalTerrestre y AnimalAereo).
- La reutilización del código común desde la clase Animal (herencia).
- El uso de métodos sobrescritos en tiempo de ejecución (polimorfismo).
"""
