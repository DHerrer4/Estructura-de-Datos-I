"""Implementa una lista simplemente enlazada en la que puedas realizar las
siguientes operaciones:
• Insertar un nodo al inicio.
• Insertar un nodo al final.
• Buscar un nodo por su valor.
• Eliminar un nodo por su valor."""


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def insertar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None

        while actual and actual.valor != valor:
            anterior = actual
            actual = actual.siguiente

        if not actual:
            return False  # No se encontró el valor

        if not anterior:
            self.cabeza = actual.siguiente  # Eliminar cabeza
        else:
            anterior.siguiente = actual.siguiente  # Eliminar nodo intermedio o final

        return True

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=' -> ')
            actual = actual.siguiente
        print('None')



lista = ListaEnlazada()
lista.insertar_inicio(3)
lista.insertar_inicio(2)
lista.insertar_inicio(1)
lista.insertar_final(4)
lista.insertar_final(5)
lista.mostrar()

print("Buscar 3:", lista.buscar(3))
print("Buscar 6:", lista.buscar(6))

lista.eliminar(3)
lista.mostrar()
