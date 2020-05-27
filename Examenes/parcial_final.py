#---------Librerias---------#
import sys
import matplotlib.pyplot as plt
import pandas as p
#---------Librerias---------#
#----------Primero----------# 
#----------Mensajes---------# 
MENSAJE_BIENVENIDA_1 =  "Bienvenido al programa \n"
MENSAJE_DESPEDIDA_1 = "Adios, esperamos verlo pronto \n"
PREGUNTA_NOMBRE_ARCHIVO = "Por favor ingrese el nombre del archivo que desea utilizar \n"
MENSAJE_ARCHIVO_INVALIDO = "El archivo que ingreso no existe, verifique el nombre \n"
PREGUNTA_TITULO = "Por favor ingrese el titulo del grafico \n"
PREGUNTA_EJE_X = "Por favor ingrese el nombre del eje X \n"
PREGUNTA_EJE_Y = "Por favor ingrese el nombre del eje Y \n"
#----------Mensajes---------# 
def valid_archivo (PREGUNTA_NOMBRE_ARCHIVO) :
    assert (open(archivo))
    return False
validador = True
while (validador) : 
    archivo = input (PREGUNTA_NOMBRE_ARCHIVO)
    try :
        validador = valid_archivo (PREGUNTA_NOMBRE_ARCHIVO)
        grafica = p.read_csv (archivo,encoding='UTF-8',header=0, delimiter=";").to_dict()
        x = list (grafica ["muestra"].values())
        y = list (grafica ["valor"].values())
        plt.title(input (PREGUNTA_TITULO))
        plt.xlabel(input (PREGUNTA_EJE_X))
        plt.ylabel(input (PREGUNTA_EJE_Y))
        plt.plot(x,y)
        plt.savefig("grafica.png")
        plt.show ()
        plt.close()
    except FileNotFoundError :
        print (MENSAJE_ARCHIVO_INVALIDO)

print (MENSAJE_DESPEDIDA_1)
#----------Primero----------# 

#----------Segundo----------# 
#----------Mensajes---------# 
MENSAJE_BIENVENIDA_2 = "Bienvenido al programa, a continuacion podra saber su IMC \n"
MENSAJE_DESPEDIDA_2 = "Adios, esperamos verlo pronto \n"
PREGUNTA_NOMBRE = "Por favor ingrese su nombre"
PREGUNTA_PESO = "ingrese su peso en kilogramos por favor \n "
MENSAJE_PESO_INVALIDO = "Ingresaste un valor no valido \n"
PREGUNTA_ESTATURA = "ingrese su estatura \n "
MENSAJE_ESTATURA_INVALIDA = "Ingresaste un valor no valido \n"
PREGUNTA_EDAD = "Por favor ingrese su edad \n"
#----------Mensajes---------# 

#----------Entradas---------# 
_pesoUsuario = 0.0
_edadUsuario = 0
_estaturaUsuario = 0.0
_nombreUsuario = " "
#----------Entradas---------# 

print (MENSAJE_BIENVENIDA_2)
_nombreUsuario = input(PREGUNTA_NOMBRE)
_edadUsuario = int (input(PREGUNTA_EDAD))
_pesoUsuario = float(input(PREGUNTA_PESO))
_estaturaUsuario = float(input(PREGUNTA_ESTATURA))
IMC = (_pesoUsuario / (_estaturaUsuario**2))
print ("{} su indice de masa corporal es {}".format (_nombreUsuario , IMC))
print (MENSAJE_DESPEDIDA_2)

try: 
    peso = float (input(PREGUNTA_PESO))
    estatura = float (input(PREGUNTA_ESTATURA))
except ValueError: 
    print (MENSAJE_PESO_INVALIDO)
    print (MENSAJE_ESTATURA_INVALIDA)
#----------Segundo----------# 

#----------Tercero----------# 
#----------Mensajes---------# 
MENSAJE_BIENVENIDA_3 = """Bienvenido al programa, a continuacion podra observar el grafico
con la informacion de los PPG , ECG y EEG \n"""
#----------Mensajes---------# 
#----------Entradas---------# 
print (MENSAJE_BIENVENIDA_3)

ecg = p.read_csv("ecg.csv" , encoding='UTF-8',header=0, delimiter=";").to_dict()
eeg = p.read_csv("eeg.csv" , encoding='UTF-8',header=0, delimiter=";").to_dict()
ppg = p.read_csv("ppg.csv" , encoding='UTF-8',header=0, delimiter=";").to_dict()
x = list((ecg["muestra"].values()),((eeg["muestra"].values())),((ppg["muestra"].values())))
y = list((ecg["valor"].values()),((eeg["valor"].values())),((ppg["valor"].values())))
plt.title("ECG , EEG , PPG -uV")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.legend ("ECG","EEG","PPG")
plt.savefig("grafico_ecg_eeg_ppg.png")
plt.close()

picos = {
    "Numero de Picos" : [9,10,9],
    "Estudio" : ["ECG","EEG","PPG"] 
}

plt.bar(picos["Numero de Picos"],picos["Estudio"], color ="b", alpha=0.5)
plt.title("Picos Estudios")
plt.xlabel("Nuemro de Picos") 
plt.ylabel("Estudio")
plt.savefig("Picos.png") 
plt.close() 
plt.show()
#----------Tercero----------# 
#-----------Cuarto----------# 
#----------Mensajes---------# 
MENSAJE_BIENVENIDA_4 = """ Bienvenido, a continuacion podra observar un grafico en el cual
se observa los lugares en los que mas he pasado tiempo en mi casa durante este tiempo \n"""
MENSAJE_DESPEDIDA_4 = "Adios, esperamos verlo pronto \n"
#----------Mensajes---------# 

print (MENSAJE_BIENVENIDA_4)

labels = 'Habitacion' , 'Estudio' , 'Cocina' , 'Sala' , 'Parque de Perros'
sizes = [10 , 60 , 15 , 5 , 20]
explode = (0 , 0.1 , 0 , 0  , 0) 
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("Tiempo en Cuarentena")
plt.savefig("Tiempo_curentena.png")
plt.show()

print (MENSAJE_DESPEDIDA_4)
#-----------Cuarto----------# 

#----------Quinto-----------#
#----------Mensajes---------#
APRENDIZAJE_SUPERVISADO_Y_NO_SUPERVISADO = """ Desde mi punto de vista me parece que hay una gran diferencia entre los dos
dependiendo de la persona, ya que no todos tenemos la misma capacidad de concentración y disciplina a la hora de estudiar o
trabajar. El aprendizaje supervisado te obliga (por sí decirlo), a prestar atención constantemente, a no distraerte y a 
participar; mientras que en el aprendizaje no supervisado, queda totalmete de tu parte el hecho de aprender, concentrate y 
participar. Ademas de que en esta situación pueden existir muchos distractores en el ambiente, ya sea el ruido, el célular, 
la mascota, etc.

Como conclusion, siento que hay ser muy consiente a la hora del estudio no supervisado y saber que hay momentos para todo y
para nosotros principalmente, debemos esforzarnos por ser juiciosos y un poco autodidactas en el estudio en casa"""

print (APRENDIZAJE_SUPERVISADO_Y_NO_SUPERVISADO)