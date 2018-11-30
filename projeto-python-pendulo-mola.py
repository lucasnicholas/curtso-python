import math

#Funcoes para calcular o valor de r e theta do Pendulo Mola
def pend_mola_rm(xm,zm): 
	rm = math.sqrt(xm*xm + zm*zm)
	return rm
def pend_mola_theta(xm,zm):
	thetam = 0
	if(zm < 0):
		thetam = math.atan(-1*xm/zm) 
	elif(xm < 0 and zm > 0):
		thetam = -1*math.pi/2 + math.atan(zm/xm)
	elif(xm > 0 and zm > 0):
		thetam = math.pi/2 + math.atan(zm/xm)
	#Essa condicao e para x e z definidos na origem
	elif(xm == 0 and zm == 0):
		thetam = 0
	return thetam

#Funcoes para calcular o valor de r e theta do Pendulo Simples
def pend_simples_rs(xs,zs):
	rs = math.sqrt(xs*xs + zs*zs)
	return rs
def pend_simples_theta(xs,zs):
	thetas = 0
	if(zs < 0):
		thetas = math.atan(-1*xs/zs)
	elif(xs < 0 and zs > 0):
		thetas = -1*math.pi/2 + math.atan(zs/xs)

	elif(xs > 0 and zs > 0):
		thetas = math.pi/2 + math.atan(zs/xs)
	#Essa condicao e para x e z definidos na origem
	elif(xs == 0 and zs == 0):
		thetas = 0
	return thetas

#Funcoes para calcular o valor da aceleracao nos eixos x e z do Pendulo Mola
def pend_mola_ax(rm, thetam):
	axm = -1*((k/m)*(rm-l0)*math.sin(thetam))
	return axm
def pend_mola_az(rm, thetam):
	azm = -1*g+((k/m)*(rm-l0)*math.cos(thetam))
	return azm

#Funcoes para calcular o valor da aceleracao nos eixos x e z do Pendulo Simpes

def pend_simples_ax(rs, thetas):
	axs = -1*(g*(math.cos(thetas)*math.sin(thetas)))
	return axs
def pend_simples_az(rs, thetas):
	azs = -1*g+(g*g*math.cos(thetas))
	return azs

#Input dos parametros do problema
print("Digite o valor do comprimento natural da mola, em metros: ")
l0 = float(input())
print("Digite o valor da massa do corpo, em quilogramas: ")
m = float(input())
print("Digite o valor da constante elastica da mola, em Newtons por metro: ")
k = float(input())
print("A aceleracao da gravidade considerada e de 9.8 metros por segundo ao quadrado")
print(" ")
g = 9.8

#Input das condicoes iniciais do problema
print("Digite o valor da posicao inicial da coordenada x, em metros: ")
xm = xs = float(input())
print("Digite o valor da posicao inicial da coordenada z, em metros: ")
zm = zs = float(input())
print("Digite o valor da velocidade inicial da coordenada x, em metros por segundo: ")
vxm = vxs = float(input())
print("Digite o valor da velocidade inicial da coordenada z, em metros por segundo: ")
vzm = vzs = float(input())
print("Digite o valor do tempo final, em segundos: ")
tf = float(input())
print("Digite o valor do intervalo de tempo, em segundos: ")
dt = float(input())
print("O valor do tempo inicial sera de 0 segundos")
print(" ")
t = 0

#Criando as listas para armazenar os valores das variaveis no pendulo mola

axm_lista = [] #lista para aceleracao na coordenada x 
azm_lista = [] #lista para aceleracao na coordenada z 
am_lista = [] #lista para modulo da aceleracao
vxm_lista = [] #lista para velocidade na coordenada x
vzm_lista = [] #lista para velocidade na coordenada z 
vm_lista = [] #lista para modulo da velocidade
xm_lista = [] #lista para posicao na coordenada x
zm_lista = [] #lista para posicao na coordenada z
rm_lista = [] #lista para comprimento da mola

#Criando as listas para armazenar os valores das variaveis no pendulo mola

axs_lista = [] #lista para aceleracao na coordenada x 
azs_lista = [] #lista para aceleracao na coordenada z
asimp_lista = [] #lista para modulo aceleracao
vxs_lista = [] #lista para velocidade na coordenada x
vzs_lista = [] #lista para velocidade na coordenada z
vs_lista = [] #lista para modulo da velocidade
xs_lista = [] #lista para posicao na coordenada x
zs_lista = [] #lista para posicao na coordenada z
rs_lista = [] #lista para comprimento

t_lista = []

