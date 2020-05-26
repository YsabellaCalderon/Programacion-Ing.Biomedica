#---------Librerias---------#
import sys
import matplotlib.pyplot as plt
import pandas as p
#---------Librerias---------#
#----------Primero----------# #TERMINAR/REVISAR
#----------Mensajes---------# 
MENSAJE_BIENVENIDA_1 =  "Bienvenido al programa \n"
MENSAJE_DESPEDIDA_1 = "Adios, esperamos verlo pronto \n"
PREGUNTA_NOMBRE_ARCHIVO = "Por favor ingrese el nombre del archivo que desea utilizar \n"
MENSAJE_ARCHIVO_INVALIDO = "El archivo que ingreso no existe, verifique el nombre \n"
PREGUNTA_TITULO = "Por favor ingrese el titulo del grafico \n"
PREGUNTA_EJE_X = "Por favor ingrese el nombre del eje X \n"
PREGUNTA_EJE_Y = "Por favor ingrese el nombre del eje Y \n"
#----------Mensajes---------# 
def Valid_archive (archivo):
    FileNotFoundError (archivo)
    return False
validador = True

while (validador):
    archivo = open (input (PREGUNTA_NOMBRE_ARCHIVO))
    try :
        validador = Valid_archive (archivo)
    except FileNotFoundError :
        print (MENSAJE_ARCHIVO_INVALIDO)

_nombreGrafico = " "
_ejeX = " "
_ejeY = " "

