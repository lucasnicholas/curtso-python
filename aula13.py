'''print("Exercicio 1")

ler = open('dados_alunos.txt')
linhas = ler.readlines()
coluna1 = []
coluna2 = []
coluna3 = []
for line in linhas:
	result = line.split()
	coluna1.append(result[0])
	coluna2.append(result[1])
	coluna3.append(result[2])
ler.close()

import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
plt1.hist(coluna1,1,'red')
plt1.xlabel("Idade(anos)")
plt1.ylabel("Frequencia")
plt1.show()
plt2.hist(coluna2,0.05,'red')
plt2.xlabel("Altura(m)")
plt2.ylabel("Frequencia")
plt2.show()
plt3.hist(coluna3,2,'red')
plt3.xlabel("Peso(kg)")
plt3.ylabel("Frequencia")
plt3.show()
'''
print("Exercicio 2")

import os

for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

print("Exercicio 3")

import wc

wc.linecount('dados_alunos.txt')

