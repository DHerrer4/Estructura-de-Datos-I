"""Se tienen dos conjuntos de números enteros. Escribe un programa que determine
si uno es subconjunto del otro."""


def es_subconjunto(conjunto1, conjunto2):
    # Convertimos las listas en conjuntos para aprovechar la operación issubset()
    set1 = set(conjunto1)
    set2 = set(conjunto2)

    if set1.issubset(set2):
        print("El primer conjunto es subconjunto del segundo.")
    elif set2.issubset(set1):
        print("El segundo conjunto es subconjunto del primero.")
    else:
        print("Ninguno de los conjuntos es subconjunto del otro.")



conjunto1 = [1, 2, 3]
conjunto2 = [1, 2, 3, 4, 5]

es_subconjunto(conjunto1, conjunto2)
