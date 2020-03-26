#--------------Mensajes---------------#
MENSAJE_BIENVENIDA = "Bienvenido al programa"
MENSAJE_LISTA_INICIAL = "Esta es la lista de edades de los pacientes que ya han sido ingresados"
MENSAJE_LISTA_NUEVOS_PACIENTES = "Por favor ingrese la lista de edades de los pacientes ingresados al hospital hoy"
PREGUNTA_LISTA_NUEVOS_PACIENTES = "Desea crear una nueva lista de edades? s->si n->no"
PREGUNTA_INGRESAR_ELEMENTOS = "Desea ingresar mas elementos a la lista? s->si n->no"
#--------------Mensajes---------------#
#---------------Codigo----------------#
def Bienvenida ():
    print (MENSAJE_BIENVENIDA)

def mostrar_lista (ListaEdadesIniciales):
    contador = 1
    for element in ListaEdadesIniciales :
        print (element)
        contador += 1

def llenarLista ():
    lista_nueva = []
    desicion = input ("""Desea crear una nueva lista de edades
    para los pacientes que ingresaron hoy? s->si n->no :""")
    while (desicion == "s") :
        lista_nueva.append (input("Ingrese un elemento a la lista"))
        desicion = input ("Desea ingresar mas elementos a la lista? s->si n->no")
    return lista_nueva




