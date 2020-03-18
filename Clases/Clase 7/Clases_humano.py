class Humano () :      #clase#
    def __init__(self , nombre ) :

        print ("hola")
        self.raza = "ser humano"
        self.nombre = nombre
        self.estatura = 1.60
        self.estatura_2 = 1.65 
        self.estatura_3 = 1.55
        self.peso = 56
        self.peso_2 = 55
        self.peso_3 = 58
        self.genero = "femenino"


ser_humano = Humano ("ysabella")  #objeto#
ser_humano_2 = Humano ("valeria")
ser_humano_3 = Humano ("Marella")
print (ser_humano.raza)
print (ser_humano.nombre)
print (ser_humano.estatura)
print (ser_humano.peso)
print (ser_humano.genero)
print (ser_humano_2.raza)
print (ser_humano_2.nombre)
print (ser_humano_2.estatura_2)
print (ser_humano_2.peso_2)
print (ser_humano_2.genero)
print (ser_humano_3.raza)
print (ser_humano_3.nombre)
print (ser_humano_3.estatura_3)
print (ser_humano_3.peso_3)
print (ser_humano_3.genero)

