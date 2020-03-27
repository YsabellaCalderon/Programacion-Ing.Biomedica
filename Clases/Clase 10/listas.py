# se cuenta con una lista de edades inciales de unos pacientes igual a:
ListaEdadesIniciales = [1,2,4,8,16,32,64]
# Crear una lista de edades de pacientes que ingresaron 
# hoy al hospital ,pregunta las edades al usuario que esta utilizando el codigo
#Muestre la lista de las edades ingresadas del dia de hoy
# luego muestra la lista de la suma de las edades iniciales y la de hoy
# mostrar: edad promedio
# mostrar: el paciente con mayor edad 
# mostrar: el paciente mas joven
# mostrar: la lista en orden decreciente y creciente
# ingresar en la posicion 4 una nueva edad de 87  (error)
#eliminar el paciente de la posicion 6

#--------------Mensajes---------------#
MENSAJE_BIENVENIDA = "Bienvenido al programa"
MENSAJE_LISTA_INICIAL = "Esta es la lista de edades de los pacientes que ya han sido ingresados"
MENSAJE_LISTA_NUEVOS_PACIENTES = "Por favor ingrese la lista de edades de los pacientes ingresados al hospital hoy"
PREGUNTA_LISTA_NUEVOS_PACIENTES = "Desea crear una nueva lista de edades? s->si n->no"
PREGUNTA_INGRESAR_ELEMENTOS = "Desea ingresar mas elementos a la lista? s->si n->no"
#--------------Mensajes---------------#
ListaEdadesNueva = []
NO= "No he finalizado"
#--------------Codigo-----------------#

def bienvenida (mensaje):
    print (mensaje)
    return MENSAJE_BIENVENIDA

def mostrar_lista (mensaje,lista):
    print (mensaje)
    posicion = 1
    for elemento in lista:
        print (elemento)
        posicion += 1
    return (print(MENSAJE_LISTA_INICIAL))

def crear_lista ():
    print (PREGUNTA_LISTA_NUEVOS_PACIENTES)
    _elementosAgregados = int(input(MENSAJE_LISTA_NUEVOS_PACIENTES))
    ListaEdadesNueva.append (_elementosAgregados)
    while (_elementosAgregados != 0):
        _elementosAgregados = int (input(MENSAJE_LISTA_NUEVOS_PACIENTES))
        ListaEdadesNueva.append (_elementosAgregados)
        finalizar = NO
    for i in range (len(ListaEdadesNueva)):
        if (_elementosAgregados == ListaEdadesNueva[i]):
            finalizar = i
    if (finalizar != NO):
        ListaEdadesNueva.pop (finalizar)
    return (print("Usted ha Finalizado"))

def unir_listas (ListaEdadesIniciales,ListaEdadesNueva):
    ListaEdadesIniciales.extend (ListaEdadesNueva)
    print ("esta es la lista actualizada")
    posicion = 1 
    for i in range (len(ListaEdadesIniciales)):
        print (ListaEdadesIniciales [i])
        posicion += 1

def promedioListas (lista):
    suma = 0
    for elemento in ListaEdadesIniciales:
        suma = suma + elemento
    promedio = suma / (len(lista))
    print ("Este es el promedio de la lista",promedio)

def ordenCreciente (mensaje,lista):
    print (mensaje)
    lista.sort ()
    lugar = 1
    for elemento in lista:
        print (elemento)
        lugar +=1
    return(print("Esta es la lista en orden creciente"))

def ordenDecreciente (mensaje,lista):
    print (mensaje)
    lista.sort (reverse = True)
    lugar = 1
    for elemento in lista:
        print (elemento)
        lugar +=1
    return(print("Esta es la lista en orden creciente"))

def pacienteIngresado (mensaje,lista,posicion,edad):
    print (mensaje)
    lista.insert (posicion,edad)
    lugar = 1
    for elemento in lista:
        print(elemento)
        lugar += 1
    return (print("Paciente ingresado"))

def eliminarPaciente (mensaje,lista,posicion):
    print (mensaje)
    lugar = 1
    lista.pop (posicion)
    for elemento in lista:
        print (elemento)
        lugar += 1
    return (print("Paciente eliminado"))

def depesdida (mensaje):
    print (mensaje)
    return ("Gracias por utilizar el codigo")

bienvenida (MENSAJE_BIENVENIDA)
ListaEdadesIniciales = [1,2,4,8,16,32,64]
mostrar_lista(MENSAJE_LISTA_INICIAL,ListaEdadesIniciales)
crear_lista()
unir_listas (ListaEdadesIniciales,ListaEdadesNueva)
promedioListas (ListaEdadesIniciales)
print ("la edad maxima en la lista{} es {}",max(ListaEdadesIniciales))
print ("la edad minima en la lista {} es {}",min(ListaEdadesIniciales))
ordenCreciente ("esta es la lista en orden creciente",ListaEdadesIniciales)
ordenDecreciente("esta es la lista en orden decreciente",ListaEdadesIniciales)
pacienteIngresado("entrada errada",ListaEdadesIniciales,3,87)
eliminarPaciente("se ha eliminado el paciente",ListaEdadesIniciales,5)


    
