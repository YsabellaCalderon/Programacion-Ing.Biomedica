#---------Mensajes-----------#
PREGUNTA_NOMBRE = "ingrese su nombre \n "
PREGUNTA_EDAD = "ingrese por favor su edad \n " 
MENSAJE_BINEVENIDO = "bienvenido al programa"
MENSAJE_DESPEDIDA = "Chao"
MENSAJE_TOCAYO = "Hola hermana somos tocayas"
MENSAJE_JOVEN = "Eres joven"
MENSAJE_ADULTO = "Eres adulto"
MENSAJE_ADULTO_MAYOR = "Eres adulto mayor"

#---------Mensajes-----------#
#---------Variables----------#
NOMBRE_PERSONAL = "Ysabella"
#----------------------------#
#---------Entradas-----------#
_nombreUsuario = " "
_edadUsuario = 0
#----------Codigo------------#
print(MENSAJE_BINEVENIDO)
_nombreUsuario = input (PREGUNTA_NOMBRE)
if (NOMBRE_PERSONAL == _nombreUsuario) : 
    print (MENSAJE_TOCAYO)
_edadUsuario = int (input(PREGUNTA_EDAD))
if ((_edadUsuario >= 0) and (_edadUsuario <= 25)) :
    print (MENSAJE_JOVEN)
elif ((_edadUsuario >= 26) and (_edadUsuario <= 65)) :
    print (MENSAJE_ADULTO)
else :
    print (MENSAJE_ADULTO_MAYOR)
print (MENSAJE_DESPEDIDA)
