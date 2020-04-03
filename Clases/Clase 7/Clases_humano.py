class Humano () :      #clase#
    def __init__(self , nombre , estatura , peso , genero , edad) :

        self.raza = "ser humano"
        self.name = nombre
        self.height = estatura
        self.weight = peso
        self.gender = genero
        self.age = edad 
        print ("hola a todos mi raza es", self.raza, "mi nombre es", self.name)

    def mostrar_atributos (self) :
        print ("mi nombre es",self.name)
        print ("mi estaura es",self.height)
        print ("mi genero es",self.gender)
        print ("mi peso es",self.weight)
        print ("mi edad es",self.age)

    def caminar (self,cantidad_pasos) :
        for i in range (cantidad_pasos):
            print ("he caminado", i+1, "pasos")

ser_humano_1 = Humano ("ysabella" , 1.60 , "femenino" , 56 , 19)  
ser_humano_2 = Humano ("valeria" , 1.65 , "Femenino" , 55  , 19)
ser_humano_3 = Humano ("Emiliano" , 1.70 , "Masculino" , 70 , 20)

ser_humano_1.mostrar_atributos ()
ser_humano_2.mostrar_atributos ()
ser_humano_3.mostrar_atributos ()

ser_humano_1.caminar(10)
ser_humano_2.caminar(10)
ser_humano_3.caminar(10)



