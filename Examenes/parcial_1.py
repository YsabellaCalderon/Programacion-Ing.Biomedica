#------------Mensajes-----------#
MENSAJE_BIENVENIDO = "Bienvenido al codigo"
MENSAJE_DESPEDIDA = "Gracias por utilizar el codigo, esperamo verlo pronto"
MENSAJE_NOMBRE_ESTUDIANTE = "El nommbre del estudiante es"
MENSAJE_GENERO = "El genero del estudiante es"
MENSAJE_EDAD = "La edad del estudiante es"
MENSAJE_COLEGIO = "El estudiante viene del colegio"

PREGUNTA_MENU = """    
    1- Datos Estidante
    2- Datos Profesrores
    3- Datos Director
    4- Salir
"""
#----------Clases-y-Funciones------------#
class Estudiantes ():
    def __init__(self,nombre,edad,genero,colegio):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.colegio = colegio
    def mostrar_atributos (self):
        print (MENSAJE_NOMBRE_ESTUDIANTE,self.nombre)
        print (MENSAJE_EDAD,self.edad)
        print (MENSAJE_GENERO,self.genero)
        print (MENSAJE_COLEGIO,self.colegio)
    def asistir_clases (self,clases_asistir):
        for i in range(clases_asistir):
            print("El estudiante {} ha asistido a las clases {}".format(self.nombre,i+1))

class Profesores ():
    def __init__(self,nombre_profesor,edad_profesor,nivel_educativo):
        self.nombre = nombre_profesor
        self.edad = edad_profesor
        self.educacion = nivel_educativo
    def mostrar_atributos_profesor (self):
        print ("el nombre del profesor es",self.nombre)
        print ("la edad del profesor es",self.edad)
        print ("el nivel educativo del profesor es",self.educacion)
    def dictar_clases (self,clases_dictadas):
        for i in range (clases_dictadas):
            print("El profesor {} ha dictado {} clases".format(self.nombre,i+1))

class Directores (Profesores):
    def contratar_profesores (self,contratar):
        for i in range (contratar):
            print ("He contratado",i+1,"profesores")
    
def main():
    _eleccion_usuario = 0
    while (_eleccion_usuario!= 4):
        _eleccion_usuario = int(input(PREGUNTA_MENU))
        if (_eleccion_usuario==1):
            print (Estudiantes)
        elif (_eleccion_usuario ==2):
           print Profesores (nombre_profesor,edad_profesor,nivel_educativo)
        elif (_eleccion_usuario == 3):
            Directores (nombre_profesor,edad_profesor,nivel_educativo)
        elif (_eleccion_usuario == 4):
            print (MENSAJE_DESPEDIDA)
        else:
            print("ingrese un número válido")

#----------Codigo---------#
main ()

estudiante_1 = Estudiantes ("Ysabella",19,"Femenino","Arzobispo Silva")
estudiante_2 = Estudiantes ("Valeria",19,"Femenino","Arzobispo Silva")
estudiante_3 = Estudiantes ("Santiago",18,"Masculino","Arzobispo Silva")
estudiante_4 = Estudiantes ("Fernanda",18,"Femenino","Arzobispo Silva")
estudiante_5 = Estudiantes ("Daniel",20,"Masculino","Arzobispo Silva")
estudiante_1.mostrar_atributos ()
estudiante_1.asistir_clases (5)

profesor_1 = Profesores ("Daniel",26,"Superior")
profesor_2 = Profesores ("Maria",30,"Superior")
profesor_1.mostrar_atributos_profesor ()
profesor_1.dictar_clases (10)

director = Directores ("Juan",35,"Superior")
director.contratar_profesores (2)


