import random
from creatDataset import players
import pandas as pd

# Função para verificar se o jogador é um goleiro
def get_GK(player):
    return player['skills']['AttackAttributelist'] == 0

# Função para verificar se o jogador é um defensor
def playerPositionDef(player):
    return (player['skills']['DefendAttributelist'] - player['skills']['AttackAttributelist'] > 10) and not get_GK(player)

# Função para verificar se o jogador é um atacante
def playerPositionAtk(player):
    return (player['skills']['AttackAttributelist'] - player['skills']['DefendAttributelist'] > 10) and not get_GK(player)

# Função para verificar se o jogador é um meio-campista
def playerPositionMid(player):
    return abs(player['skills']['DefendAttributelist'] - player['skills']['AttackAttributelist']) <= 10 and not get_GK(player)

# Função para formar o time
def funCromossomo(players):
    cromossomo = []

    # Embaralhar os jogadores
    random.shuffle(players)

    gk = [player for player in players if get_GK(player)]
    defenders = [player for player in players if playerPositionDef(player)]
    attackers = [player for player in players if playerPositionAtk(player)]
    midfielders = [player for player in players if playerPositionMid(player)]

    if len(gk) < 1 or len(defenders) < 3 or len(attackers) < 3:
        # print("Não há jogadores suficientes para formar o time com as posições necessárias.")
        return []

    # Adicionar 1 goleiro
    cromossomo.append(gk[0])
    gk.pop(0)

    # Adicionar 3 defensores
    cromossomo.extend(defenders[:3])
    defenders = defenders[3:]

    # Adicionar 3 atacantes
    cromossomo.extend(attackers[:3])
    attackers = attackers[3:]

    # Adicionar o restante como meio-campistas até completar 12 jogadores
    while len(cromossomo) < 11:
        if midfielders:
            cromossomo.append(midfielders.pop(0))
        elif defenders:
            cromossomo.append(defenders.pop(0))
        elif attackers:
            cromossomo.append(attackers.pop(0))
        elif gk:
            cromossomo.append(gk.pop(0))
        else:
            break

    return cromossomo
# Exemplo de uso

time = funCromossomo(players)
# print(time)
pd.DataFrame(time)
