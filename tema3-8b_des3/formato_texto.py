# formato_texto.py
'''
Crea un módulo personalizado que contenga funciones para cambiar el formato del texto (por ejemplo, a negrita, itálica, etc.) e impórtalo en un nuevo programa.
'''

# NEGRITA ----
'''
Aplica negrita al texto usando códigos ANSI.
Args:
    texto (str): El texto a formatear.
Returns:
    str: Texto en negrita.
'''
def negrita(texto):
    return f'\033[1m{texto}\033[0m'

# CURSIVA ----
'''
Aplica cursiva al texto usando códigos ANSI.
Args:
    texto (str): El texto a formatear.
Returns:
    str: Texto en cursiva.
'''
def cursiva(texto):
    return f'\033[3m{texto}\033[0m'

# SUBRAYADO ----
'''
Aplica subrayado al texto usando códigos ANSI.
Args:
    texto (str): El texto a formatear.
Returns:
    str: Texto subrayado.
'''
def subrayado(texto):
    return f'\033[4m{texto}\033[0m'

# COLOR TEXTO ----
'''
Aplica un color al texto usando códigos ANSI.
Args:
    texto (str): El texto a colorear.
    nombre_color (str): El nombre del color del texto (rojo, verde, amarillo, azul, magenta, cian, blanco).
Returns:
    str: Texto coloreado.
'''
def color(texto, nombre_color):
    colores = {
        'rojo': '\033[31m',
        'verde': '\033[32m',
        'amarillo': '\033[33m',
        'azul': '\033[34m',
        'magenta': '\033[35m',
        'cian': '\033[36m',
        'blanco': '\033[37m'
    }
    codigo_color = colores.get(nombre_color.lower(), '\033[37m')  # Blanco por defecto
    return f'{codigo_color}{texto}\033[0m'

# COLOR FONDO ----
'''
Aplica un color de fondo al texto usando códigos ANSI.
Args:
    texto (str): El texto a formatear.
    nombre_colorf (str): El nombre del color de fondo (rojo, verde, amarillo, azul, magenta, cian, blanco).
Returns:
    str: Texto con el color de fondo aplicado.
'''
def colorf(texto, nombre_colorf):
    colores_fondo = {
        'rojo': '\033[41m',
        'verde': '\033[42m',
        'amarillo': '\033[43m',
        'azul': '\033[44m',
        'magenta': '\033[45m',
        'cian': '\033[46m',
        'blanco': '\033[47m'
    }
    codigo_colorf = colores_fondo.get(nombre_colorf.lower(), '\033[47m')  # Blanco por defecto
    return f'{codigo_colorf}{texto}\033[0m'

# MAYÚSCULAS ----
'''
Convierte el texto a mayúsculas.
Args:
    texto (str): El texto a convertir.
Returns:
    str: Texto en mayúsculas.
'''
def a_mayusculas(texto):
    return texto.upper()

# MINÚSCULAS ----
'''
Convierte el texto a minúsculas.
Args:
    texto (str): El texto a convertir.
Returns:
    str: Texto en minúsculas.
'''
def a_minusculas(texto):
    return texto.lower()

    
    
    
    
    
    
    
