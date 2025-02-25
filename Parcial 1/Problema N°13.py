"""Implementa una cola con dos pilas. Es decir, simula el comportamiento de una
cola utilizando únicamente dos pilas"""


class QueueUsingStacks:
    def __init__(self):
        self.stack_in = []  # Pila para la inserción
        self.stack_out = []  # Pila para la eliminación

    def enqueue(self, item):
        """Agrega un elemento a la cola."""
        self.stack_in.append(item)

    def dequeue(self):
        """Elimina y devuelve el elemento frontal de la cola."""
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        if not self.stack_out:
            raise IndexError("Dequeue from empty queue")

        return self.stack_out.pop()

    def peek(self):
        """Devuelve el elemento frontal de la cola sin eliminarlo."""
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        if not self.stack_out:
            raise IndexError("Peek from empty queue")

        return self.stack_out[-1]

    def is_empty(self):
        """Verifica si la cola está vacía."""
        return not self.stack_in and not self.stack_out

    def size(self):
        """Devuelve el tamaño de la cola."""
        return len(self.stack_in) + len(self.stack_out)



queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Salida: 1
print(queue.peek())  # Salida: 2
print(queue.dequeue())  # Salida: 2
