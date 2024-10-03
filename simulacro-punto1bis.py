"""
Utilizando TADs se deberá representar y programar los métodos más
importantes de una factura de venta y sus correspondientes ítems que la conforman. Una
factura contiene información de número, fecha, importe total y cantidad de ítems. Sobre
los ítems se conoce un código de producto, descripción del producto, cantidad y su
precio unitario. Importante agregar_item y el imprimir en factura de venta.
"""

class Factura:
    def __init__(self, nombre, nombreCliente, numFact, fecha, items, importeTotal):
        self.nombre = nombre
        self.nombreCliente = nombreCliente
        self.numFact = numFact
        self.fecha = fecha
        self.items = items
        self.importeTotal = importeTotal

    def agregar_item(self, item):
        self.items.append(item)
        self.importeTotal += item.cant * item.precUni
    
    def devolver_fecha(self):
        return self.fecha
    
    def imprimir_factura(self):
        print(f"Factura Número: {self.numFact}")
        print(f"Nombre de la Empresa: {self.nombre}")
        print(f"Nombre del cliente: {self.nombreCliente}")
        print(f"Fecha: {self.fecha}")
        print("Items:")
        for item in self.items:
            print(f"Coddigo: {item.codProd}, Descripcion: {item.descrip}, Cantidad: {item.cant}, Precio Unitario: {item.precUni}, Subtotal: {item.cant * item.precUni} ")
        print(f"Importe Total: {self.importeTotal}")    
"""
    def agregar_item(self, cod, prod, cant, unit, subtotal):
        lista = [cod, prod, cant, unit, subtotal]
        self.items.append(lista)
""" 

        
class Item:
    def __init__(self, codProd, descrip, cant, precUni):
        self.codProd = codProd
        self.descrip = descrip
        self.cant = cant
        self.precUni = precUni
        

def ingresar_datos_factura():
    numFact = input("Ingrese el numero de factura: ")
    nombre = input("Ingrese el nombre de la Empresa: ")
    nombreCliente = input("Ingrese el nombre del cliente: ")
    fecha = input("Ingrese la fecha de la factura (YYYY--MM--DD): ")
    return Factura(numFact, nombre, nombreCliente, fecha, [], 0.00)

def ingresar_datos_item():
    codProd = input("Ingrese el código del producto: ")
    descrip = input("Ingrese la descripción del producto: ")
    cant = int(input("Ingrese la cantidad: "))
    precUni = float(input("Ingrese el precio unitario: "))

    return Item(codProd, descrip, cant, precUni)
factura = ingresar_datos_factura()
agregar_mas_items = True

while agregar_mas_items:
    item = ingresar_datos_item()
    factura.agregar_item(item)
    
    respuesta = input("¿Desea agregar otro ítem? (s/n): ").lower()
    if respuesta != 's':
        agregar_mas_items = False
        
        
factura.imprimir_factura()