print("EXERCICIO 1")

def f(x,y,z): 
    if z>y>x :
        print (z, " e o maior.")

f(2,3,4)

print("EXERCICIO 2")

def somando(lista):
    l = lista
    return l

l = somando([11,10,10])
soma = 0
for i in range(len(l)):
    soma += l[i]
print(soma)



print("EXERCICIO 3")

def multiplica(lista2):
    l = lista2
    return l

l = multiplica([10,10,10])
multip = 1
for i in range(len(l)):
    multip *= l[i]
print(multip)


print("EXERCICIO 4")

def g(x):
    if x >= 100 and x <= 200:
        print(x, " esta entre 100 e 200")
g(150)


print("EXERCICIO 5")

def par(lista3):
    l = lista3
    return l
listapar = []

l = [1,2,3,4,5,6,7,8,9,10,11,12]
for i in range(len(l)):
    if(l[i] % 2 == 0):
        #print(l[i],"Número par.")
        listapar.append(l[i]) 
print (listapar)
           









