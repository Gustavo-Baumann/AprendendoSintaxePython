import matplotlib.pyplot as plt
import numpy as np

def geradorGrafico(lista):
    y = np.array(lista)
    plt.plot(y,marker = "o", linestyle = "dashed",color = "green")
    plt.grid(axis= "y")
    plt.title("Seu Gráfico")
    plt.show()

try:
    print("Olá meu amigo!")
    numIter = int(input("Digite quantas iterações você quer mostrar no seu gráfico: "))
    if numIter < 0:
        raise ArithmeticError
    else:
        arrayResultados = []
        iterRestantes = 0
        while iterRestantes < numIter:
            try:
                res = int(input("Digite o próximo valor: "))
                arrayResultados.append(res)
                iterRestantes += 1
            except:
                print("ERRO: número inválido")
    geradorGrafico(arrayResultados)
except ArithmeticError:
    print("ERRO: digite um número acima de 0")
except:
    print("ERRO: digite um número")