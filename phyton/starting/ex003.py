import random
print(random.randrange(1,100))

texto = "o livro está na mesa"
if "livro" in texto:
    print("procede")
else:
    print("não procede")

print(texto.upper())

nome = "Gustavo"
time = "Inter"
texto2 = "Meu nome é {} e torço para o {}"
print(texto2.format(nome,time))

print(isinstance(nome,str))