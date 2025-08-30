from typing import Dict, Optional
from Producto import Producto
from GestionArchivo import GestionArchivo


class Inventario:
    def __init__(self, ruta_archivo: str = "inventario.txt"):
        self.storage = GestionArchivo(ruta_archivo)
        self.productos: Dict[str, Producto] = self.storage.cargar()

    # Agregar producto
    def agregar_producto(self, p: Producto) -> None:
        if p.get_id() in self.productos:
            print(" El ID ya existe. No se añadió el producto.")
            return
        self.productos[p.get_id()] = p
        if self.storage.guardar(self.productos):
            print(" Producto añadido y guardado en archivo.")
        else:
            print(" No se pudo guardar en archivo. El producto permanece en memoria.")

    # Eliminar producto
    def eliminar_producto(self, id_producto: str) -> None:
        if id_producto not in self.productos:
            print("❌ Producto no encontrado.")
            return
        del self.productos[id_producto]
        if self.storage.guardar(self.productos):
            print("✅ Producto eliminado y guardado en archivo.")
        else:
            print("⚠️ No se pudo guardar en archivo. Cambios solo en memoria.")

    # Actualizar producto
    def actualizar_producto(self, id_producto: str, cantidad: Optional[int] = None, precio: Optional[float] = None) -> None:
        if id_producto not in self.productos:
            print(" Producto no encontrado.")
            return
        p = self.productos[id_producto]
        if cantidad is not None:
            p.set_cantidad(cantidad)
        if precio is not None:
            p.set_precio(precio)
        if self.storage.guardar(self.productos):
            print(" Producto actualizado en archivo.")
        else:
            print(" No se pudo guardar en archivo. Cambios solo en memoria.")

    # Buscar producto
    def buscar_producto(self, nombre: str) -> None:
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            print("\n Productos encontrados:")
            for p in encontrados:
                print(f"- {p.get_id()} | {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: {p.get_precio()}")
        else:
            print(" No se encontraron productos con ese nombre.")

    # Mostrar inventario
    def mostrar_inventario(self) -> None:
        if not self.productos:
            print(" Inventario vacío.")
        else:
            print("\n Inventario actual:")
            for p in self.productos.values():
                print(f"- {p.get_id()} | {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: {p.get_precio()}")

    # Recargar desde archivo
    def recargar(self) -> None:
        self.productos = self.storage.cargar()
        print(" Inventario recargado desde archivo.")
