#working in random

from random import randint

elemento= int(input('Los elementos requeridos:'))
lista_aleatoria=[]
contador=1
while contador <= elemento:

    matriz = randint(1,100)
    val=elemento*matriz

    lista_aleatoria.append(val)
    contador =contador+1
print (lista_aleatoria)