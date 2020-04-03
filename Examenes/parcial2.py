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

_desicion = int (input("""
         elija una de las siguientes opciones :
         1- Lista de Peso de los pacientes ingresados
         2- Calculo de presion
         3- Peso y presion de los pacientes actual
         4- Agregar mas datos a la lista de pesos
         5- Lista de pesos Actual
         6- Presion maxima 
         7- Presion minima
         8- Lista en orden decreciente
         9- Cantidad de pacientes ingresados
         10- salir
         """))
_numeroIngresado = int (input ("Ingrese la opcion deseada"))

while (_numeroIngresado != 10):
    
    if (_numeroIngresado == 1):
        def mostrar_lista (lista):
            print (MENSAJE_LISTA)
            posicion = 1
            for elemento in lista:
                print (elemento)
                posicion += 1
            return (pesosPacientesIniciales)
        mostrar_lista (pesosPacientesIniciales)
    print ("Ingrese la opcion deseada")

    if (_numeroIngresado == 2):
        def calcularPresion (pesosPacientesIniciales):
            print ("Calculo de presion pacientes")
            presion = []
            peso = 0
            for peso in pesosPacientesIniciales:
                presion.append(6*(peso))
            return (presion)
        calcularPresion (presion)
    print ("Ingrese la opcion deseada")
    
    if (_numeroIngresado == 3):
        def mostrar_dos_listas (pesosPacientesIniciales , presion) :
            if (len(pesosPacientesIniciales)==len (presion)) :
                print ("peso" , "presion")
                for i in range (len(pesosPacientesIniciales)):
                    print(pesosPacientesIniciales[i], presion [i])
            else :
                print ("no se puede mostrar")
        mostrar_dos_listas (pesosPacientesIniciales,presion)
    print ("Ingrese el numero deseada")

while (_numeroIngresado == 4):
    def crear_Lista ():
        pesosNuevos = []
        desicion = input (MENSAJE_AGREGAR)
        while (desicion == "s"):
            pesosNuevos.append (input("Ingrese un nuevo peso a la lista"))
            desicion = input (MENSAJE_AGREGAR_2)
        return pesosNuevos
    pesosNuevos = crear_Lista ()
print ("Ingrese el numero deseado")

while (_numeroIngresado == 5):
    def unir_listas (pesosPacientesIniciales,pesosNuevos):
        pesosPacientesIniciales.extend (pesosNuevos)
        print ("esta es la lista de pesos actualizada")
        posicion = 1 
        for i in range (len(pesosPacientesIniciales)):
            print (pesosPacientesIniciales [i])
            posicion += 1
    unir_listas (pesosPacientesIniciales,pesosNuevos)
print ("Ingrese el numero deseado")

while (_numeroIngresado == 6):
    def presionMax ():
        print ("la presion mas alta en la lista{} es {}".format,max(pesosPacientesIniciales))
        return presion
    presionMax = presion
print ("Ingrese el numero deseado")

while (_numeroIngresado == 7):
    def presionMin ():
        print ("la presion mas baja en la lista{} es {}".format,min(pesosPacientesIniciales))
        return presion
    presionMin = presion
print ("Ingrese el numero deseado")

while (_numeroIngresado == 8):
    def decreciente (pesosPacientesIniciales):
        pesosPacientesIniciales.sort (reverse = True)
        lugar = 1
        for peso in pesosPacientesIniciales:
            print (peso)
            lugar +=1
        return(print(MENSAJE_DECRECIENTE))
print ("Ingrese el numero deseado")

while (_numeroIngresado == 9):
    def numeroPacientes ():
        pesosPacientesIniciales.append(peso)
    print (MENSAJE_CANTIDAD.format(pesosPacientesIniciales,pesosPacientesIniciales.count(peso)))
print ("Ingrese el numero deseado")

while (_numeroIngresado == 10):
    print ("salir")
print (MENSAJE_SALIDA)