#Calculo das variaveis
while t <= tf:
    #Pendulo Mola
	rm = pend_mola_rm(xm,zm)
	thetam = pend_mola_theta(xm,zm)
	axm = pend_mola_ax(rm,thetam)
	azm = pend_mola_az(rm,thetam)
	am = math.sqrt(axm*axm + azm*azm)
	vxm = vxm + axm*dt
	vzm = vzm + azm*dt
	vm = math.sqrt(vxm*vxm + vzm*vzm)
	xm = xm + vxm*dt
	zm = zm + vzm*dt
	axm_lista.append(axm)
	azm_lista.append(azm)
	am_lista.append(am)
	vxm_lista.append(vxm)
	vzm_lista.append(vzm)
	vm_lista.append(vm)
	xm_lista.append(xm)
	zm_lista.append(zm)
	rm_lista.append(rm)
	#Pendulo Simples
	rs = pend_simples_rs(xs,zs)
	thetas = pend_simples_theta(xs,zs)
	axs = pend_simples_ax(rs,thetas)
	azs = pend_simples_az(rs,thetas)
	asimp = math.sqrt(axs*axs + azs*azs)
	vxs = vxs + axs*dt
	vzs = vzs + azs*dt
	vs = math.sqrt(vxs*vxs + vzs*vzs)
	xs = xs + vxs*dt
	zs = zs + vzs*dt
	axs_lista.append(axs)
	azs_lista.append(azs)
	asimp_lista.append(asimp)
	vxs_lista.append(vxs)
	vzs_lista.append(vzs)
	vs_lista.append(vs)
	xs_lista.append(xs)
	zs_lista.append(zs)
	rs_lista.append(rs)
	#valores para o tempo
	t = t + dt
	t_lista.append(t)

#Imprimindo tabelas de resultados

print("Posicao Pendulo Mola")
print("  ")

for x in range(len(xm_lista)):
	print("x = ", xm_lista[x], "em metros | z = ", zm_lista[x], "em metros")

print("  ")
print("Velocidade Pendulo Mola")
print("  ")

for x in range(len(vxm_lista)):
	print("vx = ", vxm_lista[x], "em metros por segundo | vz = ", vzm_lista[x], "em metros por segundo")

print("  ")
print("Aceleracao Pendulo Mola")
print("  ")

for x in range(len(axm_lista)):
	print("ax = ", axm_lista[x], "em metros por segundo ao quadrado | az = ", azm_lista[x], "em metros por segundo ao quadrado")

print("  ")
print("Posicao Pendulo Simples")
print("  ")

for x in range(len(xs_lista)):
	print("x = ", xs_lista[x], "em metros | z = ", zs_lista[x], "em metros")

print("  ")
print("Velocidade Pendulo Simples")
print("  ")

for x in range(len(vxs_lista)):
	print("vx = ", vxs_lista[x], "em metros por segundo | vz = ", vzs_lista[x], "em metros por segundo")

print("  ")
print("Aceleracao Pendulo Simples")
print("  ")

for x in range(len(axs_lista)):
	print("ax = ", axs_lista[x], "em metros por segundo ao quadrado | az = ", azs_lista[x], "em metros por segundo ao quadrado")

print("  ")
print("Tempo")
print("  ")

for x in range(len(t_lista)):
	print("t = ", t_lista[x], "em segundos")


#Utilizando o matplotlib para fazer os graficos do pendulo mola e pendulo simples

#Pendulo mola
import matplotlib.pyplot as VmvsT
import matplotlib.pyplot as RmvsT
import matplotlib.pyplot as AmvsT
import matplotlib.pyplot as VxmvsXm
import matplotlib.pyplot as ZmvsXm


VmvsT.plot(t_lista,vm_lista)
VmvsT.xlabel("tempo(s)")
VmvsT.ylabel("Velocidade (m/s)")
VmvsT.show()
VmvsT.close()

RmvsT.plot(t_lista, rm_lista)
RmvsT.xlabel("tempo(s)")
RmvsT.ylabel("Comprimento da mola(m)")
RmvsT.show()
RmvsT.close()

AmvsT.plot(t_lista, am_lista)
AmvsT.xlabel("tempo(s)")
AmvsT.ylabel("Aceleracao(m/s^2)")
AmvsT.show()
AmvsT.close()

VxmvsXm.plot(xm_lista, vxm_lista)
VxmvsXm.xlabel("x(m)")
VxmvsXm.ylabel("Velocidade em x(m/s))")
VxmvsXm.show()
VxmvsXm.close()

ZmvsXm.plot(xm_lista, zm_lista)
ZmvsXm.xlabel("x(m)")
ZmvsXm.ylabel("z(m)")
ZmvsXm.show()
ZmvsXm.close()


#Pendulo simples
import matplotlib.pyplot as VsvsT
import matplotlib.pyplot as RsvsT
import matplotlib.pyplot as AsvsT
import matplotlib.pyplot as VxsvsXs
import matplotlib.pyplot as ZsvsXs


VsvsT.plot(t_lista,vs_lista)
VsvsT.xlabel("tempo(s)")
VsvsT.ylabel("Velocidade (m/s)")
VsvsT.show()
VsvsT.close()

RsvsT.plot(t_lista, rs_lista)
RsvsT.xlabel("tempo(s)")
RsvsT.ylabel("Comprimento(m)")
RsvsT.show()
RsvsT.close()

AsvsT.plot(t_lista, asimp_lista)
AsvsT.xlabel("tempo(s)")
AsvsT.ylabel("Aceleracao(m/s^2)")
AsvsT.show()
AsvsT.close()

VxsvsXs.plot(xs_lista, vxs_lista)
VxsvsXs.xlabel("x(m)")
VxsvsXs.ylabel("Velocidade em x(m/s))")
VxsvsXs.show()
VxsvsXs.close()

ZsvsXs.plot(xs_lista, zs_lista)
ZsvsXs.xlabel("x(m)")
ZsvsXs.ylabel("z(m)")
ZsvsXs.show()
ZsvsXs.close()
