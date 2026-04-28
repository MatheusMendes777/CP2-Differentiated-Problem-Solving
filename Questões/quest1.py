import numpy as np
import matplotlib.pyplot as plt

# intervalo de tempo
t = np.linspace(0, 6, 300)

# função
L = 180 + 45*np.cos((2*np.pi/3)*t)

# ponto calculado
t_ponto = 3
L_ponto = 180 + 45*np.cos((2*np.pi/3)*t_ponto)

# gráfico
plt.figure(figsize=(10,4.5))
plt.plot(t, L, label="L(t)")
plt.scatter([t_ponto], [L_ponto], color='red')
plt.xlabel("Tempo (horas)")
plt.ylabel("Latência (ms)")
plt.title("Questão 1 - Matheus - 569559")
plt.grid(True)
plt.legend()
plt.show()

