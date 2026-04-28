import numpy as np
import matplotlib.pyplot as plt

h = np.linspace(0, 24, 300)
T = 70 + 15*np.sin((np.pi/6)*(h - 3))

h_ponto = 6
T_ponto = 70 + 15*np.sin((np.pi/6)*(h_ponto - 3))

plt.figure(figsize=(10,4.5))
plt.plot(h, T)
plt.scatter([h_ponto], [T_ponto], color='red')
plt.xlabel("Horário (h)")
plt.ylabel("Temperatura (°C)")
plt.title("Questão 3 - Matheus - 569559")
plt.grid(True)
plt.show()