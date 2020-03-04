import random
#--------Mensajes----------#
MENSAJE_ACERTADO = "Haz acertado el numero correcto"
MENSAJE_ERROR = "No haz acertado el numero correcto"
MENSAJE_SUMA_DADOS = "suma de los dados"
MENSAJE_DADOS = "vuelva a lanzar los dados"
#--------variables---------#
dado1 = 0
dado2 = 0
suma = 0
NUMERO_DESEADO = 12
#--------Codigo------------#
while (suma != NUMERO_DESEADO) :
    print (MENSAJE_ERROR)
    dado1 = random.randint (1,6)
    dado2 = random.randint (1,6)
    suma = dado1 + dado2
    print (dado1 , dado2)
print ( suma, MENSAJE_ACERTADO) 
#--------Codigo------------#
