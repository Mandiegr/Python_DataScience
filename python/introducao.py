# python do básico ao avançado 

""" Aula 1-8: oomentários e operacoes matemáticas
# Fromas de comentar no código
- para exibir temos que usar o print na frente: print("***")
- python n reconhece acentos: " Ç ` ^ ~ "
- Para os acentos serem reconhecidos, use no inicio do codigo: -*- coding: utf-* -*-
- sinais: * multiplica, ** expoente,  %  resto

print("Hellò, world!")
print("Amanda")
print( 4 * 5)

"""

"""Aula 9: variáveis

- Var é um espaço na memória que guarda informaçôes
- n deve ter caracteres especiais nem espaços:
.Nome_da_variavel
.nome_da_variavel
= é operador de atribuição
Valor: define o tipo da var
name = "john"
var = valor

my_variable = "Hello, world!"
print(my_variable)

var1 = 1 # variavel inteira
var2 = 1.98 # variavel float
var3 = " Eu sou uma string" # variavel string
var4 = true # boolean true
var4= false # boolean false

print(var4) #dentro dos parenteses coloque a variavel que deseja exibir

"""

"""Aula 10: Operadores

x = 10    |  x recebe o valor 10
----------------------------------
x = 5
y = 5

print( x == y) 

true pq 5 é igual a 5
             ou
             ==
--------------------------------------


-------------------------------------
x = 5
y = 3

print( x < y)

false pq x/5 não é menor que y/3
-----------------------------------

----------------------------------
x = 5
y = 3

print( x > y)

true pq x/5 é maior que y/3
---------------------------------

----------------------------------
x = 5
y = 4

soma = x + y

print( soma )

r: 9
-------------------------------------

-------------------------------------

x = 5
y = 4

soma = x + y = 9

print( soma > y) = soma: 9 + y/4 -> soma é maior que Y? sim pq a soma dos valores x e y é 9 sendo maior 4

true pq a soma das variaveis é 9, assim, 9 é maior que y/4
"""

""" Aula 11: Operadores Relacionais

#operadores logicos : condicionais 

Opoerador

AND = Duas condicoes tem que ser true
OR  = Pelos menos uma condição seja true
NOT = inverte o valor 
-----------------------------------
x = 5
y = 4

soma = x + y

print( soma == y and x == soma)

false pois x e y não são iguais a soma 
-------------------------------------
"""

"""Aula 12: Estruturas Condicionais If

condicional if
. realiza testes condicionais
.executa um bloco Se uma determinada condição for atendida
.Avalia se condição é verdadeira ou não

-------------------------------

x = 1
y = 100000000

if x > y :
print("x é maior que y")

if y > x:
print("y é maior que x")

r: y é maior que x
---------------------------------------

if x > 0:
    print("x é positivo")
elif x < 0:
    print("x é negativo")
else:
    print("x é igual a zero")
    
-------------------------------------------

"""

"""Aula 13: Estruturas condicionais: Else

x = 1
y = 5

if x > y :
print("x é maior que y")

else:
print("x não é maior que y")

"""

"""Aula 14: Estruturas Condicionais: elif

É executado caso a condição do comando is não seja atendida,
executando a primeira opção verdadeira que encontrar
-------------------------------
x = 1
y = 5

if x == y :
print("numeros iguais")
elif y > x:
print("y é maior que x")
else:
print("numeros diferentes")

r: y é maior que x, pq a condição do if não foi atendida e já que y é maior que x o elif será exibido,
caso elif não atendesse a condição o else seria exibido.
--------------------------------------

"""

"""Aula 15: Estrutura de Repetição: While
.Estruturas de Repetição
.Iteradores iterar == repetir
.Repetem um trecho do código:
_enquanto uma condição for avaliada true
_durante uma pré-determinada condição
--------------------------------

x = 1

while x < 10:
print(x)
x = x+1 # para iterar e a cada rodada vai adicioando +1
r:
1
2
3
4
5
6
7
8
9 
-----------------------------------

x = 1

while x < 10:
print(x)
x += 1
------------------------------------

numero = 1

while numero <= 5:
    print(numero)
    numero += 1
    
---------------------------------------
"""

