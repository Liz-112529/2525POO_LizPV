import tkinter as tk
from tkinter import messagebox # Para mostrar mensajes de advertencia al usuario


def agregar():
    """Agrega el texto del campo al Listbox."""
    texto = entrada.get().strip() # Obtiene el texto escrito y elimina espacios en blanco al inicio/fin
    if texto:
        lista.insert(tk.END, texto) # Inserta el texto al final del Listbox
        entrada.delete(0, tk.END)   # Limpia el campo de entrada
        entrada.focus() # Devuelve el foco al Entry para seguir escribiendo cómodamente
    else:
        messagebox.showwarning("Entrada vacía", "Escribe algo antes de agregar.")  # Si no hay texto, muestra una advertencia en lugar de agregar un ítem vacío


def limpiar():
    """Limpia el campo de entrada y/o el Listbox."""
    if entrada.get():  # Si el campo de texto contiene algo
        entrada.delete(0, tk.END)  # Lo borra
    if lista.size() > 0:  # Si la lista tiene elementos
        lista.delete(0, tk.END)  # Elimina todos los ítems del Listbox


# Ventana principal
root = tk.Tk() # Se crea la ventana principal
root.title("App GUI Simple — Datos") # Título de la ventana
root.geometry("400x300") # Tamaño inicial de la ventana (ancho x alto)
# Label y Entry
lbl = tk.Label(root, text="Ingrese un texto:")  # Etiqueta que indica al usuario qué hacer
lbl.pack(pady=5)

entrada = tk.Entry(root)  # Campo donde el usuario escribe el texto
entrada.pack(fill='x', padx=12)
entrada.bind('<Return>', lambda e: agregar()) # Permite usar la tecla Enter para agregar texto

# Botones
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

btn_agregar = tk.Button(btn_frame, text="Agregar", command=agregar) # Botón para añadir texto
btn_agregar.pack(side='left', padx=5)

btn_limpiar = tk.Button(btn_frame, text="Limpiar", command=limpiar)  # Botón para limpiar
btn_limpiar.pack(side='left', padx=5)

# Listbox para mostrar datos
lista = tk.Listbox(root) # Lista donde se muestran los ítems agregados
lista.pack(fill='both', expand=True, padx=12, pady=12) # fill='both' y expand=True permiten que el Listbox se expanda al cambiar el tamaño de la ventana

# Iniciar loop
root.mainloop() # Mantiene la ventana abierta y a la espera de interacciones del usuario
