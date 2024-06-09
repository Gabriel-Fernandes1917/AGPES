import matplotlib.pyplot as plt
from creatDataset import players

def calculate_total_skills(skills):
    return sum(skills.values())

# Listas para armazenar os dados do gráfico
performance = []
salary = []
names = []

# Preenchendo as listas
for player in players:
    total_skills = calculate_total_skills(player['skills'])
    performance.append(total_skills)
    salary.append(player['S'])
    names.append(player['name'])

# Plotando o gráfico
plt.figure(figsize=(10, 6))
plt.scatter(performance, salary)

# Adicionando os rótulos
for i, name in enumerate(names):
    plt.annotate(name, (performance[i], salary[i]), fontsize=9, alpha=0.7)

plt.title('Desempenho vs Salário dos Jogadores')
plt.xlabel('Desempenho (Soma das Habilidades)')
plt.ylabel('Salário')
plt.grid(True)
plt.show()