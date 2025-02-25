"""Define una estructura que almacene los datos de un estudiante (nombre,
matrícula, calificación). Luego, escribe una función que reciba un arreglo de
estudiantes y devuelva el nombre del estudiante con la calificación más alta."""

from typing import List

# Definimos la estructura del estudiante usando una clase
class Estudiante:
    def __init__(self, nombre: str, matricula: str, calificacion: float):
        self.nombre = nombre
        self.matricula = matricula
        self.calificacion = calificacion


# Función para encontrar al estudiante con la calificación más alta
def mejor_estudiante(estudiantes: List[Estudiante]) -> str:
    if not estudiantes:
        return "No hay estudiantes en la lista"

    mejor = max(estudiantes, key=lambda est: est.calificacion)
    return mejor.nombre



estudiantes = [
    Estudiante("Juan Pérez", "A123", 88.5),
    Estudiante("Ana Gómez", "B456", 95.2),
    Estudiante("Carlos López", "C789", 91.0)
]

print(mejor_estudiante(estudiantes))  # Salida: Ana Gómez
