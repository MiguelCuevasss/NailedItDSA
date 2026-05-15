import tkinter as tk
from doubly_linked_list import DoublyLinkedList

class TaskFlow:

    def __init__(self, root):
        self.root = root
        self.root.title("Nailed It! - To-Do List")
    
        self.listaTareas = DoublyLinkedList()

        self.entradaTarea = tk.Entry(root, width=40)
        self.entradaTarea.pack()

        self.botonAgregar = tk.Button(root, text="Agregar Tarea", command=self.agregarTarea())

        self.botonAgregar.pack()

        self.listaVisual = tk.Listbox(root, width=50)
        self.listaVisual.pack()

    def agregarTarea(self):
        tarea = self.entradaTarea.get()

        self.listaTareas.agregarTarea(tarea)

        self.actualizarVista()

    def actualizarVista(self):
        self.listaVisual.delete(0, tk.END)

        nodoTemporal = self.listaTareas.primerNodo

        while nodoTemporal:
            estado = "(Completada)" if nodoTemporal.completada else "(Pendiente)"

            self.listaVisual.insert(tk.END, f"{nodoTemporal.tarea} {estado}")

            nodoTemporal = nodoTemporal.siguiente