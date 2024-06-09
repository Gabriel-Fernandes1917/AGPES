import numpy as np
import matplotlib.pyplot as plt

# Função para verificar se uma solução domina outra
def domina(sol1, sol2):
    return all(x <= y for x, y in zip(sol1, sol2)) and any(x < y for x, y in zip(sol1, sol2))

# Gerando algumas soluções aleatórias (por exemplo, pontos no espaço 2D)
np.random.seed(42)
solucoes = np.random.rand(100, 2)

# Identificando a frente de Pareto
frente_pareto = []
for i, sol1 in enumerate(solucoes):
    is_dominated = False
    for j, sol2 in enumerate(solucoes):
        if domina(sol2, sol1):
            is_dominated = True
            break
    if not is_dominated:
        frente_pareto.append(sol1)

frente_pareto = np.array(frente_pareto)

# Plotando as soluções e a frente de Pareto
plt.figure(figsize=(10, 6))
plt.scatter(solucoes[:, 0], solucoes[:, 1], label='Soluções', alpha=0.5)
plt.scatter(frente_pareto[:, 0], frente_pareto[:, 1], color='red', label='Frente de Pareto')
plt.title('Frente de Pareto')
plt.xlabel('Objetivo 1')
plt.ylabel('Objetivo 2')
plt.legend()
plt.show()
