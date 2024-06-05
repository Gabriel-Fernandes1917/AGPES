import random

players = [
    {'serial': 0,
     'name': 'João Silva',
     'skills': {
         'AttackAttributelist': 85,
         'DefendAttributelist': 70,
         'GKAttributelist': 0
     },
     'Po': 93,
     'S': 200000,
     'overall': 88},

    {'serial': 0,
     'name': 'Carlos Mendes',
     'skills': {
         'AttackAttributelist': 0,
         'DefendAttributelist': 0,
         'GKAttributelist': 90
     },
     'Po': 85,
     'S': 100000,
     'overall': 80},

    {'serial': 0,
     'name': 'Pedro Alves',
     'skills': {
         'AttackAttributelist': 88,
         'DefendAttributelist': 60,
         'GKAttributelist': 0
     },
     'Po': 85,
     'S': 300000,
     'overall': 86},

    {'serial': 0,
     'name': 'Ricardo Costa',
     'skills': {
         'AttackAttributelist': 70,
         'DefendAttributelist': 75,
         'GKAttributelist': 0
     },
     'Po': 80,
     'S': 120000,
     'overall': 78},

    {'serial': 0,
     'name': 'André Souza',
     'skills': {
         'AttackAttributelist': 65,
         'DefendAttributelist': 80,
         'GKAttributelist': 0
     },
     'Po': 75,
     'S': 100000,
     'overall': 76},

    {'serial': 0,
     'name': 'Lucas Fernandes',
     'skills': {
         'AttackAttributelist': 90,
         'DefendAttributelist': 68,
         'GKAttributelist': 0
     },
     'Po': 92,
     'S': 320000,
     'overall': 87},

    {'serial': 0,
     'name': 'Rafael Lima',
     'skills': {
         'AttackAttributelist': 77,
         'DefendAttributelist': 72,
         'GKAttributelist': 0
     },
     'Po': 88,
     'S': 250000,
     'overall': 83},

    {'serial': 0,
     'name': 'Marcelo Oliveira',
     'skills': {
         'AttackAttributelist': 82,
         'DefendAttributelist': 77,
         'GKAttributelist': 0
     },
     'Po': 90,
     'S': 270000,
     'overall': 85},

    {'serial': 0,
     'name': 'Felipe Santos',
     'skills': {
         'AttackAttributelist': 67,
         'DefendAttributelist': 85,
         'GKAttributelist': 0
     },
     'Po': 80,
     'S': 180000,
     'overall': 79},

    {'serial': 0,
     'name': 'Gustavo Ribeiro',
     'skills': {
         'AttackAttributelist': 72,
         'DefendAttributelist': 60,
         'GKAttributelist': 0
     },
     'Po': 70,
     'S': 90000,
     'overall': 73},

    {'serial': 0,
     'name': 'Eduardo Lima',
     'skills': {
         'AttackAttributelist': 85,
         'DefendAttributelist': 75,
         'GKAttributelist': 0
     },
     'Po': 92,
     'S': 310000,
     'overall': 88},

    {'serial': 0,
     'name': 'Thiago Pereira',
     'skills': {
         'AttackAttributelist': 78,
         'DefendAttributelist': 65,
         'GKAttributelist': 0
     },
     'Po': 85,
     'S': 200000,
     'overall': 81},

    {'serial': 0,
     'name': 'Leandro Ferreira',
     'skills': {
         'AttackAttributelist': 68,
         'DefendAttributelist': 70,
         'GKAttributelist': 0
     },
     'Po': 75,
     'S': 110000,
     'overall': 74},

    {'serial': 0,
     'name': 'Bruno Rocha',
     'skills': {
         'AttackAttributelist': 88,
         'DefendAttributelist': 80,
         'GKAttributelist': 0
     },
     'Po': 95,
     'S': 400000,
     'overall': 89},

    {'serial': 0,
     'name': 'Alexandre Nunes',
     'skills': {
         'AttackAttributelist': 77,
         'DefendAttributelist': 73,
         'GKAttributelist': 0
     },
     'Po': 88,
     'S': 220000,
     'overall': 84},

    {'serial': 0,
     'name': 'Fernando Dias',
     'skills': {
         'AttackAttributelist': 65,
         'DefendAttributelist': 80,
         'GKAttributelist': 0
     },
     'Po': 78,
     'S': 120000,
     'overall': 77},

    {'serial': 0,
     'name': 'Sergio Martins',
     'skills': {
         'AttackAttributelist': 75,
         'DefendAttributelist': 85,
         'GKAttributelist': 0
     },
     'Po': 92,
     'S': 330000,
     'overall': 87},

    {'serial': 0,
     'name': 'Diego Costa',
     'skills': {
         'AttackAttributelist': 90,
         'DefendAttributelist': 70,
         'GKAttributelist': 0
     },
     'Po': 93,
     'S': 350000,
     'overall': 89},

    {'serial': 0,
     'name': 'Vitor Oliveira',
     'skills': {
         'AttackAttributelist': 78,
         'DefendAttributelist': 68,
         'GKAttributelist': 0
     },
     'Po': 85,
     'S': 190000,
     'overall': 82},

    {'serial': 0,
     'name': 'Ramon Silva',
     'skills': {
         'AttackAttributelist': 65,
         'DefendAttributelist': 75,
         'GKAttributelist': 0
     },
     'Po': 75,
     'S': 100000,
     'overall': 75},

    {'serial': 0,
     'name': 'Mauricio Santos',
     'skills': {
         'AttackAttributelist': 85,
         'DefendAttributelist': 65,
         'GKAttributelist': 0
     },
     'Po': 90,
     'S': 270000,
     'overall': 86},

    {'serial': 0,
     'name': 'Rogério Lima',
     'skills': {
         'AttackAttributelist': 77,
         'DefendAttributelist': 70,
         'GKAttributelist': 0
     },
     'Po': 85,
     'S': 180000,
     'overall': 81},

    {'serial': 0,
     'name': 'Adriano Vieira',
     'skills': {
         'AttackAttributelist': 80,
         'DefendAttributelist': 75,
         'GKAttributelist': 0
     },
     'Po': 87,
     'S': 260000,
     'overall': 84},

    {'serial': 0,
     'name': 'Henrique Souza',
     'skills': {
         'AttackAttributelist': 72,
         'DefendAttributelist': 65,
         'GKAttributelist': 0
     },
     'Po': 82,
     'S': 190000,
     'overall': 80},

    {'serial': 0,
     'name': 'Guilherme Alves',
     'skills': {
         'AttackAttributelist': 85,
         'DefendAttributelist': 70,
         'GKAttributelist': 0
     },
     'Po': 90,
     'S': 280000,
     'overall': 86},

    {'serial': 0,
     'name': 'Matheus Mendes',
     'skills': {
         'AttackAttributelist': 0,
         'DefendAttributelist': 0,
         'GKAttributelist': 92
     },
     'Po': 88,
     'S': 130000,
     'overall': 82},

    {'serial': 0,
     'name': 'Paulo Silva',
     'skills': {
         'AttackAttributelist': 70,
         'DefendAttributelist': 60,
         'GKAttributelist': 0
     },
     'Po': 75,
     'S': 90000,
     'overall': 73},

    {'serial': 0,
     'name': 'Arthur Santos',
     'skills': {
         'AttackAttributelist': 78,
         'DefendAttributelist': 68,
         'GKAttributelist': 0
     },
     'Po': 82,
     'S': 190000,
     'overall': 81},

    {'serial': 0,
     'name': 'Daniel Ribeiro',
     'skills': {
         'AttackAttributelist': 65,
         'DefendAttributelist': 80,
         'GKAttributelist': 0
     },
     'Po': 75,
     'S': 110000,
     'overall': 76},

    {'serial': 0,
     'name': 'Julio Oliveira',
     'skills': {
         'AttackAttributelist': 85,
         'DefendAttributelist': 75,
         'GKAttributelist': 0
     },
     'Po': 92,
     'S': 300000,
     'overall': 88},

    {'serial': 0,
     'name': 'Leonardo Lima',
     'skills': {
         'AttackAttributelist': 88,
         'DefendAttributelist': 60,
         'GKAttributelist': 0
     },
     'Po': 85,
     'S': 320000,
     'overall': 87},

    {'serial': 0,
     'name': 'Luiz Costa',
     'skills': {
         'AttackAttributelist': 0,
         'DefendAttributelist': 0,
         'GKAttributelist': 95
     },
     'Po': 90,
     'S': 150000,
     'overall': 85},

    {'serial': 0,
     'name': 'Rafael Nunes',
     'skills': {
         'AttackAttributelist': 75,
         'DefendAttributelist': 70,
         'GKAttributelist': 0
     },
     'Po': 82,
     'S': 190000,
     'overall': 80},
]



players

for i in players:
        print(i)