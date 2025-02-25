"""Implementa un algoritmo que ordene un arreglo de números enteros utilizando el
algoritmo de Ordenamiento por Inserción y determine su complejidad temporal."""

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Arreglo ordenado:", sorted_arr)

# Complejidad temporal:
# - Mejor caso (lista ya ordenada): O(n)
# - Peor caso (lista en orden inverso): O(n^2)
# - Caso promedio: O(n^2)
