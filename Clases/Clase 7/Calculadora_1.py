#--------------Mensajes----------------#
MENSAJE_NUMERO = "ingrese el numero deseado"
MENSAJE_NUMERO_2 = "ingrese el numero deseado"
MENSAJE_SUMA = "la suma de estos dos numeros es"
MENSAJE_RESTA = "la resta de estos dos numeros es"
MENSAJE_MULTIPLICACION = "la multiplicacion de estos dos numeros es"
MENSAJE_DIVISION = "la division de estos dos numeros es"
#--------------Mensajes----------------#
 


def sumar (_numeroDeseado1,_numeroDeseado2):
    suma = _numeroDeseado1 + _numeroDeseado2
    return suma


def restar (_numeroDeseado1,_numeroDeseado2) :
    resta = _numeroDeseado1 - _numeroDeseado2
    return resta


def multiplicar (_numeroDeseado1, _numeroDeseado2) :
    multiplicar = _numeroDeseado1 * _numeroDeseado2
    return multiplicar


def dividir (_numeroDeseado1, _numeroDeseado2) :
    dividir = 0
    if (_numeroDeseado2 == 0) :
        dividir = "no valida"
    else :
        dividir = _numeroDeseado1 / _numeroDeseado2
    return dividir

