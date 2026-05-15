# Nailed It! - Task Manager

## Descripción del Proyecto

Nailed It! es una aplicación de gestión de tareas desarrollada en Python utilizando una estructura de datos **Doubly Linked List no circular** implementada completamente desde cero.

El proyecto permite administrar tareas mediante una interfaz gráfica construida con Tkinter, permitiendo agregar tareas, eliminarlas, marcarlas como completadas y navegar entre ellas utilizando referencias hacia adelante y hacia atrás.

La estructura de datos fue desarrollada manualmente sin utilizar librerías que abstraigan el comportamiento de una lista doblemente enlazada.

---

# Objetivo del Proyecto

El objetivo principal es demostrar un caso de uso real de una **Doubly Linked List**, utilizando sus características principales:

- Navegación bidireccional
- Inserción 
- Eliminación dinámica
- Recorrido de nodos
- Manipulación de referencias `siguiente` y `anterior`

---

# Estructura de Datos Utilizada

## Doubly Linked List no circular

Cada nodo contiene:

- Una tarea
- Referencia al siguiente nodo
- Referencia al nodo anterior
- Estado de completado

### Representación visual

```text
A <-> B <-> C


## Funcionalidades Core

### El proyecto cuenta con las siguientes funcionalidades principales:

-Agregar tareas
-Eliminar tareas
-Marcar tareas como completadas
-Navegar hacia adelante entre tareas
-Navegar hacia atrás entre tareas
-Buscar tareas
-Visualización dinámica en interfaz gráfica


## Estructura del proyecto 

NailedItDSA/
│
├── main.py
├── gui.py
├── node.py
├── doubly_linked_list.py
│
├── tests/
│   └── tests_dll.py
│
└── README.md

## Explicación de Archivos

### node.py

Contiene la clase Node, que representa cada nodo individual de la lista.

Cada nodo almacena:

- tarea
- referencia siguiente
- referencia anterior
- estado de completado


### doubly_linked_list.py

Contiene la implementación completa de la estructura de datos.

Métodos principales:

- agregarTarea()
- eliminarTarea()
- buscarTarea()
- siguiente_tarea()
- previous_task()

## gui.py

Contiene toda la interfaz gráfica utilizando Tkinter.

Permite:

- interacción visual
- actualización dinámica
- navegación entre tareas


## main.py

Punto de entrada principal del programa.

Inicializa:

- Tkinter
- interfaz gráfica
- ejecución principal
- tests/tests_dll.py

## test_dll.py

Contiene los unit tests del proyecto.

Se implementaron más de 10 escenarios distintos para validar el correcto funcionamiento de la estructura de datos.

1. agregar tareas
2. agregar múltiples tareas
3. navegación hacia adelante
4. navegación hacia atrás
5. eliminación al inicio
6. eliminación al final
7. eliminación en medio
8. búsqueda existente
9. búsqueda inexistente
10. marcar tareas completadas

## Complejidad Temporal de Métodos

| Método            | Complejidad |
| ----------------- | ----------- |
| agregarTarea()    | O(1)        |
| siguiente_tarea() | O(1)        |
| previous_task()   | O(1)        |
| buscarTarea()     | O(n)        |
| eliminarTarea()   | O(n)        |
| actualizarVista() | O(n)        |


### agregarTarea() — O(1)

La inserción al final de la lista es constante porque la estructura mantiene una referencia directa al último nodo.

### siguiente_tarea() — O(1)

Moverse al siguiente nodo únicamente requiere acceder a la referencia siguiente.

### previous_task() — O(1)

Moverse al nodo anterior únicamente requiere acceder a la referencia anterior.

### buscarTarea() — O(n)

Es necesario recorrer la lista hasta encontrar la tarea deseada.

### eliminarTarea() — O(n)

Primero debe localizarse el nodo antes de eliminarlo.

## Cómo Clonar el Repositorio

"git clone https://github.com/TU-USUARIO/NailedItDSA.git"

## Cómo Ejecutar el Proyecto

Paso 1. "cd NailedItDSA"
Paso 2. "python main.py"

## Cómo Ejecutar los Unit Tests

Paso 1. "cd NailedItDSA"
Paso 2. "python -m unittest tests.tests_dll"

### Autor
Miguel Cuevas