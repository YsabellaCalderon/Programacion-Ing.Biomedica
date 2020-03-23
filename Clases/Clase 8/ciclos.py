# #ciclo While#
# n = 0
# while (n != 4):
#     n = int (input("ingrese un numero :"))

# #ciclo for#
# for i in range(4):
#     print (i+1)

computadores = []
respuesta = input ("desea ingresar mas computadores? s-> si n-> no :")
while (respuesta == "s") :
    computadores.append (input("ingrese el modelo del computador :"))
    respuesta = input ("desea ingresar mas computadores? s-> si n-> no :")
print (computadores)
