import tkinter as tk
from tkinter import messagebox

class ListaDeTareas: # Clase principal de la aplicación
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas") #Título de la ventana
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Aquí el usuario escribe la nueva tarea
        self.entry = tk.Entry(self.root, width=35, font=("Arial", 12))
        self.entry.pack(pady=10)

        # Evento: presionar la tecla "Enter" agrega la tarea
        self.entry.bind("<Return>", self.agregar_tarea)

        # Frame para organizar los botones en una fila
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=5)

        # Botón para añadir tarea
        self.btn_agregar = tk.Button(frame_botones, text="Añadir Tarea", command=self.agregar_tarea)
        self.btn_agregar.grid(row=0, column=0, padx=5)

        # Botón para marcar como completada
        self.btn_completar = tk.Button(frame_botones, text="Marcar como Completada", command=self.completar_tarea)
        self.btn_completar.grid(row=0, column=1, padx=5)

        # Botón para eliminar tarea
        self.btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_eliminar.grid(row=0, column=2, padx=5)

        # Lista de tareas
        # Aquí se muestran todas las tareas añadidas
        self.listbox = tk.Listbox(
            self.root, width=45, height=15,
            selectmode=tk.SINGLE,  # Solo permite seleccionar una tarea a la vez
            font=("Arial", 12)
        )
        self.listbox.pack(pady=10)

        # Doble clic para marcar como completada
        self.listbox.bind("<Double-1>", self.completar_tarea)

        # Método: agregar nueva tarea
    def agregar_tarea(self, event=None):
        tarea = self.entry.get().strip()  # Obtener texto del Entry
        if tarea:
            # Inserta la tarea en la lista
            self.listbox.insert(tk.END, tarea)
            self.entry.delete(0, tk.END)  # Limpia el campo de entrada
        else:
            # Mensaje de advertencia si la tarea está vacía
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía")

    # Método: completar tarea
    def completar_tarea(self, event=None):
        seleccion = self.listbox.curselection()  # Obtener índice de la tarea seleccionada
        if seleccion:
            indice = seleccion[0]
            tarea = self.listbox.get(indice)

            # Si la tarea no está marcada, se añade un ✔ al inicio
            if not tarea.startswith("✔ "):
                self.listbox.delete(indice)
                self.listbox.insert(indice, "✔ " + tarea)
            else:
                # Si ya estaba marcada, se quita el ✔
                self.listbox.delete(indice)
                self.listbox.insert(indice, tarea.replace("✔ ", ""))
        else:
            # Mensaje si no hay tarea seleccionada
            messagebox.showinfo("Información", "Selecciona una tarea para marcarla como completada")

    # Método: eliminar tarea
    def eliminar_tarea(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            self.listbox.delete(seleccion[0])
        else:
            messagebox.showinfo("Información", "Selecciona una tarea para eliminarla")

# Programa principal
if __name__ == "__main__":
    root = tk.Tk()                # Crear ventana principal
    app = ListaDeTareas(root)
    root.mainloop()               # Iniciar el bucle de eventos de Tkinter