"""Aula 16: Estrutura de Repetição: for
for: percore uma lista, array

------------------------------------------

lista1 = [1,2,3,4,5]
lista2 = ["ola", "mundo", "!"]
lista3 = [0, "ola", "biscoito", 8.97, True]

for i in lista3:
print(i)

r: 
0
ola
biscoito
8.97
True

O loop for percorre cada elemento da lista3,
e o comando print(i) exibe cada elemento em uma nova linha.
O código é uma maneira simples de percorrer e exibir os elementos 
de uma lista.

-----------------------------------------------

"""

"""Aula 17: for e range 
range retorna uma lista

---------------------------------
for i in range(10,20,2):
print(i)

r: 
10
12
14
16
18

range(10, 20, 2) gera uma sequência de números começando de 10
indo até 20 (exclusivo), com um passo de 2.
O loop for itera sobre essa sequência.
A função print(i) exibe cada valor da sequência em uma nova linha.
Dessa forma, o código imprime os números 10, 12, 14, 16 e 18
que são os números gerados pela função range() com o passo de 2.
-------------------------------- 
"""

"""Aula 18: Objetos
Em Python, tudo é um objeto. Isso significa que cada dado, função ou,
módulo é encapsulado em um objeto com suas próprias características e comportamentos.

Objetos são instâncias de classes. Por exemplo, quando você cria uma 
variável com uma string, você está criando um objeto do tipo string.

Objetos possuem atributos (características) e
métodos (ações que podem ser aplicadas).


Atributos: São as características do objeto, como nome, cor, tamanho etc.
Métodos: São as ações que o objeto pode realizar, como calcular área, mover, imprimir etc.
Observe como verificar atributos e métodos a um objeto:
objeto.atributo
objeto.método( )

----------------------------------------------
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Olá, meu nome é {self.nome}!")

pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)

pessoa1.falar()
pessoa2.falar()
---------------------------------------------------------

"""

"""Aula 19: Strings pt- 1

-----------------------------
a = "Diego"
b = "Mariano"

concatenar = a + "" + b
print(concatenar)
----------------------------

"""

"""Aula 20 : Srtings
Em python strings são objetos

string = string.metodo

------------------------------
a = "Amanda"
b = "Gomes"

concatenar = a + " " + b

print(concatenar)
--------------------------------
--------------------------------
a = "Amanda"
b = "Gomes"

concatenar = a + " " + b

print(concatenar)
concatenar = concatenar.upper()

print(concatenar)
---------------------------------

------------------------------------------------------------------
a = "Amanda"
b = "Gomes"

concatenar = a + " " + b + "\n" # \n quebra linha

print(concatenar.strip()) # o strip remove caractere especial -> \n
---------------------------------------------------------------------

-------------------------------------------------------------
minha_string = "O rato roeu a roupa do rei de roma"

minha_lista = minha_string.split()

print(minha_lista) 

['O', 'rato', 'roeu', 'a', 'roupa', 'do', 'rei', 'de', 'roma']
-------------------------------------------------------------

-------------------------------------------------------------

minha_string = "O rato roeu a roupa do rei de roma"

minha_lista = minha_string.find("rei")

print(minha_lista) 

-----------------------------------------------------------------

---------------------------------------------------------------

minha_string = "O rato roeu a roupa do rei de roma"

minha_lista = minha_string.replace("rei", "rainha")

print(minha_lista) 

rato roeu a roupa do rainha de roma

----------------------------------------------------------------

----------------------------------------------------------------

minha_string = "O rato roeu a roupa do rei de roma"

minha_lista = minha_string.replace("rei", "rainha")

print(minha_lista) 

O rato roeu a roupa do rainha de roma
-----------------------------------------------------------
"""
"""Aula 21: funcoes
Em python as funcoes são definidas pela palavra resevada def

. Definição 
def Nome(Parâmetros)

Comandos

.Chamadas

Nome(Argumentos)

-----------------------------------------------

def soma( x, y):
return x + y
s = soma(2, 3)
print(s)

r: 5
---------------------------------------------------

---------------------------------------------------

def soma( x, y):
return x + y

def multiplicacao(x, y):
return x * y

s = soma(2, 3)
m = multiplicacao(4, 7)
print(m)

-------------------------------------------------------

-------------------------------------------------------

def soma( x, y):
return x + y

def multiplicacao(x, y):
return x * y

s = soma(2, 3)
m = multiplicacao(4, 7)

print(soma(s, m))

r: 33 
-----------------------------------------------------------
""" 

