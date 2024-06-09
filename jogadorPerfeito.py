import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from creatDataset import players


salaries = [player['S'] for player in players]
potential = [player['Po'] for player in players]
overall = [player['overall'] for player in players]

# Criar figura e eixos 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Adicionar pontos ao gráfico
ax.scatter(salaries, potential, overall)

# Definir rótulos dos eixos
ax.set_xlabel('Salário (S)')
ax.set_ylabel('Potencial de Valorização (Po)')
ax.set_zlabel('Overall')

# Mostrar gráfico
plt.show()