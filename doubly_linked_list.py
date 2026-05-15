from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.primerNodo = None
        self.ultimoNodo = None
        self.nodoActual = None
        self.tamaño = 0

    def agregarTarea(self, tarea):
        nuevoNodo = Node(tarea)
        
        if self.primerNodo is None:
            self.primerNodo = nuevoNodo
            self.ultimoNodo = nuevoNodo
            self.nodoActual = nuevoNodo

        else:
            self.ultimoNodo.siguiente = nuevoNodo
            nuevoNodo.anterior = self.ultimoNodo
            self.ultimoNodo = nuevoNodo

        self.tamaño += 1

    def siguiente_tarea(self):
        if self.nodoActual and self.nodoActual.siguiente:
            self.nodoActual = self.nodoActual.siguiente

    def previous_task(self):
        if self.nodoActual and self.nodoActual.anterior:
            self.nodoActual = self.nodoActual.anterior

    def eliminarTarea(self, tarea):
        actual = self.primerNodo

        while actual:
            if actual.tarea == tarea:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.primerNodo = actual.siguiente

                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.ultimoNodo = actual.anterior

                if self.nodoActual == actual:
                    if actual.siguiente:
                        self.nodoActual = actual.siguiente
                    else:
                        self.nodoActual = actual.anterior

                self.tamaño -= 1
                return

            actual = actual.siguiente


    def completarTarea(self):
        if self.nodoActual:
            self.nodoActual.completado = True