from abc import ABC, abstractmethod

# Clase base que representa un Producto en general (Abstracción)
class Producto(ABC):
    def __init__(self, nombre, precio):
        self._nombre = nombre  # Encapsulamiento: atributo protegido
        self._precio = precio  # Encapsulamiento

    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio

    @abstractmethod
    def mostrar_detalle(self):
        pass  # Método abstracto para ser sobrescrito (Abstracción y Polimorfismo)


# Subclase para productos de tecnología (Herencia)
class ProductoTecnologia(Producto):
    def __init__(self, nombre, precio, marca):
        super().__init__(nombre, precio)
        self._marca = marca

    def mostrar_detalle(self):
        print(f"[Tecnología] {self._nombre} - Marca: {self._marca} - Precio: ${self._precio}")


# Subclase para productos de ropa (Herencia)
class ProductoRopa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def mostrar_detalle(self):
        print(f"[Ropa] {self._nombre} - Talla: {self._talla} - Precio: ${self._precio}")


# Clase Usuario que realiza compras
class Usuario:
    def __init__(self, nombre_usuario):
        self._nombre_usuario = nombre_usuario
        self._carrito = []  # Lista de productos (Encapsulamiento)

    def agregar_producto(self, producto):
        self._carrito.append(producto)
        print(f"Producto agregado al carrito: {producto.get_nombre()}")

    def mostrar_carrito(self):
        print(f"\nCarrito de {self._nombre_usuario}:")
        for producto in self._carrito:
            producto.mostrar_detalle()  # Polimorfismo en acción

    def total_compra(self):
        total = sum(producto.get_precio() for producto in self._carrito)
        print(f"Total a pagar: ${total:.2f}")
        return total


# Prueba del sistema
if __name__ == "__main__":
    # Crear productos
    laptop = ProductoTecnologia("Laptop Lenovo", 550.00, "Lenovo")
    camiseta = ProductoRopa("Camiseta oversize", 15.99, "M")
    auriculares = ProductoTecnologia("Auriculares Bluetooth", 38.50, "Xiaomi")

    # Crear usuario
    usuario1 = Usuario("liz2025")

    # Agregar productos al carrito
    usuario1.agregar_producto(laptop)
    usuario1.agregar_producto(camiseta)
    usuario1.agregar_producto(auriculares)

    # Mostrar contenido del carrito
    usuario1.mostrar_carrito()

    # Calcular total
    usuario1.total_compra()

