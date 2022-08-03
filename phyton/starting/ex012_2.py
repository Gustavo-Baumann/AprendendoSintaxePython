from turtle import color
import matplotlib.pyplot as plt
import numpy as np

opcoes = np.array(["Zé","Jão","Boca"])
votos = np.array([21,45,34])

plt.bar(opcoes,votos,color = "green",width = 0.6)

plt.xlabel("Candidatos")
plt.ylabel("Votos")
plt.title("Eleição")
plt.show()