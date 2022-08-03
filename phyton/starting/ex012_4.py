import matplotlib.pyplot as plt
import numpy as np

pie = np.array([42,18,27,13])
labels = ["Azul","Laranja","Verde","Vermelho"]
separamento = [0.1,0,0,0]

plt.pie(pie,labels = labels,startangle = 180, explode = separamento)
plt.show()