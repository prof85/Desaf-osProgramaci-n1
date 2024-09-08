# aplicar_formato.py

import formato_texto as ft
import os
from os import system

# LIMPIAR PANTALLA
def limpiar_pantalla():
    '''
    Limpia la pantalla según el sistema operativo.
    Utiliza 'cls' para Windows y 'clear' para sistemas basados en Linux.
    '''
    system("cls" if os.name == "nt" else "clear")

# MOSTRAR MENÚ DE OPCIONES DE FORMATO
def mostrar_menu():
    '''
    Menú de opciones para aplicar formato al texto.
    '''
    print("\nSelecciona el formato a aplicar:\n")
    print("1. Negrita")
    print("2. Cursiva")
    print("3. Subrayado")
    print("4. Color de texto")
    print("5. Color de fondo")
    print("6. Mayúscula")
    print("7. Minúscula")
    print("8. Mostrar todos los formatos aplicados")
    print("0. Salir")

# MOSTRAR MENÚ DE OPCIONES DE COLORES
def mostrar_opciones_colores():
    '''
    Menú de opciones de colores disponibles para el texto y el fondo.
    '''
    print("\nOpciones de color:")
    print("1. Rojo")
    print("2. Verde")
    print("3. Amarillo")
    print("4. Azul")
    print("5. Magenta")
    print("6. Cian")
    print("7. Blanco")

# VALIDAR INGRESO CORRECTO DEL COLOR
def validar_color(codigo_color):
    '''
    Valida si el código de color está dentro del rango permitido (1-7).
    
    Args:
        codigo_color (int): El código del color a validar.    
    Returns:
        str: El nombre del color correspondiente si es válido, o 'blanco' si no lo es.
    '''
    colores = {
        1: 'rojo',
        2: 'verde',
        3: 'amarillo',
        4: 'azul',
        5: 'magenta',
        6: 'cian',
        7: 'blanco'
    }
    return colores.get(codigo_color, 'blanco')

# MENSAJE PARA SOLICITAR INGRESO DEL COLOR
def solicitar_codigo_color(mensaje):
    '''
    Pide al usuario elejir un color dentro de un rango de números (1 -7).
    Args:
        mensaje (str): El mensaje que se mostrará al usuario.
    Returns:
        int: El código del color seleccionado.
    '''
    while True:
        try:
            numero = int(input(mensaje))
            if 1 <= numero <= 7:
                return numero
            else:
                print("Número no válido. Por favor, ingresa un número entre 1 y 7.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

# SOLICITAR INGRESO CORRECTO DEL COLOR
def solicitar_colores():
    '''
    Solicita al usuario los códigos de color para texto y fondo.
    
    Returns:
        tuple: Un tuple con el código del color del texto y el color del fondo.
    '''
    mostrar_opciones_colores()
    
    # Solicitar código del color de texto
    codigo_texto = solicitar_codigo_color("Selecciona el número del color de texto (1-7): ")
    
    # Solicitar código del color de fondo
    codigo_fondo = solicitar_codigo_color("Selecciona el número del color de fondo (1-7): ")
    
    return codigo_texto, codigo_fondo

# MOSTRAR TODOS LOS FORMATOS APLICADOS 
def mostrar_todo(texto, codigo_texto, codigo_fondo):
    '''
    Muestra todos los formatos aplicados al texto.
    Args:
        texto (str): El texto a formatear.
        codigo_texto (int): El código del color del texto.
        codigo_fondo (int): El código del color del fondo.
    '''
    
    print("\n------------ TODOS LOS FORMATOS ------------")
    print(f"\nTexto a formatear: {texto}")
    print("\nTexto en negrita:", ft.negrita(texto))
    print("\nTexto en cursiva:", ft.cursiva(texto))
    print("\nTexto subrayado:", ft.subrayado(texto))
    print("\nTexto en color:", ft.color(texto, validar_color(codigo_texto)))
    print("\nTexto con color de fondo:", ft.colorf(texto, validar_color(codigo_fondo)))
    print("\nTexto en mayúscula:", ft.a_mayusculas(texto))
    print("\nTexto en minúscula:", ft.a_minusculas(texto))

# FUNCIÓN PRINCIPAL
def menu():
    '''
    Menú para aplicar formatos al texto.
    '''
    limpiar_pantalla()
    print("------------ FORMATEAR TEXTO ------------\n")
    texto = input("Ingresa el texto que deseas formatear: ")
    
    # Inicializar variables para los códigos de colores
    codigo_texto = None
    codigo_fondo = None

    while True:
        mostrar_menu()
       
        opcion = input("\nIngresa el número de la opción deseada: ")

        if opcion == "1":
            print("\nTexto en negrita:", ft.negrita(texto))
        elif opcion == "2":
            print("\nTexto en cursiva:", ft.cursiva(texto))
        elif opcion == "3":
            print("\nTexto subrayado:", ft.subrayado(texto))
        elif opcion == "4":
            mostrar_opciones_colores()
            codigo_texto = solicitar_codigo_color("Selecciona el número del color de texto (1-7): ")
            print("\nTexto en color:", ft.color(texto, validar_color(codigo_texto)))
        elif opcion == "5":
            mostrar_opciones_colores()
            codigo_fondo = solicitar_codigo_color("Selecciona el número del color de fondo (1-7): ")
            print("\nTexto con color de fondo:", ft.colorf(texto, validar_color(codigo_fondo)))
        elif opcion == "6":
            print("\nTexto en mayúscula:", ft.a_mayusculas(texto))
        elif opcion == "7":
            print("\nTexto en minúscula:", ft.a_minusculas(texto))
        elif opcion == "8":
            if codigo_texto is None or codigo_fondo is None:
                print("\nPrimero selecciona los colores para el texto y el fondo.")
            else:
                mostrar_todo(texto, codigo_texto, codigo_fondo)
        elif opcion == "0":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida. Por favor, elige una opción del menú.")
        
        input("\nPresione enter para continuar...")
        limpiar_pantalla()

# INICIAR      
menu()
