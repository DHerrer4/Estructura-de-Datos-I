"""Implementa una cola utilizando una estructura de datos basada en arreglos y
escribe funciones para:
• enqueue(x): Agregar un elemento.
• dequeue(): Sacar un elemento.
• front(): Obtener el elemento en la parte frontal sin eliminarlo."""

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity  # Capacidad máxima de la cola
        self.queue = [None] * capacity  # Arreglo para almacenar los elementos
        self.front_index = 0  # Índice del primer elemento
        self.rear_index = -1  # Índice del último elemento
        self.size = 0  # Tamaño actual de la cola

    def enqueue(self, x):
        """Agrega un elemento a la cola si no está llena."""
        if self.size == self.capacity:
            print("La cola está llena.")
            return
        self.rear_index = (self.rear_index + 1) % self.capacity
        self.queue[self.rear_index] = x
        self.size += 1

    def dequeue(self):
        """Elimina el elemento frontal de la cola si no está vacía."""
        if self.size == 0:
            print("La cola está vacía.")
            return None
        front_element = self.queue[self.front_index]
        self.queue[self.front_index] = None  # Opcional, para limpieza
        self.front_index = (self.front_index + 1) % self.capacity
        self.size -= 1
        return front_element

    def front(self):
        """Devuelve el elemento en la parte frontal sin eliminarlo."""
        if self.size == 0:
            print("La cola está vacía.")
            return None
        return self.queue[self.front_index]

    def is_empty(self):
        """Verifica si la cola está vacía."""
        return self.size == 0

    def is_full(self):
        """Verifica si la cola está llena."""
        return self.size == self.capacity

    def display(self):
        """Muestra los elementos de la cola."""
        if self.size == 0:
            print("La cola está vacía.")
            return
        print("Cola:", [self.queue[(self.front_index + i) % self.capacity] for i in range(self.size)])


queue = Queue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()  # Muestra la cola
print("Front:", queue.front())
print("Dequeue:", queue.dequeue())
queue.display()
