# ===============================
# Sistema de Gestión de Biblioteca Digital
# ===============================

from typing import Dict, List, Set, Tuple


class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos una tupla para (titulo, autor) porque son inmutables
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} de {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre: str, user_id: str):
        self.nombre: str = nombre
        self.user_id: str = user_id
        self.libros_prestados: List[Libro] = []

    def __str__(self):
        return f"{self.nombre:<20} {self.user_id:<10} {len(self.libros_prestados):<5} libros prestados"


class Biblioteca:
    def __init__(self):
        self.libros = {}      # Diccionario: ISBN -> Libro
        self.usuarios = {}    # Diccionario: ID -> Usuario
        self.user_ids = set() # Conjunto para IDs únicos

    # -----------------------------
    # Gestión de libros
    # -----------------------------
    def añadir_libro(self, libro: Libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"{libro.info[0]:<30} {libro.info[1]:<20} {libro.categoria:<15} {libro.isbn:<10}")
        else:
            print(f"⚠️ El libro con ISBN {libro.isbn} ya está en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            libro = self.libros.pop(isbn)
            print(f" Libro eliminado: {libro}")
        else:
            print(" No se encontró el libro con ese ISBN.")

    # -----------------------------
    # Gestión de usuarios
    # -----------------------------
    def registrar_usuario(self, usuario: Usuario):
        if usuario.user_id not in self.user_ids:
            self.usuarios[usuario.user_id] = usuario
            self.user_ids.add(usuario.user_id)
            print(f"{usuario.nombre:<20} {usuario.user_id:<10} registrado correctamente.")
        else:
            print(f"⚠️ El ID de usuario {usuario.user_id} ya está registrado.")

    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            usuario = self.usuarios.pop(user_id)
            self.user_ids.remove(user_id)
            print(f" Usuario eliminado: {usuario.nombre} (ID: {usuario.user_id})")
        else:
            print(" No se encontró el usuario.")

    # -----------------------------
    # Préstamos
    # -----------------------------
    def prestar_libro(self, user_id, isbn):
        if user_id not in self.usuarios:
            print(" Usuario no registrado.")
            return
        if isbn not in self.libros:
            print(" Libro no disponible en la biblioteca.")
            return

        usuario = self.usuarios[user_id]
        libro = self.libros.pop(isbn)
        usuario.libros_prestados.append(libro)
        print(f" Libro prestado: {libro.info[0]} a {usuario.nombre}")

    def devolver_libro(self, user_id, isbn):
        if user_id not in self.usuarios:
            print(" Usuario no registrado.")
            return

        usuario = self.usuarios[user_id]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro
                print(f" Libro devuelto: {libro.info[0]}")
                return
        print(" El usuario no tiene prestado este libro.")

    # -----------------------------
    # Listar libros prestados
    # -----------------------------
    def listar_libros_prestados(self, user_id):
        if user_id not in self.usuarios:
            print(" Usuario no registrado.")
            return

        usuario = self.usuarios[user_id]
        if usuario.libros_prestados:
            print(f"\n Libros prestados a {usuario.nombre}:")
            print(f"{'Título':<30} {'Autor':<20} {'Categoría':<15} {'ISBN':<10}")
            print("-" * 80)
            for libro in usuario.libros_prestados:
                print(f"{libro.info[0]:<30} {libro.info[1]:<20} {libro.categoria:<15} {libro.isbn:<10}")
        else:
            print(f" El usuario {usuario.nombre} no tiene libros prestados.")

    # -----------------------------
    # Búsqueda
    # -----------------------------
    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)

        if resultados:
            print("\n Resultados de la búsqueda:")
            print(f"{'Título':<30} {'Autor':<20} {'Categoría':<15} {'ISBN':<10}")
            print("-" * 80)
            for libro in resultados:
                print(f"{libro.info[0]:<30} {libro.info[1]:<20} {libro.categoria:<15} {libro.isbn:<10}")
        else:
            print(" No se encontraron libros con ese criterio.")

    # -----------------------------
    # Catálogo completo (disponibles + prestados)
    # -----------------------------
    def mostrar_catalogo_completo(self):

        print(f"{'Título':<30} {'Autor':<20} {'Categoría':<15} {'ISBN':<10} {'Estado':<20}")
        print("-" * 95)

        # Libros disponibles
        for libro in self.libros.values():
            print(f"{libro.info[0]:<30} {libro.info[1]:<20} {libro.categoria:<15} {libro.isbn:<10} {'Disponible':<20}")

        # Libros prestados
        for usuario in self.usuarios.values():
            for libro in usuario.libros_prestados:
                estado = f"Prestado a {usuario.nombre}"
                print(f"{libro.info[0]:<30} {libro.info[1]:<20} {libro.categoria:<15} {libro.isbn:<10} {estado:<20}")

# ===============================
# PRUEBA DEL SISTEMA
# ===============================
if __name__ == "__main__":
    # Crear la biblioteca
    biblio = Biblioteca()

    print(" "*80)
    print(" SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL".center(80))
    print(" "*80)

    # Crear libros
    libro1 = Libro("La odisea", "Homero", "Poema épico", "112529")
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", "192506")
    libro3 = Libro("Python para Todos", "Raúl González", "Programación", "11223")

    # Mostrar encabezado para libros añadidos
    print("\n=== Añadiendo libros ===")
    print(f"{'Título':<30} {'Autor':<20} {'Categoría':<15} {'ISBN':<10}")
    print("-"*80)

    biblio.añadir_libro(libro1)
    biblio.añadir_libro(libro2)
    biblio.añadir_libro(libro3)

    # Crear y registrar usuarios
    print("\n=== Registrando usuarios ===")
    user1 = Usuario("Andrea", "U001")
    user2 = Usuario("Charlie", "U002")
    print(f"{'Nombre':<20} {'ID':<10} {'Libros prestados':<5}")
    print("-"*40)
    biblio.registrar_usuario(user1)
    biblio.registrar_usuario(user2)

    # Préstamos
    print("\n=== Préstamos de libros ===")
    biblio.prestar_libro("U001", "112529")
    biblio.prestar_libro("U002", "192506")

    # Listado de libros prestados
    print("\n=== Listado de libros prestados ===")
    biblio.listar_libros_prestados("U001")

    # Devolución de libro
    print("\n=== Devolución de libro ===")
    biblio.devolver_libro("U001", "112529")

    # Búsqueda por categoría
    print("\n=== Búsqueda de libros por categoría ===")
    biblio.buscar_libros("categoria", "programación")

    # Catálogo completo
    print("\n=== Catálogo completo de la biblioteca ===")
    biblio.mostrar_catalogo_completo()

    print(" "*80)
    print(" Fin de la prueba del sistema".center(80))
    print(" "*80)
