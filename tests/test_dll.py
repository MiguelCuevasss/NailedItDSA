import unittest
from doubly_linked_list import DoublyLinkedList

class TestDLL(unittest.TestCase):
    
    def test_agregar_tarea(self):
        lista = DoublyLinkedList()

        lista.agregarTarea("Estudiar")

        self.assertEqual(lista.primerNodo.tarea, "Estudiar")

    def test_navegacion(self):
        lista = DoublyLinkedList()

        lista.agregarTarea("Estudiar")
        lista.agregarTarea("Hacer ejercicio")
        lista.agregarTarea("Leer un libro")

        lista.siguiente_tarea()

        self.assertEqual(lista.nodoActual.tarea, "Hacer ejercicio")

    def test_eliminar_tarea(self):
        lista = DoublyLinkedList()

        lista.agregarTarea("Estudiar")
        lista.agregarTarea("Hacer ejercicio")
        lista.agregarTarea("Leer un libro")

        lista.eliminarTarea("Estudiar")

        self.assertEqual(lista.primerNodo.tarea, "Hacer ejercicio")

if __name__ == "__main__":
    unittest.main()