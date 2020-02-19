
#---------------Mensajes-----------------#
PREGUNTA_NOMBRE = "ingrese su nombre \n "
MENSAJE_BIENVENIDO = "Bienvenido"
MENSAJE_BIENVENIDO_SEGUNDAPARTE = "a este programa"
PREGUNTA_EDAD = "ingrese su edad : "
PREGUNTA_ESTATURA = "ingrese su estatura \n "
#---------------Mensajes-----------------#
_nombrePersona = input(PREGUNTA_NOMBRE)
print(MENSAJE_BIENVENIDO,_nombrePersona, MENSAJE_BIENVENIDO_SEGUNDAPARTE) 
_edadPersona = int(input(PREGUNTA_EDAD))
print(PREGUNTA_EDAD,_edadPersona) 
print(type(_edadPersona))
_estaturaPersona = float(input(PREGUNTA_ESTATURA))
print(PREGUNTA_ESTATURA,_estaturaPersona) 
print(type(_estaturaPersona))

