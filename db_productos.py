import sqlite3
import os

def limpiar_terminal():
    # Detecta el sistema operativo
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Unix/Linux/MacOS
        os.system("clear")

def crear_tabla_productos():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT
    )''')
    conexion.commit()
    conexion.close()

def registrar_producto():
    limpiar_terminal()
    print("***** | Registro de Producto | *****\n")
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción del producto: ")
    cantidad = int(input("Cantidad disponible: "))
    precio = float(input("Precio del producto: "))
    categoria = input("Categoría del producto: ")

    cursor.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)",
                   (nombre, descripcion, cantidad, precio, categoria))
    
    conexion.commit()
    conexion.close()

def mostrar_productos():
    limpiar_terminal()
    print("***** | Mostrar Productos | *****\n")
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    resultados = cursor.fetchall()
    for registro in resultados:
        print(f"ID: {registro[0]}, Nombre: {registro[1]}, Descripción: {registro[2]}, Cantidad: {registro[3]}, Precio: {registro[4]}, Categoría: {registro[5]}")
    conexion.close()

def actualizar_producto():
    limpiar_terminal()
    print("***** | Actualizar Producto | *****\n")
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    producto_id = int(input("ID del producto a actualizar: "))
    nueva_cantidad = int(input("Nueva cantidad disponible: "))
    cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (nueva_cantidad, producto_id))
    conexion.commit()
    conexion.close()

def eliminar_producto():
    limpiar_terminal()
    print("***** | Eliminar Producto | *****\n")
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    producto_id = int(input("ID del producto a eliminar: "))
    cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
    conexion.commit()
    if cursor.rowcount == 0:
        print("No se encontró ese producto.")
    else:
        print(f"Producto con ID {producto_id} eliminado.")
    conexion.close()

def buscar_producto():
    limpiar_terminal()
    print("***** | Buscar Producto | *****\n")
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    producto_id = int(input("ID del producto: "))
    cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
    resultado = cursor.fetchone()
    if resultado:
        print(f"ID: {resultado[0]}, Nombre: {resultado[1]}, Descripción: {resultado[2]}, Cantidad: {resultado[3]}, Precio: {resultado[4]}, Categoría: {resultado[5]}")
    else:
        print(f"No se encontró el producto con ID {producto_id}.")
    conexion.close()

def reporte_bajo_stock():
    limpiar_terminal()
    print("***** | Reporte de Bajo Stock | *****\n")
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    limite_stock = int(input("Ingrese el límite de stock para generar el reporte: "))
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite_stock,))
    resultados = cursor.fetchall()
    
    if resultados:
        for registro in resultados:
            print(f"ID: {registro[0]}, Nombre: {registro[1]}, Descripción: {registro[2]}, Cantidad: {registro[3]}, Precio: {registro[4]}, Categoría: {registro[5]}")
    else:
        print("No hay productos con bajo stock.")
    conexion.close()

def mostrar_menu():
    print("\nMenú:")
    print("============================")
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Buscar producto")
    print("6. Reporte de bajo stock")
    print("============================")
    print("7. Salir\n")

# Crear la tabla solo una vez
crear_tabla_productos()

while True:
    mostrar_menu()
    
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        registrar_producto()
    elif opcion == 2:
        mostrar_productos()
    elif opcion == 3:
        actualizar_producto()
    elif opcion == 4:
        eliminar_producto()
    elif opcion == 5:
        buscar_producto()
    elif opcion == 6:
        reporte_bajo_stock()
    elif opcion == 7:
        break
    else:
        print("Opción incorrecta, intente nuevamente.")
