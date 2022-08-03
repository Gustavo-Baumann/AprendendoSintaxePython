import matplotlib.pyplot as plt
import numpy as np

xposition = np.array([1,35,60,90])
yposition = np.array([1,20,45,100])
plt.plot(xposition,yposition,marker = "o",linestyle = "dashed",color = "green")
plt.plot(yposition,xposition,marker = "o",linestyle = "dashed",color = "blue")
plt.title("Gráfico Exemplo",loc = "center")
plt.grid(axis= "y")
plt.show()

