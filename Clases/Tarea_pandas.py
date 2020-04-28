import pandas as p
diccionario =p.read_csv("balance.csv",encoding = 'UTF-8',header = 0,delimiter=';').to_dict()
print (diccionario)

nombre_largo = max (diccionario["Ciudad"].values(),key = len)
nombre_corto = min (diccionario["Ciudad"].values(),key = len)
print ("\n\n La ciudad con el nombre ,mas largo es {} y la ciudad con el nombre mas corto es {}"
.format(nombre_largo,nombre_corto))

mayor_ganancias = max (diccionario["Ganancias"].values())
menor_ganancias = max (diccionario["Perdidas"].values())
print ("La mayor ganancia ha sido {}".format(mayor_ganancias))
print ("La menor ganancia ha sido {}".format(menor_ganancias))