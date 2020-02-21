#---------Mensajes----------#
PREGUNTA_NOMBRE = "ingrese su nombre por favor \n "
PREGUNTA_PESO = "ingrese su peso por favor \n "
PREGUNTA_ESTATURA = "ingrese su estatura \n "
MENSAJE_BIENVENIDO = "Bienvenido"
MENSAJE_DESPEDIDA = "Adios"
MENSAJE_BAJO_PESO = "Estas bajo de peso"
MENSAJE_PESO_SALUDABLE = "Estas en un peso saludable"
MENSAJE_SOBREPESO = "Tienes sobrepeso"
MENSAJE_OBESIDAD_MORBIDA = "Tienes obesidad morbida"
MENSAJE_TOCAYO = "Somos tocayas super obesas"
#---------Mensajes----------#
#---------Variables---------#
NOMBRE_PERSONAL = "Ysabella"
IMC = 0.0
#---------Variables---------#
#---------Entradas----------#
_nombreUsuario = " "
_pesoUsuario = 0.0
_estaturaUsuario = 0.0
#---------Entradas----------#
#---------Codigo------------#
print (MENSAJE_BIENVENIDO)
_nombreUsuario = input(PREGUNTA_NOMBRE)
_pesoUsuario = float(input(PREGUNTA_PESO))
_estaturaUsuario = float(input(PREGUNTA_ESTATURA))
IMC = (_pesoUsuario / (_estaturaUsuario**2))
print (IMC)
if (( IMC >= 12) and ( IMC <= 18)) :
    print (MENSAJE_BAJO_PESO)
elif ((IMC >= 19) and (IMC <= 24)) :
    print (MENSAJE_PESO_SALUDABLE)
elif ((IMC >= 30) and (IMC <= 39)) :
    print (MENSAJE_SOBREPESO)
else :
    print (MENSAJE_OBESIDAD_MORBIDA)
    print (MENSAJE_TOCAYO)
print (MENSAJE_DESPEDIDA)

