import random
from creatDataset import players


def get_GK(dataplayers):
    if dataplayers['skills']['AttackAttributelist'] == 0:
        return True
    else: 
        return False

# for i in teams:
#     for x in i:
#         for p in x:
#            print(p['skills']['AttackAttributelist'])
#            if p['skills']['AttackAttributelist'] == 0:
#                GK_tag = p['name']
#            else:
#                 player_tag = p['name']
               
def cromossomo():
    cromossomo = []
    while len(cromossomo) < 12:
       nAle = random.randint(0, len(players))
       while get_GK(players[nAle]) == False:
           cromossomo()
        
        cromossomo.append(players[nAle])
           
        #botar um while pra ficar tentanto até dar 1 goleiro


def constraintViolation(data,var_vector,budget):
    index = [i for i in var_vector]
    totalCost = data.iloc[index]['value_eur'].sum()/10000
    CV = max(0,(totalCost-budget)/budget)
    return CV

def gerarPopulação():
    
    while < 12