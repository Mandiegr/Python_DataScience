
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