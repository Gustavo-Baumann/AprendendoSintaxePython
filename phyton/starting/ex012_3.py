import matplotlib.pyplot as plt
import numpy as np

ocorrencias = np.random.normal(60,3,100)

plt.hist(ocorrencias)
plt.show()