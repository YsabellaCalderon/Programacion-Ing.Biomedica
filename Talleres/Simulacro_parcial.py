#-----------Mensajes------------#
MENSAJE_IDENTIFICACION = " El número de identificación del Canguro es :"
MENSAJE_EDAD = " La edad del canguro es "
MENSAJE_NOMBRE = " El cuidador es :"
MENSAJE_IDENTIFICACION_CUIDADOR = "El número de idenificación del cuidador :"
#-----------Mensajes------------#
#-----------Codigo--------------#
print ("Bienvenido a la Reserva de Canguros")
print ("A continuacion les mostraremos a nuestros Canguros y Cuidadores")

class Canguros():
    def __init__(self,identificacion ,edad):
        self.identificacion = identificacion
        self.edad = edad
    def mostrar_atributos(self):
        print (MENSAJE_IDENTIFICACION , self.identificacion)
        print (MENSAJE_EDAD, self.edad, "años")
    def saltar(self,cantidad_saltos):
        for i in range (cantidad_saltos):
            print ( "El canguro ha dado", i+1, "saltos")

class Cuidadores():
    def __init__(self , identificacion , nombre):
        self.identificacion_cuidador = identificacion
        self.nombre = nombre
    def mostrar_atributos(self):
        print (MENSAJE_IDENTIFICACION_CUIDADOR, self.identificacion_cuidador)
        print (MENSAJE_NOMBRE, self.nombre)
    def canguros_alimentados(self,cantidad_canguros_alimentados):
        for i in range (cantidad_canguros_alimentados):
            print ( "El cuidador ha alimentado", i+1, "canguros")

class Jefe():
    def __init__(self,identificacion_cuidador,nombre):
        self.identificacion_cuidador = identificacion_cuidador
        self.nombre = nombre
    def dar_mensaje (self,mensaje):
        print(mensaje)
    def contratar_cuidador(self , cuidadores_contratados):
        for i in range (cuidadores_contratados):
            print ( "Se han contratado", i+1, "cuidadores")
       
canguro1 = Canguros(857569 , 2)
canguro2 = Canguros(855938 , 5)
canguro3 = Canguros(726444 , 6)
canguro4 = Canguros(947562 , 1)
canguro5 = Canguros(325412 , 3)
canguro6 = Canguros(125345 , 9)
canguro7 = Canguros(263542 , 2)
canguro8 = Canguros(235414 , 2)
canguro9 = Canguros(215353 , 1)
canguro10 = Canguros(232447 , 8)

cuidador1 = Cuidadores(1004923559, "Mafe")
cuidador2 = Cuidadores(1009567987, "Ysabella")
cuidador3 = Cuidadores(1010156452, "Valeria")
cuidador4 = Cuidadores(1005060697, "Lucas")
cuidador5 = Cuidadores(1020238452,"Bradley")
     
canguro1.mostrar_atributos()
canguro1.saltar(10)

cuidador1.mostrar_atributos()
cuidador1.canguros_alimentados(7)

jefe1 = Jefe(772638,"Maria")

jefe1.dar_mensaje("Hola a todos, soy Maria su jefa. Disfruten su trabajo")
jefe1.contratar_cuidador(5)

print ("Adios, esperamos verlo pronto")

#-----------Codigo--------------#