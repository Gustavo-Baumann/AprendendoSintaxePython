try:
    n1 = float(input("digite um número: "))
    n2 = float(input("digite outro número: "))
    resultado = n1 + n2
    print("O resultado da soma dos números é", resultado)
except:
    print("Input inválido. Tente Novamente")
else:
    print("Obrigado por usar nossa calculadora")