ecg = p.read_csv("ecg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x = list(ecg["muestra"].values())
y = list(ecg["valor"].values())
plt.title(input (_nombreGrafico))
plt.xlabel(input (_ejeX))
plt.ylabel(input (_ejeY))
plt.plot(x,y)
plt.savefig("mi_ecg.png")
plt.close()
#----------Primero----------#
#----------Segundo----------# 
#----------Mensajes---------# 
MENSAJE_BIENVENIDA_2 = "Bienvenido al programa, a continuacion podra saber su IMC \n"
MENSAJE_DESPEDIDA_2 = "Adios, esperamos verlo pronto \n"
PREGUNTA_NOMBRE = "Por favor ingrese su nombre"
PREGUNTA_PESO = "ingrese su peso por favor \n "
MENSAJE_PESO_INVALIDO = "Ingresaste un valor no valido \n"
PREGUNTA_ESTATURA = "ingrese su estatura \n "
MENSAJE_ESTATURA_INVALIDA = "Ingresaste un valor no valido \n"
MENSAJE_BAJO_PESO = "Estas bajo de peso"
MENSAJE_PESO_SALUDABLE = "Estas en un peso saludable"
MENSAJE_SOBREPESO = "Tienes sobrepeso"
MENSAJE_OBESIDAD_MORBIDA = "Tienes obesidad morbida"
#----------Mensajes---------# 
#----------Entradas---------# 
_pesoUsuario = 0.0
_estaturaUsuario = 0.0
_nombreUsuario = " "
#----------Entradas---------# 

print (MENSAJE_BIENVENIDA_2)
_nombreUsuario = input(PREGUNTA_NOMBRE)
_pesoUsuario = float(input(PREGUNTA_PESO))
_estaturaUsuario = float(input(PREGUNTA_ESTATURA))
IMC = (_pesoUsuario / (_estaturaUsuario**2))
print (IMC)
if (( IMC >= 12) and ( IMC <= 18)) :
    print (MENSAJE_BAJO_PESO)
elif ((IMC >= 19) and (IMC <= 24)) :
    print (MENSAJE_PESO_SALUDABLE)
elif ((IMC >= 30) and (IMC <= 39)) :
    print (MENSAJE_SOBREPESO)
else :
    print (MENSAJE_OBESIDAD_MORBIDA)
print (MENSAJE_DESPEDIDA_2)

try: 
    peso = int (input(PREGUNTA_PESO))
except ValueError: 
    print (MENSAJE_PESO_INVALIDO)
try: 
    estatura = int (input(PREGUNTA_ESTATURA))
except ValueError: 
    print (MENSAJE_DESPEDIDA_2)

#----------Segundo----------# 
#----------Tercero----------# 
#----------Mensajes---------# 
MENSAJE_BIENVENIDA_3 = """Bienvenido al programa,
a continuacion podra generar un grafico de barras
para ver las cantidades de sus productos \n"""
PREGUNTA_KILOS_ARROZ = "por favor ingrese la cantidad que tiene de arroz \n"
PREGUNTA_KILOS_LENTEJAS = "por favor ingrese la cantidad que tiene de lentejas \n"
PREGUNTA_KILOS_FRIJOLES = "por favor ingrese la cantidad que tiene de frijoles \n"
PREGUNTA_KILOS_PAPAS = "por favor ingrese la cantidad que tiene de papas \n"
MENSAJE_DESPEDIDA_3 = """Esperamos que la informacion haya sido de utilidad,
esperamos verlo pronto \n"""
#----------Mensajes---------# 
#----------Entradas---------# 
_kilosArroz = 0
_kilosFrijoles = 0
_kilosLentejas = 0
_kilosPapa = 0 
#----------Entradas---------# 

print (MENSAJE_BIENVENIDA_3)

_kilosArroz = int (input(PREGUNTA_KILOS_ARROZ))
_kilosFrijoles = int (input(PREGUNTA_KILOS_FRIJOLES))
_kilosLentejas = int (input(PREGUNTA_KILOS_LENTEJAS))
_kilosPapa = int (input(PREGUNTA_KILOS_PAPAS))

cantidades = { 
"Producto" : ["Arroz" , "Frijoles" , "Lentejas" , "Papas"] , 
"Kilogramos" :[_kilosArroz , _kilosFrijoles , _kilosLentejas , _kilosPapa] }

plt.bar (cantidades ["Producto"] , cantidades ["Kilogramos"], color = "g" , alpha = 0.5)
plt.title("Cantidades Productos Usuario")
plt.xlabel("Productos") 
plt.ylabel("Peso (kg)")
plt.savefig("Cantidades Productos Usuario.png") 
plt.close() 
plt.show()

print (MENSAJE_DESPEDIDA_3)
#----------Tercero----------# 

#-----------Cuarto----------# 
#----------Mensajes---------# 
MENSAJE_BIENVENIDA_4 = """Bienvenido al programa, 
a continuacion podra hablarnos un poco acerca de como se ha sentido estos ultimos dias \n"""
MENSAJE_PARRAFO = """Por favor ingrese un parrafo acerca de como se ha sentido ultimamente, 
recuerde que este debe terminar en punto (.) \n"""
MENSAJE_PARRAFO_INVALIDO = """El parrafo que ha ingresado no es valido,
verifique sus signos de puntuación \n"""
MENSAJE_DESPEDIDA_4 = "Adios, esperamos verlo pronto"
#----------Mensajes---------# 
def valid_paragraph  (paragraph):
    assert(paragraph.endswith("."))
    return False
validador = True

while (validador):
    paragraph =  input(MENSAJE_PARRAFO)
    try:
        validador = valid_paragraph(paragraph)
    except AssertionError:
        print(MENSAJE_PARRAFO_INVALIDO)

print (MENSAJE_DESPEDIDA_4)
#-----------Cuarto----------# 

#-----------Quinto----------# 
#----------Mensajes---------# 
MENSAJE_BIENVENIDA_5 = """ Bienvenido, a continuacion podra observar un grafico en el cual
se observa un estudio en la compra de ciertos productos \n"""
MENSAJE_DESPEDIDA_5 = "Adios, esperamos verlo pronto \n"
#----------Mensajes---------# 

print (MENSAJE_BIENVENIDA_5)

labels = 'Leche', 'Huevos', 'Vino', 'Arroz' , 'Queso' , 'Salchichas'
sizes = [12 , 8 , 4 , 26 , 30 , 20]
explode = (0 , 0 , 0 , 0 , 0.2 , 0) 
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("Estudio Compras")
plt.savefig("Estudio_compras.png")
plt.show()

print (MENSAJE_DESPEDIDA_5)
#-----------Quinto----------# 