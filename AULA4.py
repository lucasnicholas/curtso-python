print("EXERCICIO 1")

def print_twice(y):
    print(y)

def do_twice(f,x):
    f(x)
    f(x)
do_twice(print_twice,'spam')

def do_four(g,z):
    g(z)
    g(z)
def do_twice2(z):
    print(z)
    print(z)
do_four(do_twice2,'spam')
