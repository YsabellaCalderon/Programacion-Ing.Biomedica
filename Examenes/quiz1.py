#-----------Mensajes-------------#
MENSAJE_BIENVENIDO = "Bienvenido al codigo"
PREGUNTA_TEMPERATURA = "por favor ingrese su temperarura \n"
PREGUNTA_PAIS = "por favor ingrese su pais de procendencia \n"
MENSAJE_HIPOTERMIA = "se encuentra en estado de hipotermia"
MENSAJE_SALUDABLE = "se encuentra en estado saludable"
MENSAJE_ESTADO_ALERTA = "se encuentra en estado de alerta"
MENSAJE_ESTADO_PELIGRO = "se encuentra en estado de peligro"
MENSAJE_OBSERVACION = "se encuentra en estado de observacion"
#----------Mensaje---------------#
#----------Entradas--------------#
_temperaturaUsuario = 0.0
_procedenciaUsuario = " "
#----------Entradas--------------#
#----------Salidas---------------#
_estadoPaciente = " "
#----------Salidas---------------#
#----------Codigo----------------#
print (MENSAJE_BIENVENIDO)
_procedenciaUsuario = (input(PREGUNTA_PAIS))
if ((_procedenciaUsuario == "china") or (_procedenciaUsuario == "italia") or (_procedenciaUsuario == "iran")) :
    print (MENSAJE_OBSERVACION)
_temperaturaUsuario = float (input(PREGUNTA_TEMPERATURA))
if (_temperaturaUsuario < 36) :
    print (MENSAJE_HIPOTERMIA)
elif ((_temperaturaUsuario >= 36) and (_temperaturaUsuario <= 38.4)) :
    print (MENSAJE_SALUDABLE)
elif ((_temperaturaUsuario >= 38.5) and (_temperaturaUsuario >= 40)) :
    print (MENSAJE_ESTADO_ALERTA)
else:
    print (MENSAJE_ESTADO_PELIGRO)
    

