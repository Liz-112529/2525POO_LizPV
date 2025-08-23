import csv
from typing import List
from Producto import Producto


class GestiondeInventario:
    def __init__(self, ruta_archivo: str = "inventario.csv"):
        self.ruta_archivo = ruta_archivo

    def guardar(self, productos: List[Producto]) -> bool:
        """Guarda la lista de productos en el archivo CSV."""
        try:
            with open(self.ruta_archivo, mode="w", newline="", encoding="utf-8") as archivo:
                writer = csv.writer(archivo)
                # Escribir cabecera
                writer.writerow(["id_producto", "nombre", "cantidad", "precio"])
                # Escribir productos
                for p in productos:
                    writer.writerow([p.id_producto, p.nombre, p.cantidad, p.precio])
            return True
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")
            return False

    def cargar(self) -> List[Producto]:
        """Carga los productos desde el archivo CSV."""
        productos: List[Producto] = []
        try:
            with open(self.ruta_archivo, mode="r", newline="", encoding="utf-8") as archivo:
                reader = csv.DictReader(archivo)
                for row in reader:
                    producto = Producto(
                        id_producto=row["id_producto"],
                        nombre=row["nombre"],
                        cantidad=int(row["cantidad"]),
                        precio=float(row["precio"])
                    )
                    productos.append(producto)
        except FileNotFoundError:
            print("El archivo no existe todavía, se iniciará inventario vacío.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")
        return productos
