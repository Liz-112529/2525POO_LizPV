"""
Agenda Personal - Tkinter
Archivo: agenda_tkinter.py
Descripcion: Aplicacion GUI que permite agregar, ver y eliminar eventos o tareas programadas.

Esta versión intenta importar `tkcalendar.DateEntry` (para un selector de fecha gráfico).
Si `tkcalendar` NO está instalado, el script usa un DateEntry de respaldo simple (un Entry
prellenado con la fecha actual en formato YYYY-MM-DD). De ese modo NO obtendrás
`ModuleNotFoundError` y podrás ejecutar la aplicación sin dependencias externas.

"""

import tkinter as tk
from tkinter import ttk, messagebox
import uuid
from datetime import date, datetime

# Intentar importar tkcalendar.DateEntry; si falla, definimos un DateEntry de respaldo
try:
    from tkcalendar import DateEntry  # si está disponible, usaremos el DateEntry gráfico
    TKCALENDAR_AVAILABLE = True
except Exception:
    TKCALENDAR_AVAILABLE = False

    class DateEntry(ttk.Entry):
        """Clase de respaldo mínima que se comporta como un Entry prellenado con la fecha actual.
        No muestra un calendario emergente; solo facilita capturar una fecha por texto.
        Formato esperado: YYYY-MM-DD
        """
        def __init__(self, master=None, date_pattern='yyyy-mm-dd', **kwargs):
            super().__init__(master, **kwargs)
            self.date_pattern = date_pattern
            # Insertar fecha de hoy como valor por defecto
            self.insert(0, date.today().strftime('%Y-%m-%d'))


