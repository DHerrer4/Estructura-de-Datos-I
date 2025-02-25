"""Implementa una estructura para manejar un inventario de productos con los
siguientes campos: ID, nombre, cantidad y precio. Escribe un programa que
permita agregar, modificar y eliminar productos del inventario."""

class Producto:
    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        if id_producto in self.productos:
            print("Error: El ID del producto ya existe.")
        else:
            self.productos[id_producto] = Producto(id_producto, nombre, cantidad, precio)
            print(f"Producto '{nombre}' agregado correctamente.")

    def modificar_producto(self, id_producto: int, nombre: str = None, cantidad: int = None, precio: float = None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nombre:
                producto.nombre = nombre
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print(f"Producto con ID {id_producto} modificado correctamente.")
        else:
            print("Error: El producto no existe.")

    def eliminar_producto(self, id_producto: int):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado correctamente.")
        else:
            print("Error: El producto no existe.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\nInventario de productos:")
            for producto in self.productos.values():
                print(producto)


inventario = Inventario()

# Agregar productos
inventario.agregar_producto(1, "Laptop", 10, 800.50)
inventario.agregar_producto(2, "Mouse", 50, 25.99)
inventario.agregar_producto(3, "Teclado", 30, 45.75)

# Modificar un producto
inventario.modificar_producto(2, cantidad=45, precio=23.99)

# Mostrar el inventario
inventario.mostrar_inventario()

# Eliminar un producto
inventario.eliminar_producto(3)

# Mostrar el inventario después de eliminar
inventario.mostrar_inventario()
