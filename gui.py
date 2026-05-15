import tkinter as tk
from doubly_linked_list import DoublyLinkedList

class TaskFlow:

    def __init__(self, root):
        self.root = root
        self.root.title("Nailed It! - To-Do List")
    
        self.listaTareas = DoublyLinkedList()

        self.entradaTarea = tk.Entry(root, width=40)
        self.entradaTarea.pack()

        self.botonAgregar = tk.Button(root, text="Agregar Tarea", command=self.agregarTarea)
        self.botonAgregar.pack()

        self.botonEliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminarTarea)
        self.botonEliminar.pack()

        self.botonCompletar = tk.Button(root, text="Marcar como Completada", command=self.marcarCompletada)
        self.botonCompletar.pack()

        self.labelActual = tk.Label(root, text="Tarea Actual: Ninguna")
        self.labelActual.pack()

        self.botonSiguiente = tk.Button(root, text="Siguiente Tarea", command=self.siguienteTarea)
        self.botonSiguiente.pack()

        self.listaVisual = tk.Listbox(root, width=50)
        self.listaVisual.pack()

    def agregarTarea(self):
        tarea = self.entradaTarea.get()

        self.listaTareas.agregarTarea(tarea)

        self.actualizarVista()
        self.actuarTareaActual()
        

    def eliminarTarea(self):

        seleccion = self.listaVisual.curselection()

        if seleccion:

            indice = seleccion[0]
            nodoTemporal = self.listaTareas.primerNodo
            contador = 0

            while nodoTemporal:
                if contador == indice:
                    self.listaTareas.eliminarTarea(nodoTemporal.tarea)
                    break

                nodoTemporal = nodoTemporal.siguiente
                contador += 1

            self.actualizarVista()

    def marcarCompletada(self):
        seleccion = self.listaVisual.curselection()

        if seleccion:

            indice = seleccion[0]
            nodoTemporal = self.listaTareas.primerNodo
            contador = 0

            while nodoTemporal:
                if contador == indice:
                    nodoTemporal.completado = True
                    break

                nodoTemporal = nodoTemporal.siguiente
                contador += 1

            self.actualizarVista()

    def siguienteTarea(self):
        self.listaTareas.siguiente_tarea()
        self.actuarTareaActual()

    def actuarTareaActual(self):
        if self.listaTareas.nodoActual:
            
            self.labelActual.config(text=f"Tarea Actual: {self.listaTareas.nodoActual.tarea}")
        else:
            self.labelActual.config(text="Tarea Actual: Ninguna")


    def actualizarVista(self):
        self.listaVisual.delete(0, tk.END)

        nodoTemporal = self.listaTareas.primerNodo

        while nodoTemporal:
            estado = "(Completada)" if nodoTemporal.completado else "(Pendiente)"

            self.listaVisual.insert(tk.END, f"{nodoTemporal.tarea} {estado}")

            nodoTemporal = nodoTemporal.siguiente