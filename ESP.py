import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from iniciarpopulacao import generate_population
from creatDataset import players

# Função para calcular CVa e CVb
def calcular_cva(time):
    return max(0, (sum(jogador['S'] for jogador in time) - 2900000) / 2900000)  # 2900000 é nosso orçamento

def calcular_cvb(time):
    return max(0, (sum(jogador['S'] for jogador in time) - 2900000) / 2900000)  # 2900000 é nosso orçamento

# Função para classificar a população com base na dominância de Pareto
def classificar_pareto(populacao):
    frente_pareto = []
    dominancia = []

    for i in range(len(populacao)):
        dominado = False
        dominantes = []
        for j in range(len(populacao)):
            if i != j:
                cvai, cvbi = calcular_cva(populacao[i]), calcular_cvb(populacao[i])
                cvaj, cvbj = calcular_cva(populacao[j]), calcular_cvb(populacao[j])
                if cvai == 0 and cvbi > 0:
                    dominado = True
                    dominantes.append(j)
                elif cvai > 0 and cvbi == 0:
                    continue
                elif cvai > 0 and cvbi > 0 and (cvai < cvaj and cvbi < cvbj):
                    dominado = True
                    dominantes.append(j)
                elif cvai == 0 and cvbi == 0:
                    if cvaj == 0 and cvbj == 0:
                        continue
                    elif cvaj == 0 and cvbj > 0:
                        continue
                    else:
                        dominado = True
                        dominantes.append(j)
        if not dominado:
            frente_pareto.append(i)
        dominancia.append(dominantes)
    return frente_pareto

# Função para cruzamento
def cruzamento(pai1, pai2, pc):
    if random.random() < pc:
        filho = [pai1[0]]
        resto_pai1 = sorted(pai1[1:], key=lambda x: -x['S'])
        resto_pai2 = sorted(pai2[1:], key=lambda x: -x['S'])
        
        for i in range(1, len(pai1)):
            if i % 2 == 0:
                filho.append(resto_pai1.pop(0))
            else:
                filho.append(resto_pai2.pop(0))
                
        return filho
    else:
        return random.choice([pai1, pai2])

# Função para mutação polinomial
def mutacao_polinomial(individuo, pm, eta_m):
    if random.random() < pm:
        for i in range(1, len(individuo)):  # Não muta o goleiro na primeira posição
            if random.random() < pm:
                delta = random.uniform(-1, 1)
                mutacao = (1.0 - abs(delta)) ** (1.0 / (1.0 + eta_m))
                individuo[i]['S'] = individuo[i]['S'] * (1 + delta * mutacao)
                # Garantir que o valor da mutação não seja negativo
                if individuo[i]['S'] < 0:
                    individuo[i]['S'] = 0
    return individuo

# Função para selecionar a próxima geração
def selecionar_proxima_geracao(populacao, frente_pareto, pc, pm, eta_m):
    nova_populacao = [populacao[i] for i in frente_pareto]
    while len(nova_populacao) < len(populacao):
        pai1, pai2 = random.sample(nova_populacao, 2)
        filho = cruzamento(pai1, pai2, pc)
        filho = mutacao_polinomial(filho, pm, eta_m)
        nova_populacao.append(filho)
    return nova_populacao

# Função para calcular habilidades de ataque e defesa
def habilidades(time):
    attack = sum(jogador['skills']['AttackAttributelist'] for jogador in time)
    defense = sum(jogador['skills']['DefendAttributelist'] for jogador in time)
    return attack, defense

# Parâmetros do algoritmo
tamanho_populacao = 400
numero_geracoes = 300
pc = 0.5  # Probabilidade de cruzamento
pm = 0.1  # Probabilidade de mutação
eta_m = 30  # Parâmetro de mutação polinomial

# Inicialização da população
populacao = generate_population(players, tamanho_populacao, 2900000)

# Execução do algoritmo
for geracao in range(numero_geracoes):
    frente_pareto = classificar_pareto(populacao)
    populacao = selecionar_proxima_geracao(populacao, frente_pareto, pc, pm, eta_m)

# Plotar a frente de Pareto
plt.figure(figsize=(10, 6))

# Plotar todos os times
for i, time in enumerate(populacao):
    attack, defense = habilidades(time)
    if i in frente_pareto:
        plt.scatter(attack, defense, color='blue', label='Pareto Front' if i == frente_pareto[0] else "")  # Times na frente de Pareto em vermelho
    else:
        plt.scatter(attack, defense, color='blue', label='Others' if i == 0 else "")  # Demais times em azul

plt.xlabel('Habilidade de Ataque')
plt.ylabel('Habilidade de Defesa')
plt.title('Frente de Pareto')
plt.legend()
plt.show()

# Resultados finais
melhor_time = populacao[0]
print(f'Melhor time: {melhor_time}')
pd.DataFrame(melhor_time)
