import turtle
from turtle import Turtle
turtle.speed(10)
print("EXERCICIO 1")

jn = turtle.Screen() 

def posicao(l,n):
    turtle.penup()
    turtle.setx(l)
    turtle.sety(n)
    turtle.pendown()
posicao(100,100)

def desenho1(tamanho, cor,x,y):
    angul = 120
    turtle.fillcolor(cor)
    turtle.begin_fill()

    for side in range(x):
        turtle.forward(tamanho)
        turtle.right(angul)
        turtle.forward(tamanho)
        turtle.right(y - angul)
    turtle.end_fill()
    return

desenho1(100, "purple",10,36)

turtle.resetscreen()

print("EXERCICIO 2")



jn2 = turtle.Screen() 
def flor(turtle, raio):
    heading = turtle.heading()
    turtle.circle(raio, 60)
    turtle.left(120)
    turtle.circle(raio, 60)
    turtle.setheading(heading)

bigode = Turtle()
bigode.color("red")
bigode.fillcolor("red")
bigode.speed(90)
bigode.begin_fill()
bigode.pensize(5)  

for _ in range(20):
    flor(bigode, 100)
    bigode.left(360 / 20)
bigode.end_fill()

bigode.color("green")
bigode.fillcolor("green")
bigode.begin_fill()

bigode.right(90)
bigode.forward(200)

bigode.circle(100, 60)
bigode.left(120)
bigode.circle(100, 60)
bigode.end_fill()


jn2 = turtle.mainloop() 






