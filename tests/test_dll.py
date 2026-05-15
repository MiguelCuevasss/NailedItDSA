import unittest
from doubly_linked_list import DoublyLinkedList

class TestDLL(unittest.TestCase):
    
    def test_agregar_tarea(self):
        lista = DoublyLinkedList()

        lista.agregarTarea("Estudiar")

        self.assertEqual(lista.primerNodo.tarea, "Estudiar")

    def test_agregar_varias_tareas(self):
        lista = DoublyLinkedList()

        lista.agregarTarea("Estudiar")
        lista.agregarTarea("Hacer ejercicio")
        lista.agregarTarea("Leer un libro")

        self.assertEqual(lista.ultimoNodo.tarea, "Leer un libro")

    def test_navegacion(self):
        lista = DoublyLinkedList()

        lista.agregarTarea("Estudiar")
        lista.agregarTarea("Hacer ejercicio")
        lista.agregarTarea("Leer un libro")

        lista.siguiente_tarea()

        self.assertEqual(lista.nodoActual.tarea, "Hacer ejercicio")


    def test_navegacion_anterior(self):
        lista = DoublyLinkedList()

        lista.agregarTarea("Estudiar")
        lista.agregarTarea("Hacer ejercicio")
        lista.agregarTarea("Leer un libro")

        lista.siguiente_tarea()

        self.assertEqual(lista.nodoActual.tarea, "Hacer ejercicio")

        lista.tarea_anterior()

        self.assertEqual(lista.nodoActual.tarea, "Estudiar")


    def test_eliminar_inicio(self):
        lista = DoublyLinkedList()

        lista.agregarTarea("Estudiar")
        lista.agregarTarea("Hacer ejercicio")
        lista.agregarTarea("Leer un libro")

        lista.eliminarTarea("Estudiar")

        self.assertEqual(lista.primerNodo.tarea, "Hacer ejercicio")


    def test_eliminar_final(self):
        lista = DoublyLinkedList()

        lista.agregarTarea("Estudiar")
        lista.agregarTarea("Hacer ejercicio")
        lista.agregarTarea("Leer un libro")

        lista.eliminarTarea("Leer un libro")

        self.assertEqual(lista.ultimoNodo.tarea, "Hacer ejercicio")


    def test_eliminar_medio(self):
        lista = DoublyLinkedList()

        lista.agregarTarea("Estudiar")
        lista.agregarTarea("Hacer ejercicio")
        lista.agregarTarea("Leer un libro")

        lista.eliminarTarea("Hacer ejercicio")

        self.assertEqual(lista.primerNodo.siguiente.tarea, "Leer un libro")


    def test_buscar_tarea_existente(self):
        lista = DoublyLinkedList()

        lista.agregarTarea("Estudiar")
        lista.agregarTarea("Hacer ejercicio")
        lista.agregarTarea("Leer un libro")

        resultado = lista.buscarTarea("Hacer ejercicio")

        self.assertEqual(resultado.tarea, "Hacer ejercicio")


    def test_buscar_tarea_inexistente(self):
        lista = DoublyLinkedList()

        lista.agregarTarea("Estudiar")
        lista.agregarTarea("Hacer ejercicio")
        lista.agregarTarea("Leer un libro")

        resultado = lista.buscarTarea("Cocinar")

        self.assertEqual(resultado, None)


    def test_marcar_completada(self):
        lista = DoublyLinkedList()

        lista.agregarTarea("Estudiar")
        lista.agregarTarea("Hacer ejercicio")
        lista.agregarTarea("Leer un libro")

        lista.primerNodo.completado = True

        self.asertEqual(lista.primerNodo.completado, True)


if __name__ == "__main__":
    unittest.main()