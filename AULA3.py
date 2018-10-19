print("EXERCICIO 1")

def func_tipo(a):
    print(a)
    print(type(a))
func_tipo(3)


print("EXERCICIO 2")

def velmed(xi,xf,t):
    vm = (xf-xi)/t
    print("a velocidade media e",vm,"m/s")
velmed(0,50,100)

def velmed2(vi, t, a):
    v = vi + a*t
    print("a velocidade media e",v,"m/s")
velmed2(0,10,10)

print("EXERCICIO 3")

def angul(altura,sombra):
    tg=sombra/altura
    print(" o angulo zenital e",tg)
    return tg
angul(50,0.5)

print("EXERCICIO 4")


def milha_metro(milha,metro):

    convert_milha_em_metro=milha*1.61*10**3
    print("1 milha em metros e",convert_milha_em_metro)

    convert_metro_em_milha=metro/(1.61*10**3)
    print("1 metro em milhas e", convert_metro_em_milha)
milha_metro(1,1)

def hora_segundo(hora,segundo):
 
    convert_hora_em_segundo=hora*3600
    print("1 hora em segundos e",convert_hora_em_segundo)

    convert_segundo_em_hora=segundo/3600
    print("1 segundo em horas e",convert_segundo_em_hora)
hora_segundo(1,1)

def kmporhora(minuto,milha):
    convert_minuto_em_hora=minuto/60
    kmhora=(milha*1.61)/convert_minuto_em_hora
    minutoporkm=minuto/(milha*1.61)
    print("tempo medio por quilometro",minutoporkm,"minutos por hora")
    print("4milhas em 30 minutos equivale a",kmhora,"km/h")

kmporhora(30,4)















