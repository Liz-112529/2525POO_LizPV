# Clase Producto: Representa cada artículo del inventario con atributos básicos.
# ==============================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Atributos principales de cada producto
        # El ID sirve como identificador único en el inventario
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        # Método especial para representar un producto como texto
        # Así, al imprimir un objeto Producto se ve información legible
        return f"{self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"


# Clase Inventario: Usa un diccionario (dict) en lugar de una lista.
# ==============================
class Inventario:
    def __init__(self):
        # Usamos un diccionario para almacenar los productos
        # Clave: ID del producto, Valor: Objeto Producto
        # Esto facilita buscar, eliminar o actualizar productos rápidamente
        self.productos = {}

    def agregar_producto(self, producto):
        # Verificamos si el ID ya existe para evitar duplicados
        if producto.id_producto in self.productos:
            print("Error: Producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto

    def eliminar_producto(self, id_producto):
        # Eliminamos un producto si su ID existe en el inventario
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Actualizamos cantidad y/o precio de un producto existente
        if id_producto in self.productos:
            if cantidad is not None:   # Si se pasa cantidad, la modificamos
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:    # Si se pasa precio, lo modificamos
                self.productos[id_producto].precio = precio
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        # Buscamos productos cuyo nombre contenga la palabra ingresada
        # Esto permite buscar incluso si no se escribe el nombre exacto
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto)

    def mostrar_inventario(self):
        # Muestra todos los productos registrados en el inventario
        if not self.productos:
            print("Inventario vacío.")
        else:
            print(f"{'ID':<10}{'Nombre':<20}{'Cantidad':<10}{'Precio':<10}")
            print("-" * 50)
        for producto in self.productos.values():
            print(f"{producto.id_producto:<10}{producto.nombre:<20}{producto.cantidad:<10}{producto.precio:<10.2f}")


# Interfaz de Usuario: Muestra un menú en consola.
# ==============================
def menu():
    inventario = Inventario()  # Se crea un inventario vacío al iniciar
    while True:
        # Menú principal con opciones disponibles
        print("\n1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '6':
            break   # Salir del programa
        elif opcion == '1':
            # Pedimos datos para crear un nuevo producto
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            # Eliminamos producto por ID
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            # Actualizamos cantidad o precio
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")

            # Si el usuario deja en blanco, no se actualiza ese atributo
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == '4':
            # Buscar producto por coincidencia en el nombre
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            # Mostrar todos los productos
            inventario.mostrar_inventario()


# ==============================
# Ejecutar el programa
# ==============================
if __name__ == "__main__":
    menu()
