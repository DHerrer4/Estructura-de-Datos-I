"""Implementa una pila con un arreglo dinámico y realiza las siguientes operaciones:
• push(x): Agregar un elemento.
• pop(): Eliminar el elemento en el tope.
• top(): Obtener el elemento en el tope sin eliminarlo."""

class Pila:
    def __init__(self):
        self.data = []  # Inicializa un arreglo dinámico vacío

    def push(self, x):
        """Agrega un elemento al tope de la pila."""
        self.data.append(x)  # Añade el elemento al final del arreglo

    def pop(self):
        """Elimina y retorna el elemento en el tope de la pila."""
        if not self.is_empty():
            return self.data.pop()  # Elimina y retorna el último elemento
        else:
            raise IndexError("La pila está vacía. No se puede hacer pop.")

    def top(self):
        """Retorna el elemento en el tope de la pila sin eliminarlo."""
        if not self.is_empty():
            return self.data[-1]  # Retorna el último elemento
        else:
            raise IndexError("La pila está vacía. No se puede obtener el tope.")

    def is_empty(self):
        """Verifica si la pila está vacía."""
        return len(self.data) == 0

    def size(self):
        """Retorna el número de elementos en la pila."""
        return len(self.data)


if __name__ == "__main__":
    pila = Pila()
    pila.push(10)
    pila.push(20)
    print(pila.top())  # Debe imprimir 20
    print(pila.pop())  # Debe imprimir 20
    print(pila.top())  # Debe imprimir 10
    print(pila.is_empty())  # Debe imprimir False
