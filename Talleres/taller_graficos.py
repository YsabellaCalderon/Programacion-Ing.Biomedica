#-------Graficos Barrios------#
import matplotlib.pyplot as plt
import pandas as p

barrios = p.read_csv("barrios.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(barrios)
plt.title("Consumos Barrios", fontsize=20)
plt.bar(barrios["Barrio"].values(),barrios["Agua"].values(),align="center")
plt.xlabel("Barrios")
plt.ylabel("Agua")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("Barrios.png")
plt.close()
plt.show()

barrios = p.read_csv("barrios.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(barrios)
plt.title("Consumos Barrios", fontsize=20)
plt.bar(barrios["Barrio"].values(),barrios["Gas"].values(),align="center")
plt.xlabel("Barrios")
plt.ylabel("GAs")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("Barrios.png")
plt.close()
plt.show()

#--------Graficos Pie--------#
labels = 'Bogota', 'Medellin', 'Leticia', 'Villavicencio'
sizes = [80,7,5,8]
explode = (0, 0, 0.1, 0)  
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("Casos de Covid-19")
plt.savefig("Grafico_pie.png")
plt.show()

#----------Grafico ECG--------#
ecg = p.read_csv("ecg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x = list(ecg["muestra"].values())
y = list(ecg["valor"].values())
plt.title("ECG-uV")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("ECG_Paciente.png")
plt.close()