"""Aula 22:Arquivos

arquivo = open("arquivo.txt")

linhas = arquivo.readlines()

print(linhas)

['Meu arquivo\n', 'Olá, Mundo']

readlines ler todas as linhas do arquivo e retorna tudo dentro de uma lista

---------------------------------------------
arquivo = open("arquivo.txt")

linhas = arquivo.readlines()

for linha in linhas:
print(linha)
Meu arquivo

Olá, Mundo
-----------------------------------------------

------------------------------------------
arquivo = open("arquivo.txt")

texto_completo = arquivo.read()
print(texto_completo)

retorna tudo dentro de uma unica variavel
-----------------------------------------

-----------------------------------------------

w = open("arquivo2.txt", "w") # cria um arquivo : w = open("arquivo2.txt", "w")

w.write("Esse é o meu arquivo 2") # escre no arquivo: w.write("Esse é o meu arquivo 2")

w.close() # fecha o arquivo, é bom fexhar quando utiliza mais de um arq

------------------------------------------------------

"""

"""Aula 23-24:Listas

--------------------------------

minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1,2,3,4,5]
minha_lista3 = ["abacaxi", 2, 9.84, True]

print(minha_lista2[3])

r: 4
-------------------------------------------

-------------------------------------------
minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1,2,3,4,5]
minha_lista3 = ["abacaxi", 2, 9.84, True]

for item in minha_lista:
print(item)
vai navegar pelos elementos da lista e retonar item por item daquela lista
------------------------------------------

--------------------------------------------------------
minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1,2,3,4,5]
minha_lista3 = ["abacaxi", 2, 9.84, True]

tamanho = len(minha_lista) # len == tamanho

print(tamanho)

r: 3

-------------------------------------------------------------

-------------------------------------------------------

minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1,2,3,4,5]
minha_lista3 = ["abacaxi", 2, 9.84, True]

minha_lista.append("banana") #append == adiciona elemento

print(minha_lista)

r: ['abacaxi', 'melancia', 'abacate', 'banana']

------------------------------------------------------

------------------------------------------------------
minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1,2,3,4,5]
minha_lista3 = ["abacaxi", 2, 9.84, True]

minha_lista.append("banana")

if 3 in minha_lista2: 
print("3 está na lista 2")
r: 3 está na lista 2
---------------------------------------------------------

------------------------------------------------------
minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1,2,3,4,5]
minha_lista3 = ["abacaxi", 2, 9.84, True]

minha_lista.append("banana")

del minha_lista[2:] # del == remove 
print(minha_lista)
------------------------------------------------

-------------------------------------------------
lista = [3, 9, 1, 200, 56, 29]

lista.sort() # ordena lista alterando a lista e não retornando outra

print(lista)

[1, 3, 9, 29, 56, 200]

------------------------------------------------

--------------------------------------------------

lista = [3, 9, 1, 200, 56, 29]

lista.sort(reverse=True)

print(lista)

[200, 56, 29, 9, 3, 1]

-------------------------------------------------

lista = [3, 9, 1, 200, 56, 29]

lista.reverse()

print(lista)

"""

