#------------Mensajes-------------#
MENSAJE_BIENVENIDO = "Bienvenido al codigo"
PREGUNTA_EDAD = "Por favor ingrese su edad"
MENSAJE_NUMERO = "Ingrese un numero por favor"
MENSAJE_EDAD_30 = "Tienes un descuento del 30%"
MENSAJE_MAYOR_60 = "Tienes un descuento del mismo valor de tu edad"
MENSAJE_ACCESO = "acceso concedido"
MENSAJE_ACCESO_2 = "acceso denegado, no cumples con la mayoria de edad"
#----------------------------------#
#--------------Inputs--------------#
_edadPersona = 0
_numeroIngresado = 0
_listaProductos = " "
#--------------Codigo--------------#

print (MENSAJE_BIENVENIDO)
print (""" Menu:
1-Ingrese su edad
2-Productos que desea comprar
3-Lista de productos
4-Desea eliminar algun producto 
5-Salir""")
_numeroIngresado = int (input(MENSAJE_NUMERO))
_edadPersona = int (input (PREGUNTA_EDAD))
while (_numeroIngresado == 1) :
    if ((_edadPersona > 0) and (_edadPersona == 18)):
        print (MENSAJE_ACCESO)
    elif ((_edadPersona >=18) and (_edadPersona <=29)):
        print (MENSAJE_ACCESO)
    elif ((_edadPersona >= 30) and (_edadPersona <=59)) :
        print (MENSAJE_ACCESO , MENSAJE_EDAD_30)
    elif (_edadPersona <=17):
        print(MENSAJE_ACCESO_2)
    else :
        print (MENSAJE_MAYOR_60)
    _numeroIngresado = int (input(MENSAJE_NUMERO))
print (MENSAJE_NUMERO)

while (_numeroIngresado == 2) :
    productos = []
    _listaProductos = input ("que productos sea comprar? : ")
    print (_listaProductos)
    respuesta = input ("Desea ingresar mas productos? s-> si n-> no :")
    while   (respuesta == "s") :
        productos.append (input("ingrese los productos :"))
        respuesta = input ("Desea ingresar mas productos? s->si n->no :")
    print (_listaProductos)
    _numeroIngresado = int (input (MENSAJE_NUMERO))
print (MENSAJE_NUMERO)

while (_numeroIngresado == 3) :
    print (_listaProductos,productos)
    _numeroIngresado = int (input (MENSAJE_NUMERO))
print (MENSAJE_NUMERO)

while (_numeroIngresado == 4) :
    print (_listaProductos,productos)
    _listaProductos = input("por favor ingrese el producto que ya no desea comprar :")
    elemento = input 
    _listaProductos = list.remove (elemento)
    
print (MENSAJE_NUMERO)

while (_numeroIngresado == 5) :
    print ("salir")
print ("Gracias por utilizar el programa")

    

