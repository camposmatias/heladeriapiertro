import sqlite3
import os

def limpiar_terminal():
    # Detecta el sistema operativo
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Unix/Linux/MacOS
        os.system("clear")

def crear_tabla_personas():
    conexion = sqlite3.connect("base_datos.db")
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Personas (nombre TEXT, edad INTEGER, ciudad TEXT) ''')
    conexion.commit()
    conexion.close()

def registrar_persona():
    limpiar_terminal()
    print("***** | Registro de Personas | *****\n")
    conexion = sqlite3.connect("base_datos.db")
    cursor = conexion.cursor()
    
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    ciudad = input("Ciudad: ")
    cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES   (?, ?, ?)", (nombre, edad, ciudad))
    
    conexion.commit()
    conexion.close()

def mostrar_personas():
    limpiar_terminal()
    print("***** | Mostrar Personas | *****\n")
    conexion = sqlite3.connect("base_datos.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Personas")
    resultados = cursor.fetchall()
    for registro in resultados:
        print("Nombre:", registro[0], "Edad:", registro[1], "Ciudad:", registro[2])
    conexion.close()

def actualizar_persona():
    limpiar_terminal()
    print("***** | Actualizar Personas | *****\n")
    conexion = sqlite3.connect("base_datos.db")
    cursor = conexion.cursor()
    nombre = input("Nombre de la persona: ")
    nueva_edad = int(input("Nueva edad: "))
    cursor.execute("UPDATE Personas SET edad = ? WHERE nombre = ?", (nueva_edad, nombre))
    conexion.commit()
    conexion.close()

def eliminar_persona():
    conexion = sqlite3.connect("base_datos.db")
    cursor = conexion.cursor()
    nombre = input("Nombre de la persona a eliminar: ")

    if nombre:
        cursor.execute("DELETE FROM Personas WHERE nombre = ?",(nombre,))
        conexion.commit()
        if cursor.rowcount == 0:
            print("No se encontró a esa persona.")
        else:
            print(f"La persona {nombre} ha sido eliminada.")
    else:
        print("Nombre no válido.")
    
    conexion.close()

def buscar_persona():
    limpiar_terminal()
    print("***** | Buscar Personas | *****\n")
    conexion = sqlite3.connect("base_datos.db")
    cursor = conexion.cursor()
    nombre = input("Nombre de la persona: ")
    cursor.execute("SELECT * FROM Personas WHERE nombre = ?", (nombre,))
    resultado = cursor.fetchone()
    if resultado:
        print("Nombre:", resultado[0], "Edad:", resultado[1], "Ciudad:", resultado[2])
    else:
        print(f"No se encontró a la persona {nombre}.")
    conexion.close()

def reporte_menores_edad():
    limpiar_terminal()
    print("***** | Menores de Edad | *****\n")
    conexion = sqlite3.connect("base_datos.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Personas WHERE edad < 18")
    resultados = cursor.fetchall()

    if resultados:
        for registro in resultados:
            print("Nombre:", registro[0], "Edad:", registro[1], "Ciudad:", registro[2])
    else:
        print("No hay menores de edad en la base de datos.")
        
    conexion.close()

def mostrar_menu():
    print("\nMenú:")
    print("============================")
    print("1. Registrar persona")
    print("2. Mostrar personas")
    print("3. Actualizar persona")
    print("4. Eliminar persona")
    print("5. Buscar persona")
    print("6. Reporte menores de edad")
    print("============================")
    print("7. Salir\n")

# Crear la tabla solo una vez
crear_tabla_personas()

while True:
    mostrar_menu()
    
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        registrar_persona()
    elif opcion == 2:
        mostrar_personas()
    elif opcion == 3:
        actualizar_persona()
    elif opcion == 4:
        eliminar_persona()
    elif opcion == 5:
        buscar_persona()
    elif opcion == 6:
        reporte_menores_edad()
    elif opcion == 7:
        break
    else:
        print("Opción incorrecta, intente nuevamente.")
