import os
import json
from typing import Dict
from Producto import Producto


class GestionArchivo:
    """
    Persistencia en JSON usando diccionario {id: {...}}.
    - cargar() -> Dict[str, Producto]
    - guardar(diccionario) -> bool
    """
    def __init__(self, ruta: str = "inventario.txt"):
        self.ruta = ruta
        if not os.path.exists(self.ruta):
            # Archivo inicial como diccionario vacío
            with open(self.ruta, "w", encoding="utf-8") as f:
                json.dump({}, f, indent=4, ensure_ascii=False)

    def cargar(self) -> Dict[str, Producto]:
        try:
            with open(self.ruta, "r", encoding="utf-8") as f:
                data = json.load(f)

            dproducto: Dict[str, Producto] = {}

            # Soporta tanto dict como list (compatibilidad hacia atrás)
            if isinstance(data, dict):
                iterable = data.items()
            elif isinstance(data, list):
                # Convertir lista de objetos a dict por id
                iterable = ((p.get("id") or p.get("id_producto"), p) for p in data)
            else:
                print("Formato JSON no reconocido. Iniciando inventario vacío.")
                return {}

            for idp, p in iterable:
                if not idp:
                    # Si no hay id, saltar ese registro
                    continue
                producto = Producto(
                    id_producto=str(p.get("id", idp)),
                    nombre=str(p.get("nombre", "")),
                    cantidad=int(p.get("cantidad", 0)),
                    precio=float(p.get("precio", 0.0))
                )
                dproducto[producto.get_id()] = producto

            return dproducto

        except Exception as e:
            print(f"Error leyendo {self.ruta}: {e}")
            return {}

    def guardar(self, dproducto: Dict[str, Producto]) -> bool:
        try:
            payload = {
                idp: {
                    "id": p.get_id(),
                    "nombre": p.get_nombre(),
                    "cantidad": p.get_cantidad(),
                    "precio": p.get_precio(),
                }
                for idp, p in dproducto.items()
            }
            with open(self.ruta, "w", encoding="utf-8") as f:
                json.dump(payload, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error escribiendo {self.ruta}: {e}")
            return False
