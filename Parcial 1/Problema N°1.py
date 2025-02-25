"""Dado un arreglo de enteros de tamaño NNN, escribir una función que encuentre
el sub-arreglo con la suma más grande y devuelva dicha suma."""

def max_subarray(arr):
    max_actual = max_global = arr[0]

    for num in arr[1:]:
        max_actual = max(num, max_actual + num)
        max_global = max(max_global, max_actual)

    return max_global


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(arr))  # Salida: 6 (sub-arreglo [4, -1, 2, 1])
