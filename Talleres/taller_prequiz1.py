#----------Mensajes----------#
MENSAJE_BIENVENIDA = "Bienvenido"
PREGUNTA_NUMERO_PACIENTES = "ingrese el numero de pacientes \n"
RIESGO_ALTO = "riesgo operacional alto"
RIESGO_MEDIO = "riesgo operacional medio"
RIESGO_BAJO = "riesgo operacional bajo"
CANTIDAD_PACIENTES_UCI = "ingrese el numero de pacientes en UCI \n"
#---------Mensajes----------#
#---------Entradas-----------#
_numeroPacientes = 0
_numeroPacientesUCI = 0
#---------Salidas------------#
_riesgoOperacional = " "
#---------Codigo-------------#
print (MENSAJE_BIENVENIDA)
_numeroPacientes = int  (input (PREGUNTA_NUMERO_PACIENTES))
_numeroPacientesUCI = int (input (CANTIDAD_PACIENTES_UCI))
if ((_numeroPacientes > 0) and (_numeroPacientes <= 1000)) :
    print (RIESGO_BAJO)
elif ((_numeroPacientes >= 1000) and (_numeroPacientes <= 5000)) :
    print (RIESGO_MEDIO)    
else: 
    print (RIESGO_ALTO)




