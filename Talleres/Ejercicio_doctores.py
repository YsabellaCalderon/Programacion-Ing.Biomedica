#---------------Tarea---------------#
#Realizar un programa que permita:
#1-mostrar un lista de doctores, una lista de enfermos y una lista de enfermeros
#2-y una funcion que permita crear una lista de personas adicional
#---------------Tarea---------------#
#---------------Mensajes--------------#
MENSAJE_BIENVENIDA = "Bienvenido al programa"
MENSAJE_LISTAS = "A continuacion proceda a ingresar las listas con la informacion del personal del hospital y sus pacientes"
MENSAJE_LISTA_DOCTORES = "Por favor ingrese la lista de doctores"
MENSAJE_LISTA_ENFERMEROS = "Por favor ingrese la lista de enfermeros"
MENSAJE_LISTA_PACIENTES = "Por favor ingrese la lista de pacientes"
MENSAJE_ESTADO_PACIENTES = "Ingrese el estado de los pacientes"
#---------------Mensajes--------------#

#--------------Codigo---------------#
print (MENSAJE_BIENVENIDA)
print (MENSAJE_LISTAS)

def llenarLista():
    lista = []
    desicion = input ("Desea ingresar algun elemento s->si n->no :")
    while (desicion == "s") :
        lista.append (input("ingrese un elemento a la lista"))
        desicion = input ("Desea ingresar mas elementos? s->si n->no :")
    return lista

def mostrar_lista (lista):
    contador = 1
    for elemento in lista :
        print (elemento)
        contador += 1

def mostrar_dos_listas (lista_1 , lista_2) :
    if (len(lista_1)==len (lista_2)) :
        print ("paciente" , "Estado paciente")
        for i in range (len(lista_1)):
            print(lista_1[i], lista_2 [i])
    else :
        print ("no se puede mostrar uno a uno")

print (MENSAJE_LISTA_DOCTORES)
doctores = llenarLista ()
print (MENSAJE_LISTA_ENFERMEROS)
enfermeros = llenarLista ()
print (MENSAJE_LISTA_PACIENTES)
pacientes = llenarLista ()
print (MENSAJE_ESTADO_PACIENTES)
estadopacientes = llenarLista ()
print ("Lista de Doctores disponibles en el Hospital")
mostrar_lista (doctores)
print ("Lista de Enfermeros disponibles en el hospital")
mostrar_lista (enfermeros)
print ("Lista de pacientes y su Estado actual")
mostrar_dos_listas ( pacientes, estadopacientes)

print ("Muchas gracias por utilizar el programa, esperamos verlo de nuevo pronto")