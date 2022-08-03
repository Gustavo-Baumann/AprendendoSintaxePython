import os

try:
    arquivo = open("demo.txt","x")
    arquivo.write("olá meu amigo!")
    arquivo.close()
except:
    print("Algo deu errado ao criar o arquivo :P")

try:
    arquivo = open("demo.txt","r")
    print(arquivo.read())
    arquivo.close()
except:
    print("Algo deu errado ao ler o arquivo :P")

try:
    if os.path.exists("demo.txt"):
        os.remove("demo.txt")
except:
    print("Algo deu errado ao deletar o arquivo :P")