"""Aula 25-26: dicionarios 

Dicionários

-
Em Python, dicionários são arrays associativos, ou seja, um determinado valor passa a ser vinculado a uma chave. Exemplo:

# dicionarios em python
dicionario_sites = {"Diego": "diegomariano.com"}

No dicionário acima, a chave "Diego" foi vinculado ao valor "diegomariano.com". Assim, para imprimir o valor chame:

print(dicionario_sites['Diego'])
# Sera impresso "diegomariano.com

Se o dicionário tiver vários elementos, você pode usar laços para imprimi-los:

# dicionarios em python
dicionario_sites = {"Diego": "diegomariano.com", "Google": "google.com", "Udemy": "udemy.com"}
for chave in dicionario_sites:
print(dicionario_sites[chave])
Dicionarios são listas de associacoes compostas por:
* uma chave
* uma valor conrrespondente

dicionario = {"chave": "valor"}

declarado entre chaves {}
enquanro listas entre conchete [], mas usamos o [] para buscar o valor
-----------------------------------------------------------

# chave = valor vinculado
meu_dicionario = {"A": "Amanda", "B":"Bruna", "C": "Charlie"}

print(meu_dicionario["B"])

r: Bruna

--------------------------------------------------------------
# chave = valor vinculado
meu_dicionario = {"A": "Amanda", "B":"Bruna", "C": "Charlie"}

# para cada chave dentro do meu dicionario print a chave
for chave in meu_dicionario:
print(chave)
r: 
A
B
C

---------------------------------------------------------------

# chave = valor vinculado
meu_dicionario = {"A": "Amanda", "B":"Bruna", "C": "Charlie"}

# para cada chave dentro do meu dicionario print a chave
for chave in meu_dicionario:
print(meu_dicionario[chave]) # estanos pegando o valor das chaves

r:
Amanda
Bruna
Charlie
-------------------------------------------------------------------

# chave = valor vinculado
meu_dicionario = {"A": "Amanda", "B":"Bruna", "C": "Charlie"}

# para cada chave dentro do meu dicionario print a chave
for chave in meu_dicionario:
print(chave+":"+meu_dicionario[chave]) 

r: 
A:Amanda
B:Bruna
C:Charlie

"""

"""Aula 27 : numeros aleatorios
-----------------------------------
import random

numero = random.randint(0, 10)
print(numero)

---------------------------------------

---------------------------------------

import random

random.seed(0) # forca permanece o primeiro numero aletorio que aparecer
numero = random.randint(0, 10)
print(numero)

----------------------------------------------

----------------------------------------------
import random

lista = [3, 6, 5, 4, 2, 19]
numero = random.choice(lista) # choice escolhe um n aleatorio de uma lista
print(numero)

------------------------------------
"""

"""Aula 28: Tratamento de excecoes

a = 2
b = 0

# tenta
try: 
print(a/b)
except: #excecao
print("Não é permitido divisão por 0")

print(a/a)

"""

"""Aula 29 - 32
Em python 3, deve-se usar apenas input( ) para strings, e para números deve-se combinar com as funções float ou int. Veja:

# Recebendo textos
meu_texto = input("Digite um texto: ")
# Recebendo números
numero_inteiro = int(input("Digite um numero inteiro: "))
numero_decimal = float(input("Digite um numero decimal: "))

exercicios:

--------------------------------------------
idade = int(input("Digite sua idade: "))
if idade >= 18:
print("Maior de idade")
elif idade < 18:
print("Menor de idade")
-------------------------------------------

. Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado. 

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1+nota2)/2
if media >= 6:
print("Aprovado")
else:
print("Reprovado")

3. Escreva um programa que resolva uma equação de segundo grau. 

from math import sqrt
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
delta = b**2 - 4*a*c
if delta < 0:
print("Delta negativo")
else:
raiz_delta = sqrt(delta)
x1 = (-b + raiz_delta)/2*a
x2 = (-b - raiz_delta)/2*a
print("As raízes são", x1, "e", x2)

4. Escreva um programa que ordene uma lista numérica com três elementos. 

lista = [3,2,1]
print(sorted(lista))

5. Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal. 

n1 = int(input("Digite o primeiro número: "))
sinal = input("Digite o sinal: ")
n2 = int(input("Digite o segundo número: "))
if sinal == "+":
op = n1 + n2
elif sinal == "-":
op = n1 - n2
elif sinal == "/":
op = n1 + n2
elif sinal == "*":
op = n1 * n2
else:
print("Sinal inválido.")
print(op)


"""

