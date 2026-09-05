class Producto:

    def __init__(self, nombre:str, precio:float, cantidad:int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio:float):
        if nuevo_precio < 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad:int):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual a cero.")
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad
    
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"
    
class Inventario:

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def buscar_producto(self, nombre: str) -> Producto | None:
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def calcular_valor_inventario(self) -> float:
        return sum(producto.calcular_valor_total() for producto in self.productos)

    def listar_productos(self):
        for producto in self.productos:
            print(producto.__str__())

def menu_principal():
    inventario = Inventario()

    #TODO: USO DE TRY EXCEPT PARA VALIDAR EL INGRESO DE DATOS NUMÉRICOS

    while True:
        print("\n Sistema de Inventario\n")
        print("1. Agregar Producto")
        print("2. Buscar Producto")
        print("3. Listar Productos")
        print("4. Calcular Valor Total del Inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción lista anteriormente: ")
        match opcion:

            case '1':

                print("\n Agregar Producto\n")
                nombre = input("Ingrese el nombre del producto: ")
                try:
                    precio = float(input("Ingrese el precio del producto: "))
                    cantidad = int(input("Ingrese la cantidad del producto: "))
                except ValueError:
                    print("ERROR: El precio y la cantidad deben ser números.")
                    continue

                if not nombre.strip():
                    print("ERROR: El nombre no puede estar vacío.")
                    continue
                elif precio < 0:
                    print("ERROR: El precio debe ser mayor que cero.")
                    continue
                elif cantidad < 0:
                    print("ERROR: La cantidad debe ser mayor o igual a cero.")
                    continue
                else:
                    producto = Producto(nombre, precio, cantidad)
                    inventario.agregar_producto(producto)
                    print(f"Producto {nombre} agregado exitosamente.")
                

            case '2':

                print("\n Búsqueda de Producto\n")

                if not inventario.productos:
                    print("ERROR: No hay productos en el inventario.")
                    continue

                nombre = input("Ingrese el nombre del producto a buscar: ")

                if not nombre.strip():
                    print("ERROR: El nombre no puede estar vacío.")
                    continue

                producto = inventario.buscar_producto(nombre)
                if producto:
                    print(f"Producto encontrado: {producto}")
                else:
                    print("Producto no encontrado.")
                    continue

            case '3':

                print("\n Listado de Productos\n")
                if not inventario.productos:
                    print("No hay productos en el inventario.")
                else:
                    inventario.listar_productos()

            case '4':

                print("\n Valor Total del Inventario\n")
                valor_total = inventario.calcular_valor_inventario()
                print(f"El valor total del inventario es: {valor_total}")

            case '5':

                print("Saliendo del sistema de inventario.")
                break

            case _:

                print("Opción inválida. Por favor, seleccione una opción válida.")
                continue

if __name__ == "__main__":
    inventario = Inventario()
    menu_principal()