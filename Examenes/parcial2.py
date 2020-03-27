#---------Mensajes----------#
MENSAJE_BIENVENIDA = "Bienvenido al programa"
MENSAJE_LISTA = "Esta es la lista del peso de los pacientes ingresados"
MENSAJE_LISTA_1 = "Esta es la informacion de peso y presion de las pacientes"
MENSAJE_AGREGAR = "Le gustaria agregar mas datos a la lista? si->s no->n:"
MENSAJE_AGREGAR_2 = "Desea agregar mas elementos? si->s no->n:"
MENSAJE_CANTIDAD = "La cantidad de pacientes ingresados es"
MENSAJE_DECRECIENTE = "ESta es la lista en orden decreciente"
MENSAJE_SALIDA = "Gracias por utilizar el programa, esperamos verlo pronto"
#---------Mensajes----------#
pesosPacientesIniciales = [32,64,74,85,98,115,122,127,137,148]
presion = []
peso = 0
#---------Codigo------------#

def bienvenida (mensaje):
    print (mensaje)
    return (MENSAJE_BIENVENIDA)
bienvenida (MENSAJE_BIENVENIDA)

def mostrar_lista (lista):
    print (MENSAJE_LISTA)
    posicion = 1
    for elemento in lista:
        print (elemento)
        posicion += 1
    return (pesosPacientesIniciales)
mostrar_lista (pesosPacientesIniciales)

def calcularPresion (pesosPacientesIniciales):
    print ("Calculo de presion pacientes")
    presion = []
    peso = 0
    for peso in pesosPacientesIniciales:
        presion.append(6*(peso))
    return (presion)
calcularPresion (presion)

def mostrar_dos_listas (pesosPacientesIniciales , pesosNuevos) :
    if (len(pesosPacientesIniciales)==len (pesosNuevos)) :
        print ("peso" , "presion")
        for i in range (len(pesosPacientesIniciales)):
            print(pesosPacientesIniciales[i], pesosNuevos [i])
    else :
        print ("no se puede mostrar")
mostrar_dos_listas (pesosPacientesIniciales,presion)

def crear_Lista ():
    pesosNuevos = []
    desicion = input (MENSAJE_AGREGAR)
    while (desicion == "s"):
        pesosNuevos.append (input("Ingrese un nuevo peso a la lista"))
        desicion = input (MENSAJE_AGREGAR_2)
    return pesosNuevos
pesosNuevos = crear_Lista ()

def unir_listas (pesosPacientesIniciales,pesosNuevos):
    pesosPacientesIniciales.extend (pesosNuevos)
    print ("esta es la lista de pesos actualizada")
    posicion = 1 
    for i in range (len(pesosPacientesIniciales)):
        print (pesosPacientesIniciales [i])
        posicion += 1
unir_listas (pesosPacientesIniciales,pesosNuevos)

def presionMax ():
    print ("la presion mas alta en la lista{} es {}".format,max(pesosPacientesIniciales))
    return presion
presionMax = presion

def presionMin ():
    print ("la presion mas baja en la lista{} es {}".format,min(pesosPacientesIniciales))
    return presion
presionMin = presion

def decreciente (pesosPacientesIniciales):
    pesosPacientesIniciales.sort (reverse = True)
    lugar = 1
    for peso in pesosPacientesIniciales:
        print (peso)
        lugar +=1
    return(print(MENSAJE_DECRECIENTE))

def numeroPacientes ():
    pesosPacientesIniciales.append(peso)
print (MENSAJE_CANTIDAD.format(pesosPacientesIniciales,pesosPacientesIniciales.count(peso)))

def despedida (mensaje):
    print (mensaje)
    return (MENSAJE_SALIDA)
bienvenida (MENSAJE_SALIDA)
