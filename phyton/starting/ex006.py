x,y = 100,10

def dividir(v1,v2):
    return v1/v2

z = dividir(x,y)
print("O resultado é:", z)

del x,y,z

def contar(num = 1):
    if num < 6:
        contar(num + 1)
        print(num)
    else:
        num = 0

contar()

valor = lambda a,b : a*b
print(valor(4,3))

grito = lambda texto : texto.upper()
print(grito("banana!"))