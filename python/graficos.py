
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

# Scatterplot: Gráfico de dispersão

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]


titulo = "Scatterplot: Gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

plt.title(titulo)
plt.xlabel("Eixox")
plt.ylabel("Eixoy")

plt.scatter(x, y, label="Meus pontos", color="r")
plt.plot(x, y)
plt.legend()

plt.show()

# Inserindo pontos nos gráficos de linha

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [200, 25, 400, 3300, 100]
 
titulo = "Scatterplot: gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"
 
# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
 
plt.plot(x, y, color="#000000", linestyle="--")
plt.scatter(x, y, label="Meus pontos", color="k", marker=".", s=z)
plt.legend()
plt.show()
plt.savefig("figura1.png", dpi=300) # salva o gráfico na pasta em que foi criado o projeto

# Atividade:  Estudo de caso: crescimento da população brasileira

dados = open("populacao_brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
	if i != 0:
		linha = dados[i].split(";")
		x.append(int(linha[0]))
		y.append(int(linha[1]))

plt.bar(x, y, color="#e4e4e4")
plt.plot(x, y, color='k', linestyle="--")

plt.title("Crescimento da População Brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")
#plt.show()
plt.savefig("populacao_brasileira.png", dpi=300)


"""
Documentação oficial do Matplotlib
A seguir, alguns exemplos de argumentos que podem ser aplicados ao método plot( ).



color: cor (ver exemplos abaixo)

label: rótulo

linestyle: estilo de linha (ver exemplos abaixo)

linewidth: largura da linha

marker: marcador (ver exemplos abaixo)



CORES (color)
'b' blue

'g' green

'r' red

'c' cyan

'm' magenta

'y' yellow

'k' black

'w' white



Marcadores (marker)
'.' point marker

',' pixel marker

'o' circle marker

'v' triangle_down marker

'^' triangle_up marker

'<' triangle_left marker

'>' triangle_right marker

'1' tri_down marker

'2' tri_up marker

'3' tri_left marker

'4' tri_right marker

's' square marker

'p' pentagon marker

'*' star marker

'h' hexagon1 marker

'H' hexagon2 marker

'+' plus marker

'x' x marker

'D' diamond marker

'd' thin_diamond marker

'|' vline marker

'_' hline marker





Tipos de linha (linestyle)
'-' solid line style

'--' dashed line style

'-.' dash-dot line style

':' dotted line style



Fonte: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.htm

"""