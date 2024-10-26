from Inicializador import cargar_inventario
from Inicializador import guardar_inventario

def anadir_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ").strip()
    cantidad = int(input("Ingrese la cantidad disponible: "))
    precio = float(input("Ingrese el precio unitario: "))

    if nombre in inventario:
        print(f"El producto '{nombre}' ya existe en el inventario.")
    else:
        inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
        guardar_inventario(inventario)
        print(f"Producto '{nombre}' añadido al inventario.")


#actualizar un producto existente
def actualizar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a actualizar: ").strip()

    if nombre in inventario:
        cantidad = int(input("Ingrese la nueva cantidad disponible: "))
        precio = float(input("Ingrese el nuevo precio unitario: "))
        inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
        guardar_inventario(inventario)
        print(f"Producto '{nombre}' actualizado.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")


# eliminar un producto del inventario
def eliminar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()

    if nombre in inventario:
        del inventario[nombre]
        guardar_inventario(inventario)
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")


# productos en el inventario
def mostrar_inventario(inventario):
    if inventario:
        print("\nInventario actual:")
        for nombre, detalles in inventario.items():
            print(f"Producto: {nombre}, Cantidad: {detalles['cantidad']}, Precio: {detalles['precio']}")
    else:
        print("\nEl inventario está vacío.")


#el menú y gestionar las acciones del usuario
def menu():
    inventario = cargar_inventario()

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            anadir_producto(inventario)
        elif opcion == '2':
            actualizar_producto(inventario)
        elif opcion == '3':
            eliminar_producto(inventario)
        elif opcion == '4':
            mostrar_inventario(inventario)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == '__main__':
    menu()