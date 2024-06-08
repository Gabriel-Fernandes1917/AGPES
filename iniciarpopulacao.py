from cromossomo import funCromossomo
from creatDataset import players
import pandas as pd



def check_budget(cromossomo, orcamento):
    return sum(player['S'] for player in cromossomo) <= orcamento

def generate_population(players, tamanhoPopulacao, orcamento):
    populacao = []
    for _ in range(tamanhoPopulacao):
        chromosome = funCromossomo(players)
        if check_budget(chromosome, orcamento) == True:
            populacao.append(chromosome)
    return populacao


tamanhoPopulacao = 3
orcamento = 2900000
populacao = generate_population(players, tamanhoPopulacao,orcamento)

# for i in populacao:
#     for x in i:
#       totalCost = sum(x["S"])



# print(populacao)
pd.DataFrame(populacao)

