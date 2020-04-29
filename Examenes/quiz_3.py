#----------Mensajes----------#
MENSAJE_BIENVENIDAD = "\n\nBienvenido al codigo, a continuacion podra ver los datos de los barrios de Medellin"
MENSAJE_DESPEDIDA = "\n\nAdios, gracias por utilizar el codigo"
#----------Mensajes----------#

import pandas as p
diccionario =p.read_csv("barrios.csv",encoding = 'UTF-8',header = 0,delimiter=';').to_dict()

print (MENSAJE_BIENVENIDAD)

nombre_largo = max (diccionario["Barrio"].values(),key = len)
nombre_corto = min (diccionario["Barrio"].values(),key = len)
print ("\n\n El barrio con el nombre ,mas largo es {} y el barrio con el nombre mas corto es {}"
.format(nombre_largo,nombre_corto))

mayor_agua = max (diccionario["Agua"].values())
menor_agua = min (diccionario["Agua"].values())
print ("\n\nEl mayor consumo de agua ha sido {} y el menor consumo de agua ha sido {}"
.format(mayor_agua,menor_agua))

mayor_energia = max (diccionario["Energia"].values())
menor_energia = min (diccionario["Energia"].values())
print ("\n\nEl mayor consumo de energia ha sido {} y el menor consumo de energia ha sido {}"
.format(mayor_energia,menor_energia))

mayor_gas = max (diccionario["Gas"].values())
menor_gas = min (diccionario["Gas"].values())
print ("\n\nEl mayor consumo de gas ha sido {} y el menor consumo de gas ha sido {}"
.format(mayor_gas,menor_gas))

mayor_internet = max (diccionario["Internet"].values())
menor_internet = min (diccionario["Internet"].values())
print ("\n\nEl mayor consumo de agua ha sido {} y el menor consumo de internet ha sido{}"
.format(mayor_internet,menor_internet))

cantidad_maxima_habitantes = max (diccionario["Habitantes"].values())
cantidad_minima_habitantes = min (diccionario["Habitantes"].values())
print ("\n\nLa mayor cantidad de habitantes es {} y la menor cantidad es {}"
.format(cantidad_maxima_habitantes,cantidad_minima_habitantes))

print (MENSAJE_DESPEDIDA)