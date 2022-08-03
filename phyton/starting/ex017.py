import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [12,10,9,7,5,3,1,3,4,6,9,10]

modelo = np.poly1d(np.polyfit(x,y,4))
linha = np.linspace(1,12,100)

plt.scatter(x,y)
plt.plot(linha,modelo(linha))
plt.show()

print(r2_score(y,modelo(x)))
predict = modelo(7.5)
print("Predict do valor 7.5:",predict)