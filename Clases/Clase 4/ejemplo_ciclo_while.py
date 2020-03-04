#----------Variables---------#
# numero = 0
# NUMERO_DESEADO = 12
#---------Codigo-------------#
# while (numero < NUMERO_DESEADO) :
  #  numero = numero +1
  #  print(numero)
# print (numero)
import random
PREGUNTA_NUMERO = """
    ingrese un numero 
    entero 1-10
    : """
MENSAJE_FALLO = "fallaste!! intentalo de nuevo"
MENSAJE_ACIERTO = "felicidades sabes mi numero favorito"
MENSAJE_NUMERO_MAYOR = "el numero que ingreso es mas grande"
MENSAJE_NUMERO_MENOR = "el numero que ingreso es menor"
NUMERO_FAVORITO = random.randint (1,10)
_numeroIngresado = int (input (PREGUNTA_NUMERO))
while (_numeroIngresado != NUMERO_FAVORITO) :
    print (MENSAJE_FALLO)
    if (_numeroIngresado > NUMERO_FAVORITO) : print (MENSAJE_NUMERO_MAYOR)
    else : print (MENSAJE_NUMERO_MENOR)
    _numeroIngresado = int (input (PREGUNTA_NUMERO))
print (MENSAJE_ACIERTO)
