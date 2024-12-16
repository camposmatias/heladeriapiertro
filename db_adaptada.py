import sqlite3
from colorama import init, Fore, Back
import os

def limpiar_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

init(autoreset=True)

def crear_tabla_productos():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Productos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT NOT NULL, 
                   precio REAL NOT NULL, 
                   descripcion TEXT,
                   categoria TEXT,
                   stock INTEGER NOT NULL)''')
    conexion.commit()
    conexion.close()

def registrar_producto():
    limpiar_terminal()
    print(Fore.CYAN + "=================")
    print(Fore.CYAN + "Registrar Productos")
    print(Fore.CYAN + "=================\n")
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    nombre = input("Nombre del Producto: ")
    precio = float(input("Precio: "))
    descripcion = input("Descripción: ")
    categoria = input("Categoría: ")
    stock = int(input("Stock: "))

    cursor.execute("INSERT INTO Productos (nombre, precio, descripcion, categoria, stock) VALUES (?, ?, ?, ?, ?)", (nombre, precio, descripcion, categoria, stock))
    
    conexion.commit()
    conexion.close()

def mostrar_producto():
    limpiar_terminal()
    print(Fore.CYAN + "=================")
    print(Fore.CYAN + "Mostrar Productos")
    print(Fore.CYAN + "=================\n")
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Productos")
    resultados = cursor.fetchall()
    for registro in resultados:
        print("ID:", registro[0], "Nombre:", registro[1], "Precio:", registro[2], "Descripción:", registro[3], "Categoría:", registro[4], "Stock:", registro[5])
    print("\n\n")
    
    conexion.close()

def actualizar_producto():
    limpiar_terminal()
    print(Fore.CYAN + "=================")
    print(Fore.CYAN + "Actualizar Productos")
    print(Fore.CYAN + "=================\n")
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    nombre = input("Nombre del Producto: ")
    nuevo_stock = int(input("Nuevo stock: "))
    cursor.execute("UPDATE Productos SET stock = ? WHERE nombre = ?", (nuevo_stock, nombre))

    conexion.commit()
    conexion.close()

def eliminar_producto():
    limpiar_terminal()
    print(Fore.CYAN + "=================")
    print(Fore.CYAN + "Eliminar Productos")
    print(Fore.CYAN + "=================\n")
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    nombre = input("Nombre del Producto a eliminar: ")

    if nombre:
        cursor.execute("DELETE FROM Productos WHERE nombre = ?",(nombre,))
    else:
        print("El producto no existe en el inventario.")
    
    conexion.commit()
    conexion.close()

def buscar_producto():
    limpiar_terminal()
    print(Fore.CYAN + "=================")
    print(Fore.CYAN + "Buscar Productos")
    print(Fore.CYAN + "=================\n")
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    nombre = input("Nombre del Producto: ")
    cursor.execute("SELECT * FROM Productos WHERE nombre = ?", (nombre,))
    resultado = cursor.fetchone()
    print("Nombre:", resultado[1], "Precio:", resultado[2], "Descripción:", resultado[3], "Categoría:", resultado[4], "Stock:", resultado[5])    

    conexion.close()

def reporte_bajo_stock():
    limpiar_terminal()
    print(Fore.CYAN + "=================")
    print(Fore.CYAN + "Reporta de Bajo Stock")
    print(Fore.CYAN + "=================\n")
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    limite_stock = int(input("Ingrese el límite de stock para el reporte: "))
    cursor.execute("SELECT * FROM Productos WHERE stock <= ?", (limite_stock,))
    resultado = cursor.fetchall()

    if resultado:
        for registro in resultado:
            print("ID", registro[0], "Nombre: ", registro[1], "Precio: ", registro[2], "Descripción: ", registro[3], "Categoría: ", registro[4], "Stock: ", registro[5])
    else:
        print("No hay productos con bajo stock")
         
    conexion.close()

def mostrar_menu():
    print(Fore.BLUE + "========================")
    print(Fore.GREEN + " Gestión de Productos")
    print(Fore.BLUE + "========================")
    print("1. Registrar")
    print("2. Mostrar")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. Buscar")
    print("6. Reporte de bajo stock")
    print(Fore.BLUE + "=======================")
    print(Fore.RED + "7. Salir\n")

crear_tabla_productos()


while True:
    mostrar_menu()
    opcion= int(input("Elija en N° de operación que desea realizar: "))
    if opcion == 1:
        registrar_producto()
    elif opcion == 2:
        mostrar_producto()
    elif opcion == 3:
        actualizar_producto()
    elif opcion == 4:
        eliminar_producto()
    elif opcion == 5:
        buscar_producto()
    elif opcion == 6:
        reporte_bajo_stock()
    elif  opcion == 7:
        print(Fore.YELLOW + "*** Programa finalizado exitosamente ***")
        break
    else:
        print("Opción incorrecta, reintente.")
    

