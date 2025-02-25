"""Dado dos conjuntos AAA y BBB, implementa funciones para:
• Obtener la unión de ambos conjuntos.
• Obtener la intersección de ambos conjuntos.
• Obtener la diferencia A−BA - BA−B."""

def union_sets(A, B):
    return A | B

def intersection_sets(A, B):
    return A & B

def difference_sets(A, B):
    return A - B


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Unión:", union_sets(A, B))
print("Intersección:", intersection_sets(A, B))
print("Diferencia A - B:", difference_sets(A, B))