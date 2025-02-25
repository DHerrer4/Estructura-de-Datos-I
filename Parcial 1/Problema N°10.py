"""Escribe un programa que verifique si una expresión matemática con paréntesis,
corchetes y llaves está bien balanceada usando una pila.
Ejemplo:
({[()]}) → Balanceado
({[(])}) → No balanceado"""


class Pila:
    def __init__(self):
        self.data = []  # Inicializa una lista vacía para la pila

    def push(self, x):
        """Agrega un elemento al tope de la pila."""
        self.data.append(x)

    def pop(self):
        """Elimina y retorna el elemento en el tope de la pila."""
        if not self.is_empty():
            return self.data.pop()
        else:
            raise IndexError("La pila está vacía.")

    def top(self):
        """Retorna el elemento en el tope de la pila sin eliminarlo."""
        if not self.is_empty():
            return self.data[-1]
        else:
            raise IndexError("La pila está vacía.")

    def is_empty(self):
        """Verifica si la pila está vacía."""
        return len(self.data) == 0


def es_balanceada(expresion):
    pila = Pila()
    # Mapeo de símbolos de cierre a apertura
    mapeo = {')': '(', '}': '{', ']': '['}

    for char in expresion:
        if char in mapeo.values():  # Si es un símbolo de apertura
            pila.push(char)
        elif char in mapeo.keys():  # Si es un símbolo de cierre
            if pila.is_empty() or pila.pop() != mapeo[char]:
                return "No balanceado"

    return "Balanceado" if pila.is_empty() else "No balanceado"



if __name__ == "__main__":
    expresiones = ["({[()]})", "({[(])})"]

    for exp in expresiones:
        resultado = es_balanceada(exp)
        print(f"La expresión '{exp}' está: {resultado}")