class AgendaApp:
    """Clase principal de la aplicación Agenda Personal."""

    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal de Liz")
        self.root.geometry("700x450")
        self.root.resizable(False, False)

        # Lista interna de eventos (cada evento es un dict)
        self.eventos = []

        # --- Contenedores (Frames) para organizar la interfaz ---
        # Frame superior: muestra la lista de eventos
        self.frame_lista = ttk.Frame(self.root, padding=(10, 10))
        self.frame_lista.pack(fill=tk.BOTH, expand=True)

        # Frame medio: campos de entrada (fecha, hora, descripcion)
        self.frame_entrada = ttk.Frame(self.root, padding=(10, 0))
        self.frame_entrada.pack(fill=tk.X)

        # Frame inferior: botones de acciones
        self.frame_acciones = ttk.Frame(self.root, padding=(10, 10))
        self.frame_acciones.pack(fill=tk.X)

        # Construir componentes
        self._construir_treeview()
        self._construir_campos_entrada()
        self._construir_botones()

    def _construir_treeview(self):
        """Construye el Treeview que muestra los eventos."""
        columnas = ("fecha", "hora", "descripcion")

        self.tree = ttk.Treeview(self.frame_lista, columns=columnas, show="headings", height=10)
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")

        # Ajuste de anchos de columna
        self.tree.column("fecha", width=120, anchor=tk.CENTER)
        self.tree.column("hora", width=80, anchor=tk.CENTER)
        self.tree.column("descripcion", width=440, anchor=tk.W)

        # Scrollbar vertical
        vsb = ttk.Scrollbar(self.frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Doble clic en fila -> ver detalles (opcional)
        self.tree.bind("<Double-1>", self._on_doble_click)

    def _construir_campos_entrada(self):
        """Construye los campos de entrada con etiquetas y widgets.
        Se utiliza DateEntry (tkcalendar) cuando está disponible; de lo contrario
        se usa el DateEntry de respaldo definido más arriba.
        """
        # Etiqueta y DateEntry para la fecha
        lbl_fecha = ttk.Label(self.frame_entrada, text="Fecha:")
        lbl_fecha.grid(row=0, column=0, padx=(0, 6), pady=8, sticky=tk.W)

        # Usamos el DateEntry (gráfico si está tkcalendar, o Entry simple si no)
        if TKCALENDAR_AVAILABLE:
            self.entry_fecha = DateEntry(self.frame_entrada, date_pattern='yyyy-mm-dd')
        else:
            # Si no hay tkcalendar, la clase DateEntry es un Entry prellenado (formato YYYY-MM-DD)
            self.entry_fecha = DateEntry(self.frame_entrada)

        self.entry_fecha.grid(row=0, column=1, padx=(0, 12), pady=8, sticky=tk.W)

        # Etiqueta y Entry para la hora
        lbl_hora = ttk.Label(self.frame_entrada, text="Hora (HH:MM):")
        lbl_hora.grid(row=0, column=2, padx=(0, 6), pady=8, sticky=tk.W)

        self.entry_hora = ttk.Entry(self.frame_entrada, width=10)
        self.entry_hora.grid(row=0, column=3, padx=(0, 12), pady=8, sticky=tk.W)

        # Etiqueta y Entry para la descripcion
        lbl_descrip = ttk.Label(self.frame_entrada, text="Descripción:")
        lbl_descrip.grid(row=1, column=0, padx=(0, 6), pady=(0, 10), sticky=tk.W)

        self.entry_descrip = ttk.Entry(self.frame_entrada, width=65)
        self.entry_descrip.grid(row=1, column=1, columnspan=3, padx=(0, 6), pady=(0, 10), sticky=tk.W)

        # Mostrar un pequeño aviso si tkcalendar no está disponible
        if not TKCALENDAR_AVAILABLE:
            lbl_aviso = ttk.Label(self.frame_entrada, text="(Aviso: Use formato YYYY-MM-DD)")
            lbl_aviso.grid(row=2, column=0, columnspan=4, sticky=tk.W, padx=(0,6))

    def _construir_botones(self):
        """Construye los botones para agregar, eliminar y salir."""
        btn_agregar = ttk.Button(self.frame_acciones, text="Agregar Evento", command=self.agregar_evento)
        btn_agregar.pack(side=tk.LEFT, padx=(0, 8))

        btn_eliminar = ttk.Button(self.frame_acciones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento_seleccionado)
        btn_eliminar.pack(side=tk.LEFT, padx=(0, 8))

        btn_salir = ttk.Button(self.frame_acciones, text="Salir", command=self.root.quit)
        btn_salir.pack(side=tk.RIGHT)

    def agregar_evento(self):
        """Agrega un nuevo evento a la lista y actualiza el Treeview.
        Valida que los campos no estén vacíos y que la hora y fecha tengan formato correcto.
        """
        fecha = self.entry_fecha.get().strip()
        hora = self.entry_hora.get().strip()
        descripcion = self.entry_descrip.get().strip()

        # Validaciones simples
        if not fecha:
            messagebox.showwarning("Validación", "Por favor seleccione una fecha.")
            return
        if not hora:
            messagebox.showwarning("Validación", "Por favor ingrese la hora en formato HH:MM.")
            return
        if not descripcion:
            messagebox.showwarning("Validación", "Por favor escriba una descripción para el evento.")
            return

        if not self._validar_fecha(fecha):
            messagebox.showwarning("Validación", "Formato de fecha inválido. Use YYYY-MM-DD.")
            return

        if not self._validar_hora(hora):
            messagebox.showwarning("Validación", "Formato de hora inválido. Use HH:MM (24h). Ej: 09:30 o 17:45")
            return

        # Crear objeto evento con un id unico
        evento = {
            "id": str(uuid.uuid4()),
            "fecha": fecha,
            "hora": hora,
            "descripcion": descripcion
        }

        # Agregar a la lista interna
        self.eventos.append(evento)

        # Insertar en el Treeview
        self.tree.insert("", tk.END, iid=evento['id'], values=(evento['fecha'], evento['hora'], evento['descripcion']))

        # Limpiar campos de entrada (no limpiamos la fecha por conveniencia)
        self.entry_hora.delete(0, tk.END)
        self.entry_descrip.delete(0, tk.END)

    def eliminar_evento_seleccionado(self):
        """Elimina el evento seleccionado en el Treeview con un dialogo de confirmacion.
        Si no hay seleccion muestra una advertencia.
        """
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo("Eliminar evento", "No hay ningún evento seleccionado.")
            return

        # Confirmacion (opcional solicitado)
        confirmar = messagebox.askyesno("Confirmar eliminación", "¿Está seguro que desea eliminar el evento seleccionado?")
        if not confirmar:
            return

        # Puede haber multiples seleccionados; iterar
        for iid in seleccion:
            # Eliminar del Treeview
            self.tree.delete(iid)
            # Eliminar de la lista interna
            self.eventos = [e for e in self.eventos if e['id'] != iid]

    def _on_doble_click(self, event):
        """Muestra un pequeño diálogo con detalles del evento al hacer doble clic en una fila."""
        item = self.tree.identify_row(event.y)
        if not item:
            return
        valores = self.tree.item(item, "values")
        fecha, hora, descripcion = valores
        messagebox.showinfo("Detalles del evento", f"Fecha: {fecha} | Hora: {hora} | Descripción: {descripcion}")

    def _validar_hora(self, hora_str):
        """Valida que la hora esté en formato HH:MM y dentro de 00:00 - 23:59."""
        try:
            partes = hora_str.split(":")
            if len(partes) != 2:
                return False
            hh = int(partes[0])
            mm = int(partes[1])
            if 0 <= hh <= 23 and 0 <= mm <= 59:
                return True
            return False
        except ValueError:
            return False

    def _validar_fecha(self, fecha_str):
        """Valida formato de fecha YYYY-MM-DD."""
        try:
            datetime.strptime(fecha_str, "%Y-%m-%d")
            return True
        except Exception:
            return False


def main():
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
