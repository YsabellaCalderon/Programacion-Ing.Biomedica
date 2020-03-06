#-------Mensajes-------#
MENSAJE_BIENVENIDO = "Bienvenido al codigo"
MENSAJE_LETRA = "Intenta ingresa una letra para descubrir nuestra palabra secreta"
PALABRA_SECRETA = "potus"
MENSAJE_ERROR = "la letra no corresponde,intentalo de nuevo"
MENSAJE_FELICIDADES = "Felicidades!! haz acertado"
MENSAJE_DESPEDIDA = "Adios, gracias por usar el codigo"
#-------Mensajes-------#
#-------Variables------#
letra_ingresada = " "
#-------Variables------#
#-------Entradas-------#
_letraEscogida = " "
#-------Codigo---------#
print (MENSAJE_BIENVENIDO)
print (MENSAJE_LETRA)
while (letra_ingresada not in PALABRA_SECRETA) :
    print (MENSAJE_ERROR)
    letra_ingresada = input (MENSAJE_LETRA)
print (MENSAJE_FELICIDADES , PALABRA_SECRETA)


