def read_news (nombre_noticia) :
    noticia_en_memoria = open(nombre_noticia, 'r')
    linea_noticia = noticia_en_memoria.read().splitlines()
    noticia_en_memoria.close()
    return linea_noticia

def escribir_noticia (nombre_noticia , lista_escribir):
    nueva_noticia = open (nombre_noticia,'w')
    nueva_noticia.writelines (lista_escribir)
    nueva_noticia.close ()

def mostrar_lineas (lista_lineas):
    for linea in lista_lineas:
        print (linea)

def agregra_lineas (nombre_noticia , linea):
    noticia = open ("noticia.txt" , 'a')
    noticia.write (" autor : Sydney Combs ")
    noticia.close ()

