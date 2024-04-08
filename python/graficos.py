
#visualização de dados em python

import matplotlib.pyplot as plt

x = [1, 2, 5]
y = [2, 3, 7]

plt.title("Meu primeiro gráfico com Python")

plt.xlabel("Eixo X")
plt.ylabel("Eixo y")

plt.plot(x,y)
plt.show()