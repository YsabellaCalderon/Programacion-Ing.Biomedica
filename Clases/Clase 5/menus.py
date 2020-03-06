#-------------lista de nombres----------------#
listaNombres = ["Santiago" ,
 "juanes" ,
 "elena" ,
 "marco" ,
 "mch betancur" ,
 "mch mesa" ,
 "lesly" ,
 "Ysabella" ,
 "Santiago h" ,
 "Daniel" ,
 "Mafe" ,
 "david" ,
 "susana" ,
 "daniel h"]
listaNombres [4] = "Maria Camila Betancur"
listaNombres [5] = "Maria Camila Mesa"
listaNombres.pop (-1)
listaNombres.append ("Daniel H")
print (listaNombres)
#-------------lista de nombres----------------#
#-------------lista de edades-----------------#
ListaEdades = [19 , 17 , 19 , 19 , 19 , 19 , 19 , 19 , 18 , 19 , 18 , 22 , 20 , 26]
print (ListaEdades)
#-------------lista de edades-----------------#
#-------------lista de notas------------------#
listaNotas = [4.9 , 3.5 , 3.2 , 4.8 , 4.9 , 4.7 , 2.9 , 4.3 , 2.8 , 3.7 , 3.5 , 4.1 , 4.9 , 2.1 , 4.5]
print (listaNotas)
#-------------lista de notas------------------#
#-----------Menu------------#
_desicion = int (input("""
         ingrese :
         1-lista de nombres
         2-edades
         3-notas
         4-salir
         """))

while (_desicion != 4) :
    if (_desicion == 1) :
        print (listaNombres)
    elif (_desicion == 2) :
        print (ListaEdades)
    elif (_desicion == 3) :
        print (listaNotas) 
    else:
        print ("ingrese un valor valido")
    _desicion = int (input("""
            ingrese :
            1-lista de nombres
            2-edades
            3-notas
            4-salir
            """))
print ("gracias por usar el programa")
