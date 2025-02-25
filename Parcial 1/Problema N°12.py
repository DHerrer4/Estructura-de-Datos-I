"""Simula un sistema de atención en una tienda donde los clientes son atendidos
en orden de llegada (FIFO). Implementa la cola para manejar la fila de clientes."""

class Tienda:
    def __init__(self):
        self.fila_clientes = []  # Usamos una lista para simular la cola FIFO

    def agregar_cliente(self, nombre):
        print(f"Cliente {nombre} llega a la tienda y se une a la fila.")
        self.fila_clientes.append(nombre)

    def atender_cliente(self):
        if self.fila_clientes:
            cliente = self.fila_clientes.pop(0)  # Extrae el primer cliente en la lista (FIFO)
            print(f"Atendiendo a {cliente}...")
            print(f"Cliente {cliente} ha sido atendido.")
        else:
            print("No hay clientes en la fila para atender.")

    def simular_atencion(self, num_clientes):
        for i in range(1, num_clientes + 1):
            self.agregar_cliente(f"Cliente_{i}")

        print("\nIniciando atención de clientes...\n")
        while self.fila_clientes:
            self.atender_cliente()


# Simulación del sistema de atención
tiendanueva = Tienda()
tiendanueva.simular_atencion(5)