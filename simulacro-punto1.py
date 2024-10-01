"""
Utilizando TADs se deberá representar y programar los métodos más
importantes de una factura de venta y sus correspondientes ítems que la conforman. Una
factura contiene información de número, fecha, importe total y cantidad de ítems. Sobre
los ítems se conoce un código de producto, descripción del producto, cantidad y su
precio unitario. Importante agregar_item y el imprimir en factura de venta.
"""

class Item():
    def __init__(self, codigo_producto, descripcion, cantidad, precio_unitario):
        self.codigo_producto = codigo_producto
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        
    def calcular_total(self):
        return self.cantidad * self.precio_unitario

class Factura ():
    def __init__(self, info_numero, fecha, importe_total, cant_items):
        self.info_numero = info_numero
        self.fecha = fecha
        self.importe_total = 0
        self.cant_items = 0
        self.lista = []
    
    def agregar_items(self):
        print("Ingrese 0 para salir del programa. ")
        codigo_producto = int(input("Ingrese el codigo del producto:"))
        while codigo_producto != 0:
            descripcion = input("Ingrese una breve descripcion del item: ")
            cantidad = int(input("Ingrese la cantidad de items: "))
            precio_unitario = int(input("Ingrese el valor unitario del item: "))
            item = Item(codigo_producto, descripcion, cantidad, precio_unitario)
            self.lista.append(item)
            self.importe_total += item.calcular_total()
            self.cant_items += cantidad
            codigo_producto = int(input("Ingrese el codigo del producto:"))
        
        
    def imprimir_factura(self):
        print(f"Factura N°: {self.info_numero}")
        print(f"Fecha: {self.fecha}")
        print(f"Cantidad de ítems: {self.cant_items}")
        print("Ítems:")
        print("Código | Descripción           | Cantidad | Precio Unitario | Subtotal")
        print("-" * 60)
        
        for item in self.lista:
            subtotal = item.calcular_total()
            print(f"{item.codigo_producto:<6} | {item.descripcion:<20} | {item.cantidad:<8} | {item.precio_unitario:<15} | {subtotal:<10}")

        print("-" * 60)
        print(f"Importe total: {self.importe_total}")
        
        
factura1 = Factura(info_numero=1, fecha="01/10/2024", importe_total=None, cant_items=None)
factura1.agregar_items()
factura1.imprimir_factura()
