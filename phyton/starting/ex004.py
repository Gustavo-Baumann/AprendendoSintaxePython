x = 10
y = 5

print(x > 5 and y > 5)
print(x > 5 or y > 5)
print(not(x > 5 and y > 5))

carros = ["Supra","Tesla","GTR"]
carros.append("Corvette")
maisCarros = ["Porsche","BMW","Audi A3"]
carros.extend(maisCarros)
carros.pop(4)
carrosCopiados = carros.copy()
[print(z) for z in carrosCopiados]