"""Aula 33 - 38 python avançado

A seguir serão apresentados alguns tópicos avançados em Python:

list comprehension

x = [1,2,3,4,5]
y = []

for i in x:
y.append(i**2)
print(x)
print(y)

r:
[1, 2, 3, 4, 5]
[1, 4, 9, 16, 25]
-------------------------------------------

------------------------------------------
x = [1,2,3,4,5]
y = [i**2 for i in x]

print("usando list comprehension")
print(x)
print(y)

----------------------------------------------

x = [1,2,3,4,5]
y = [i**2 for i in x]
z = [i for i in x if i%2==1] # imprimir numeros impares

print(z)

[1, 3, 5]

-----------------------------------------------------

enumerate

lista = ["abacate", "bola", "cachorro"]

for i, nome in enumerate(lista):
print(i, nome)

R:
0 abacate
1 bola
2 cachorro
----------------------------------------------------------
map



reduce

zip

filter

"""

"""Exercicio

seq1 = input("Digite a sequência 1: ")
seq2 = input("Digite a sequência 2: ")

if seq1 == seq2:
print("Sequências iguais")
else:
print("Sequências diferentes")
------------------------------------------------
import re

seq1 = input("Digite a sequência 1: ")
seq2 = input("Digite a sequência 2: ")

busca = re.fullmatch(seq1, seq2)

if busca:
print("Sequências idênticas")
print(busca.group())
else:
print("Sequências diferentes")
----------------------------------------------

import re

seq1 = "AT.G"
seq2 = "ATTGAAAAAG"

busca = re.fullmatch(seq1, seq2)

if busca:
print("Sequências idênticas")
print(busca.group())
else:
print("Sequências diferentes")
#match -> compara apenas o incio, enquanto o fullmatch compara toda a sequencia
------------------------------------------
nome = input("Digite o nome do arquivo que você deseja abrir:")

arquivo = open(nome)

linhas = arquivo.readlines()
for linha in linhas:
print(linha.strip()) #strip -> remove caracteres especiais como espaço
em outro arquivo:
seq.fasta {
>gi|5524211|gb|AAD44166.1| cytochrome b [Elephas maximus maximus]
LCLYTHIGRNIYYGSYLYSETWNTGIMLLLITMATAFMGYVLPWGQMSFWGATVITNLFSAIPYIGTNLV
EWIWGGFSVDKATLNRFFAFHFILPFTMVALAGVHLTFLHETGSNNPLGLTSDSDKIPFHPYYTIKDFLG
LLILILLLLLLALLSPDMLGDPDNHMPADPLNTPLHIKPEWYFLFAYAILRSVPNKLGGVLALFLSIVIL
GLMPFLHTSKHRSMMLRPLSQALFWTLTMDLLTLTWIGSQPVEYPYTIIGQMASILYFSIILAFLPIAGX
IENY
}
-----------------------------------------------------------------------

seq = input("digite uma sequência:")

arquivo = open("seq2.fasta","w") # cria um arquivo 

arquivo.write(">seq\n")
arquivo.write(seq)

arquivo.close()


# digite uma sequência:AAGTOOO 
# more seq2.fasta
# >seq
# AAGTOOO

"""

"""menu = 0

def abrirArquivo():
nome = input("Digite o nome do arquivo que deseja abrir:")
arquivo = open(nome)
return arquivo

def lerArquivo(arquivo):
linhas = arquivo.readLines()
for linha in linhas:
print(linha.strip())
while menu != 3:
print("(1) Abrir arquivo\n(2) Ler arquivo aberto\n(3)Sair\n")
menu = input("Digite a opção desejada:")
if menu == 1:
arquivo = abrirArquivo()
elif menu == 2:
lerArquivo(arquivo) """



#conteudo: https://www.udemy.com/course/python-mysql