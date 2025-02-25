"""Descripción:
Una empresa de entregas tiene un sistema donde recibe pedidos de clientes y
los asigna a repartidores. Los pedidos pueden ser normales o urgentes.
• Los pedidos urgentes deben ser atendidos primero.
• Los pedidos normales se atienden en el orden en que llegan.
• Cada repartidor solo puede llevar un pedido a la vez.
• Se debe permitir agregar y procesar pedidos de manera eficiente.
Requisitos:
• Diseñar una estructura de datos eficiente para gestionar los pedidos.
• Implementar funciones para agregar un pedido, asignar un pedido a un
repartidor y mostrar los pedidos pendientes.
• El sistema debe permitir múltiples repartidores.
Para resolverlo, deberá responder las siguientes preguntas:
1. ¿Qué estructura de datos permite manejar prioridades?
2. ¿Cómo se podría organizar la cola para que los pedidos urgentes sean
atendidos primero?
3. ¿Cómo se asignan pedidos a los repartidores de manera eficiente?"""

"""
1. ¿Qué estructura de datos permite manejar prioridades?
Una lista ordenada es una estructura de datos simple y efectiva para manejar prioridades sin depender de librerías externas. 
En el código, se utiliza una lista normal (self.cola_pedidos) y se ordena manualmente cada vez que se agrega un pedido, 
asegurando que los pedidos urgentes sean atendidos primero.

2. ¿Cómo se podría organizar la cola para que los pedidos urgentes sean atendidos primero?
La cola se organiza mediante una lista (self.cola_pedidos) y cada vez que se agrega un pedido, 
se ordena manualmente con self.cola_pedidos.sort(key=lambda p: p.prioridad). Como los pedidos urgentes tienen prioridad 0 
y los normales prioridad 1, al ordenar la lista, los pedidos urgentes siempre estarán al frente, asegurando que sean atendidos primero.

3. ¿Cómo se asignan pedidos a los repartidores de manera eficiente?
El sistema usa un conjunto de repartidores disponibles (self.repartidores_disponibles). 
Cuando hay pedidos pendientes y repartidores disponibles, el método asignar_pedido():

Extrae un repartidor libre con pop().
Toma el primer pedido de la cola (el más prioritario).
Asigna el pedido al repartidor y lo registra en self.pedidos_asignados.
Una vez que el repartidor entrega el pedido (marcar_pedido_entregado()), 
se libera y se asigna un nuevo pedido si hay más pendientes.
"""

class Pedido:
    def __init__(self, id_pedido, tipo, cliente):
        self.id_pedido = id_pedido
        self.tipo = tipo  # "urgente" o "normal"
        self.cliente = cliente
        self.prioridad = 0 if tipo == "urgente" else 1  # Urgentes tienen mayor prioridad

    def __repr__(self):
        return f"Pedido({self.id_pedido}, {self.tipo}, {self.cliente})"

class SistemaPedidos:
    def __init__(self):
        self.cola_pedidos = []  # Lista para manejar la cola de pedidos
        self.repartidores_disponibles = set()  # Conjunto de repartidores libres
        self.pedidos_asignados = {}  # Mapea repartidor -> pedido

    def agregar_pedido(self, id_pedido, tipo, cliente):
        pedido = Pedido(id_pedido, tipo, cliente)
        self.cola_pedidos.append(pedido)
        self.cola_pedidos.sort(key=lambda p: p.prioridad)  # Ordenar por prioridad (urgentes primero)
        print(f"Pedido {id_pedido} agregado ({tipo}).")
        self.asignar_pedido()

    def agregar_repartidor(self, id_repartidor):
        self.repartidores_disponibles.add(id_repartidor)
        print(f"Repartidor {id_repartidor} agregado.")
        self.asignar_pedido()

    def asignar_pedido(self):
        while self.repartidores_disponibles and self.cola_pedidos:
            repartidor = self.repartidores_disponibles.pop()
            pedido = self.cola_pedidos.pop(0)  # Tomar el primer pedido (más prioritario)
            self.pedidos_asignados[repartidor] = pedido
            print(f"Pedido {pedido.id_pedido} asignado al repartidor {repartidor}.")

    def mostrar_pedidos_pendientes(self):
        print("Pedidos pendientes en la cola:")
        for pedido in self.cola_pedidos:
            print(pedido)

    def marcar_pedido_entregado(self, id_repartidor):
        if id_repartidor in self.pedidos_asignados:
            pedido = self.pedidos_asignados.pop(id_repartidor)
            self.repartidores_disponibles.add(id_repartidor)
            print(f"Pedido {pedido.id_pedido} entregado por repartidor {id_repartidor}.")
            self.asignar_pedido()
        else:
            print(f"No hay pedido asignado al repartidor {id_repartidor}.")


sistema = SistemaPedidos()
sistema.agregar_repartidor(1)
sistema.agregar_repartidor(2)
sistema.agregar_pedido(101, "normal", "Cliente A")
sistema.agregar_pedido(102, "urgente", "Cliente B")
sistema.agregar_pedido(103, "normal", "Cliente C")

sistema.mostrar_pedidos_pendientes()
sistema.marcar_pedido_entregado(1)
sistema.marcar_pedido_entregado(2)
sistema.mostrar_pedidos_pendientes()

