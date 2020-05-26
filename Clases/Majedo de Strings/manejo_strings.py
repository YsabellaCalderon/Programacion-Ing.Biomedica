texto = "qui lorem ipsum quia dolor sit amet onsectetur adipisci velit"
print(texto.split('q')) # cada vez que encuentre la letra haga un salto (especie de corte, quita la letra)#

# volver una lista un string #
lista = ["hola", "a", "todos"]
string_of_lista = ' '.join(lista) # ' ' separa los elementos de la lista como lo desee ( ';')#
print(string_of_lista)
# modificar las q por las t #
print('t'.join(texto.split('q')))
lista_palabras_texto = texto.split()
print(lista_palabras_texto)
print ( max (lista_palabras_texto,key=len))
# Esto retorna que a es más grande por el código ASCII #
print(max("ZaWU"))
print(min("ZaWU"))
txt_primera_mayuscula= texto.capitalize() # poner la primera letra en mayuscula #
print(txt_primera_mayuscula)
txt_mayuscula= texto.upper() # poner todo en mayusculas #
print(txt_mayuscula)
txt= "HOLA A TODOS"
print (txt.casefold()) # poner todo en minuscula # 

txt= "Quiero ir en otro lugar"
print(txt.center(40)) # para centrar el texto (entre el parentesis va la cantidad de caracteres a la izquierda que se va a mover)#
# cuenta los espacios de la frase #

parrafo = "hola cualquier cosa hola cualquier cosa algo hola cualquier cosa."
print(parrafo.endswith(".")) # verificar que el parrafo termine en punto (validar) #
coordenada_inicio = parrafo.find("algo") # saber donde esta una palabra (encontrar una palabra en especifico) #
coordenada_final = coordenada_inicio+ len("algo")+1 # para que imprima exactamente la palabra #
print(parrafo[coordenada_inicio:coordenada_final])

txt = "72163746234"
print (txt.isnumeric()) # para saber si un texto es numerico #

txt = "AAAA"
print(txt.isalpha()) # para saber si es alfabetico #
print(txt.isascii()) # si esta en ascii #
print(txt.isprintable()) # para saber si se puede imprimir #
print(txt.isupper()) # para saber si esta en mayuscula #


txt = "me gusta programar en Java"
print (txt.replace("Java", "Python")) # para reemplazar una palabra por otra (palabra vieja,palabra nueva) #