import matplotlib.pyplot as plt
import pandas as p

#-----------Graficos de Barras-------------#
inventario = p.read_csv("inventario.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(inventario)
plt.title("Elementos vs Unidades", fontsize=20)
plt.bar(inventario["Elemento"].values(),inventario["Unidades"].values(), color = "g", alpha = 0.5, align="center")
plt.xlabel("Elemento")
plt.ylabel("Unidades")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("Elemento vs Unidades.png")
plt.close()
plt.show()

inventario = p.read_csv("inventario.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(inventario)
plt.title("Elementos vs Elementos Viejos", fontsize=20)
plt.bar(inventario["Elemento"].values(),inventario["Viejo"].values(),color = "y",alpha = 0.5,align="center")
plt.xlabel("Elemento")
plt.ylabel("Elementos Viejos")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("Elemento vs Elementos Viejos.png")
plt.close()
plt.show()

inventario = p.read_csv("inventario.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(inventario)
plt.title("Elementos vs Elementos Nuevos", fontsize=20)
plt.bar(inventario["Elemento"].values(),inventario["Nuevos"].values(),color = "b",alpha = 0.5,align="center")
plt.xlabel("Elemento")
plt.ylabel("Elementos Nuevos")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("Elemento vs Elementos Nuevos.png")
plt.close()
plt.show()

#-----------Graficos de Barras-------------#
#-------------Grafico de PPG---------------#

ppg = p.read_csv("ppg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x = list(ppg["muestra"].values())
y = list(ppg["valor"].values())
plt.title("PPG Paciente")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("PPG Paciente.png")
plt.close()
plt.show()

print ("El numero de picos en el PPG del pacientes es de 9")
#-------------Grafico de PPG---------------#
#-------------Grafico de Pie---------------#

labels = 'Recuperacion en Casa', 'Hospitalizados', 'UCI'
sizes = [85,10,5]
explode = (0, 0, 0.1)  
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("Casos Diagnosticados de Covid-19")
plt.savefig("Casos Diagnosticados de Covid-19.png")
plt.show()