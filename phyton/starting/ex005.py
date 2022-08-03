meuSet = {"PC","Monitor","Teclado"}
meuSet.add("Mouse")
meuOutroSet = {"Cadeira","Mesa","Microfone"}
meuSet.update(meuOutroSet)

for item in meuSet:
    print(item)

if len(meuSet) > 10:
    print("Set profissional")
elif len(meuSet) <= 10:
    print("Set humilde")

while len(meuSet) > 0:
    meuSet.pop()
else:
    print("Set Esvaziado")