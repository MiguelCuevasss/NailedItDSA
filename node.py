class Node:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None
        self.anterior = None
        self.completado = False