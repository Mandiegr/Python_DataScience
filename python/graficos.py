
#visualização de dados em python

import matplotlib.pyplot as plt

x = [1, 2, 5]
y = [2, 3, 7]

plt.title("Meu primeiro gráfico com Python")

plt.xlabel("Eixo X")
plt.ylabel("Eixo y")

plt.plot(x,y)
plt.show()

#Gráfico em barra

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

titulo = "Gráfico em barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

plt.title(titulo)
plt.xlabel("Eixo X")
plt.ylabel("Eixo y")

plt.bar(x,y)
plt.show()

#Comparação de duas barras X e Y

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

titulo = "Gráfico em barras 2"
eixox = "Eixo X"
eixoy = "Eixo Y"

plt.title(titulo)
plt.xlabel("Eixo X")
plt.ylabel("Eixo y")

plt.bar(x1,y1, label = "Grupo 1")
plt.bar(x2,y2, label = "Grupo 2")
plt.legend()

plt.show()