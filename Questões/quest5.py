import numpy as np
import matplotlib.pyplot as plt

s = np.linspace(0, 10, 300)
R = 120*(0.72**s)

s_ponto = 9
R_ponto = 120*(0.72**s_ponto)

plt.figure(figsize=(10,4.5))
plt.plot(s, R)
plt.scatter([s_ponto], [R_ponto], color='red')
plt.xlabel("Dias")
plt.ylabel("Número de erros")
plt.title("Questão 5 - Matheus - 569559")
plt.grid(True)
plt.show()