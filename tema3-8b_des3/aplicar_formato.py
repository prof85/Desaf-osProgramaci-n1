# aplicar_formato.py
import formato_texto as ft
import time
from os import system

# LIMPIAR PANTALLA
'''
Limpiar la pantalla 'cls' para Windows y 'clear' para sistemas basados en Linux.
'''
def limpiar_pantalla():
    system("cls" if os.name == "nt" else "clear")

# OPCIONES DE FORMATO
'''
Muestra el menú de opciones para aplicar formato al texto.
'''
def mostrar_menu(): # Función para mostrar el menú de opciones
    print("\nSelecciona el formato a aplicar:\n")
    print("1. Negrita")
    print("2. Cursiva")
    print("3. Subrayado")
    print("4. Color de texto")
    print("5. Color de fondo")
    print("6. Mayúscula")
    print("7. Minúscula")
    print("8. Mostrar todos los formatos aplicados o no") 
    print("0. Salir")

# MOSTRAR LOS FORMATOS REALIZADOS O NO
'''
Muestra todos los formatos aplicados al texto introducido.
Salvo el color del texto y de fondo, el resto se realizan sin intervención del usuario
'''

def mostrar_todo(texto,color,colorf): 
'''
Muestra todos los formatos que se pueden o se aplicaron al texto.
Args:
    texto (str): El texto a formatear.
    codigo_texto (int): El código del color del texto.
    codigo_fondo (int): El código del color del fondo.
'''
        
    print("------------ TODOS LOS FORMATOS ------------\n")        
    print(f"\nTexto a formatear: {texto}") # Imprime el texto a formatear
    print("\nTexto en negrita:", ft.negrita(texto)) # Imprime el texto en negrita
    print("\nTexto en cursiva:", ft.cursiva(texto)) # Imprime el texto en cursiva
    print("\nTexto subrayado:", ft.subrayado(texto)) # Imprime el texto subrayado
    print("\nTexto en color:", ft.color(texto, color)) # Imprime el texto en color
    print("\nTexto con color de fondo:", ft.colorf(texto, colorf)) # Imprime color de fondo en el texto
    print("\nTexto en mayúscula:", ft.a_mayusculas(texto)) # Imprime el texto en mayúscula
    print("\nTexto en minúscula:", ft.a_minusculas(texto)) # Imprime el texto en minúscula

# FUNCIÓN PRINCIPAL
def menu():
'''
Función principal que ejecuta el menú para aplicar formatos al texto.
'''
    limpiar_pantalla()
    print("------------ FORMATEAR TEXTO ------------\n")
    texto = input("Ingresa el texto que deseas formatear: ")

    while True:
        limpiar_pantalla()
        mostrar_menu() # Llama a la función
        opcion = input("\nIngresa el número de la opción deseada: ")

        if opcion == "1":
            print("\nTexto en negrita:", ft.negrita(texto))
        elif opcion == "2":
            print("\nTexto en cursiva:", ft.cursiva(texto))
        elif opcion == "3":
            print("\nTexto subrayado:", ft.subrayado(texto))
        elif opcion == "4":
            color = input("\nEscribe el color a aplicar (rojo, verde, amarillo, azul, magenta, cian, blanco): ")
            print("\nTexto en color:", ft.color(texto, color))    
        elif opcion == "5":
            colorf = input("\nEscribe el color a aplicar (rojo, verde, amarillo, azul, magenta, cian, blanco): ")
            print("\nTexto con color de fondo:", ft.colorf(texto, colorf))    
        elif opcion == "6":
            print("\nTexto en mayúscula:", ft.a_mayusculas(texto))         
        elif opcion == "7":
            print("\nTexto en minúscula:", ft.a_minusculas(texto))
        elif opcion == "8":
            color = input("\nEscribe el color del texto a aplicar (rojo, verde, amarillo, azul, magenta, cian, blanco): ")
            colorf = input("\nEscribe el colordel fondo del texto a aplicar (rojo, verde, amarillo, azul, magenta, cian, blanco): ")
            mostrar_todo(texto, color, colorf)
        elif opcion == "0":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida. Por favor, elige una opción del menú.")
        
        input("\nPresione enter para continuar...")
               
# INICIAR      
menu()

