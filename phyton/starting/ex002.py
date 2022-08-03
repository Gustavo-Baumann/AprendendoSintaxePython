x = "..."

def funcao():
    global x
    x = "daora"

funcao()
print('python é ' + x)

#list
frutas = ["laranja","banana","uva"]
#tupla
legumes = ("cenoura","pepino","batata")
#set
verduras = {"alface","repolho","salsa"}
#frozenset
coisasBoas = ({"cafe","chocolate","lasanha"})

contagem = range(5,0,-1)
for n in contagem:
    print(n)