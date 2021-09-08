#
# Programa para jugar al ahorcado
# 
# Con la función jugar1 el juego termina cuando el usuario adivina la palabra
# mientras que con la función jugar2 el juego termina cuando el usuario adivina 
# la palabra o pierde las 6 vidas arriesgando letras incorrectas
#
# No olvidar utilizar la receta en Python en cada función 
#

# El módulo random es usado para poder utilizar el método choice()
# que permite elegir aleatoriamente un elemento de una secuencia. 
import random

# Ésta función muestra la solución encontrada por el jugador en cierto momento.
# Por ejemplo si la palabra a adivinar es 'casa' y el usuario eligió la letra 'a'
# debe mostrar '-a-a'
# Nota: La definición de ésta función puede variar de acuerdo a cómo
# se eligió representar a la palabra adivinada


def mostrarTablero(tab):
        completar!!        


# Ésta función se utiliza una vez que el usuario ingresó una letra
# para chequear si la letra está en la palabra secreta y modificar
# la cadena que se muestra en pantalla en el caso de que la letra
# esté en la cadena a adivinar. Devuelve True si la letra está en
# la palabra secreta y False sino. 
 
def agregarLetra(tab, pal, letra):
        completar!!             

# Función principal que permite jugar al juego del ahorcado.
# Ésta función termina sólo si el usuario adivinó la palabra

'''
Ejemplo de uso:

>>>jugar1()
JUEGO DEL AHORCADO
Ingrese una letra: a
-a-a
Ingrese una letra: c
-a-a
Ingrese una letra: f
-a-a
Ingrese una letra: e
-a-a
Ingrese una letra: m
-a-a
Ingrese una letra: p
pa-a
Ingrese una letra: l
pala
Felicitaciones! Ha avivinado la palabra.
'''

def jugar1(): 
     palabras = ['pala', 'masa', 'casa', 'vela', 'tasa', 'capa', 'lupa']
     # Paso 1: Se selecciona una palabra a adivinar aleatoriamente de la lista palabras
     pal = random.choice(palabras)
 
     # Paso 2: Se inicializan variables para empezar a jugar. Decidir qué tipo
     # de datos usar para representar los datos del programa.
     ...
     # A jugar! El usuario elije letras para adivinar la palabra. 
     print('JUEGO DEL AHORCADO')
     ...


'''
La funicón mostrarVidas, toma un entero y muestra el dibujo de la horca
asociado a éste.

mostrarVidas: Int -> None

'''
def mostrarVidas(i):
        
        horcas = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
        print(horcas[i])

	
# La función jugar2 también permite jugar al juego del ahorcado,
# pero termina si el usuario adivinó la palabra, o si perdió las
# 6 vidas arriesgando caracteres que no están en la palabra secreta. 

'''
Ejemplo de uso:
>>> jugar2()
JUEGO DEL AHORCADO
      +---+
      |   |
          |
          |
          |
          |
    =========
Ingrese una letra: a
---a

      +---+
      |   |
          |
          |
          |
          |
    =========
Ingrese una letra: o
---a

      +---+
      |   |
      O   |
          |
          |
          |
    =========
Ingrese una letra: e
-e-a

      +---+
      |   |
      O   |
          |
          |
          |
    =========
Ingrese una letra: p
-e-a

      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
Ingrese una letra: v
ve-a

      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
Ingrese una letra: t
ve-a

      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
Ingrese una letra: l
vela

      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
Felicitaciones! Adivinó la palabra.
'''


def jugar2(): 
     palabras = ['pala', 'masa', 'casa', 'vela']
     # Paso 1: Se selecciona una palabra a adivinar aleatoriamente de la lista palabras
     pal = random.choice(palabras)
 
     # Paso 2: Se inicializan variables para empezar a jugar. Decidir qué tipo
     # de datos usar para representar los datos del programa.
     ...
     # Paso 3: A jugar! El usuario elije letras para adivinar la palabra. 
     ...
     # Paso 4: Muestra mensaje sobre el resultado del juego.
     ...
     



