"""Dada una lista enlazada con un posible ciclo, escribe un algoritmo que detecte si
la lista tiene un ciclo o no (algoritmo de Floyd, "tortuga y liebre")"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    slow = head  # Tortuga
    fast = head  # Liebre

    while fast and fast.next:
        slow = slow.next  # Se mueve un paso
        fast = fast.next.next  # Se mueve dos pasos

        if slow == fast:
            return True  # Hay un ciclo

    return False  # No hay ciclo



# Crear una lista con ciclo: 1 -> 2 -> 3 -> 4 -> 2 (ciclo)
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2  # Ciclo aquí

print(has_cycle(n1))  # True
