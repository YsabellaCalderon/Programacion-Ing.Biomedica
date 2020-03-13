#------------------------------#
#nombre archivo: calculadora.py
# entradas: dos numeros
# sumar
# restra
# multiplicar
# dividir
#return: devolver

MENSAJE_NUMERO = "ingrese el numero deseado"
MENSAJE_NUMERO_2 = "ingrese el numero deseado"
#------------------------------#
#-----------Entradas-----------#
_numeroDeseado1 = 0
_numeroDeseado2 = 0
#------------Variable----------#
resultado = 0
#-----------Codigo-------------#

_numeroDeseado1 = int(input(MENSAJE_NUMERO))
_numeroDeseado2 = int(input(MENSAJE_NUMERO_2))

def sumar (_numeroDeseado1,_numeroDeseado2):
    suma = _numeroDeseado1 + _numeroDeseado2
    return suma
resultado = sumar (_numeroDeseado1,_numeroDeseado2)
print (resultado)

def restar (_numeroDeseado1,_numeroDeseado2) :
    resta = _numeroDeseado1 - _numeroDeseado2
    return resta
resultado = restar (_numeroDeseado1,_numeroDeseado2)
print (resultado)

def multiplicar (_numeroDeseado1, _numeroDeseado2) :
    multiplicar = _numeroDeseado1 * _numeroDeseado2
    return multiplicar
resultado = multiplicar (_numeroDeseado1,_numeroDeseado2)
print (resultado)

def dividir (_numeroDeseado1,_numeroDeseado2) :
    dividir = _numeroDeseado1 / _numeroDeseado2
    return dividir

resultado = dividir (_numeroDeseado1,_numeroDeseado2)
print (resultado)