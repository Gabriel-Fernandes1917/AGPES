from cromossomo import funCromossomo
from creatDataset import players
import pandas as pd



def check_budget(cromossomo, orcamento):
    return sum(player['S'] for player in cromossomo) <= orcamento

def generate_population(players, tamanhoPopulacao):
    populacao = []
    for _ in range(tamanhoPopulacao):
        chromosome = funCromossomo(players)
        if check_budget(chromosome, orcamento) == True:
            populacao.append(chromosome)
    return populacao


tamanhoPopulacao = 3
orcamento = 2300000
populacao = generate_population(players, tamanhoPopulacao)
# print(populacao)
pd.DataFrame(populacao)