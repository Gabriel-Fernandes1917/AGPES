import random

players =[{'serial': 0,
         'name': 'João Silva',
         'skills': {
             'AttackAttributelist': 85,
             'DefendAttributelist': 70,
             'GKAttributelist': 0
         },
         'Po': 28,
         'S': 200000},
        {'serial': 0,
         'name': 'Carlos Mendes',
         'skills': {
             'AttackAttributelist': 78,
             'DefendAttributelist': 80,
             'GKAttributelist': 0
         },
         'Po': 26,
         'S': 180000},
        {'serial': 0,
         'name': 'Pedro Lima',
         'skills': {
             'AttackAttributelist': 90,
             'DefendAttributelist': 65,
             'GKAttributelist': 0
         },
         'Po': 29,
         'S': 220000},
        {'serial': 0,
         'name': 'Rafael Costa',
         'skills': {
             'AttackAttributelist': 70,
             'DefendAttributelist': 88,
             'GKAttributelist': 0
         },
         'Po': 27,
         'S': 190000},
        {'serial': 0,
         'name': 'Fernando Souza',
         'skills': {
             'AttackAttributelist': 0,
             'DefendAttributelist': 0,
             'GKAttributelist': 85
         },
         'Po': 30,
         'S': 150000},
        {'serial': 0,
         'name': 'Luiz Pereira',
         'skills': {
             'AttackAttributelist': 80,
             'DefendAttributelist': 70,
             'GKAttributelist': 0
         },
         'Po': 27,
         'S': 185000},
        {'serial': 0,
         'name': 'Vitor Gomes',
         'skills': {
             'AttackAttributelist': 82,
             'DefendAttributelist': 74,
             'GKAttributelist': 0
         },
         'Po': 25,
         'S': 200000},
        {'serial': 0,
         'name': 'Eduardo Machado',
         'skills': {
             'AttackAttributelist': 78,
             'DefendAttributelist': 72,
             'GKAttributelist': 0
         },
         'Po': 26,
         'S': 175000},
        {'serial': 0,
         'name': 'Renato Carvalho',
         'skills': {
             'AttackAttributelist': 76,
             'DefendAttributelist': 79,
             'GKAttributelist': 0
         },
         'Po': 28,
         'S': 190000},
        {'serial': 0,
         'name': 'Marcelo Andrade',
         'skills': {
             'AttackAttributelist': 85,
             'DefendAttributelist': 67,
             'GKAttributelist': 0
         },
         'Po': 29,
         'S': 210000},
        {'serial': 0,
         'name': 'Fábio Nunes',
         'skills': {
             'AttackAttributelist': 81,
             'DefendAttributelist': 73,
             'GKAttributelist': 0
         },
         'Po': 27,
         'S': 195000},
        {'serial': 0,
         'name': 'Lucas Fernandes',
         'skills': {
             'AttackAttributelist': 82,
             'DefendAttributelist': 75,
             'GKAttributelist': 0
         },
         'Po': 27,
         'S': 210000},
        {'serial': 0,
         'name': 'Thiago Martins',
         'skills': {
             'AttackAttributelist': 80,
             'DefendAttributelist': 78,
             'GKAttributelist': 0
         },
         'Po': 25,
         'S': 190000},
        {'serial': 0,
         'name': 'Gabriel Almeida',
         'skills': {
             'AttackAttributelist': 88,
             'DefendAttributelist': 70,
             'GKAttributelist': 0
         },
         'Po': 28,
         'S': 230000},
        {'serial': 0,
         'name': 'André Ribeiro',
         'skills': {
             'AttackAttributelist': 75,
             'DefendAttributelist': 85,
             'GKAttributelist': 0
         },
         'Po': 27,
         'S': 200000},
        {'serial': 0,
         'name': 'Diego Santana',
         'skills': {
             'AttackAttributelist': 0,
             'DefendAttributelist': 0,
             'GKAttributelist': 88
         },
         'Po': 29,
         'S': 160000},
        {'serial': 0,
         'name': 'Bruno Costa',
         'skills': {
             'AttackAttributelist': 79,
             'DefendAttributelist': 77,
             'GKAttributelist': 0
         },
         'Po': 26,
         'S': 180000},
        {'serial': 0,
         'name': 'Roberto Dias',
         'skills': {
             'AttackAttributelist': 84,
             'DefendAttributelist': 72,
             'GKAttributelist': 0
         },
         'Po': 27,
         'S': 205000},
        {'serial': 0,
         'name': 'Maurício Lopes',
         'skills': {
             'AttackAttributelist': 81,
             'DefendAttributelist': 74,
             'GKAttributelist': 0
         },
         'Po': 26,
         'S': 190000},
        {'serial': 0,
         'name': 'Henrique Moreira',
         'skills': {
             'AttackAttributelist': 77,
             'DefendAttributelist': 80,
             'GKAttributelist': 0
         },
         'Po': 28,
         'S': 200000},
        {'serial': 0,
         'name': 'Leonardo Pinto',
         'skills': {
             'AttackAttributelist': 83,
             'DefendAttributelist': 73,
             'GKAttributelist': 0
         },
         'Po': 29,
         'S': 210000},
        {'serial': 0,
         'name': 'Alex Teixeira',
         'skills': {
             'AttackAttributelist': 80,
             'DefendAttributelist': 75,
             'GKAttributelist': 0
         },
         'Po': 27,
         'S': 195000},
        {'serial': 0,
         'name': 'Ricardo Rocha',
         'skills': {
             'AttackAttributelist': 83,
             'DefendAttributelist': 74,
             'GKAttributelist': 0
         },
         'Po': 27,
         'S': 215000},
        {'serial': 0,
         'name': 'Felipe Araújo',
         'skills': {
             'AttackAttributelist': 79,
             'DefendAttributelist': 77,
             'GKAttributelist': 0
         },
         'Po': 26,
         'S': 185000},
        {'serial': 0,
         'name': 'Bruno Oliveira',
         'skills': {
             'AttackAttributelist': 87,
             'DefendAttributelist': 68,
             'GKAttributelist': 0
         },
         'Po': 28,
         'S': 225000},
        {'serial': 0,
         'name': 'Marcos Lima',
         'skills': {
             'AttackAttributelist': 73,
             'DefendAttributelist': 86,
             'GKAttributelist': 0
         },
         'Po': 27,
         'S': 195000},
        {'serial': 0,
         'name': 'Igor Santos',
         'skills': {
             'AttackAttributelist': 0,
             'DefendAttributelist': 0,
             'GKAttributelist': 87
         },
         'Po': 30,
         'S': 155000},
        {'serial': 0,
         'name': 'Paulo Henrique',
         'skills': {
             'AttackAttributelist': 81,
             'DefendAttributelist': 76,
             'GKAttributelist': 0
         },
         'Po': 26,
         'S': 190000},
        {'serial': 0,
         'name': 'Rodrigo Lima',
         'skills': {
             'AttackAttributelist': 84,
             'DefendAttributelist': 73,
             'GKAttributelist': 0
         },
         'Po': 27,
         'S': 205000},
        {'serial': 0,
         'name': 'Gustavo Silva',
         'skills': {
             'AttackAttributelist': 79,
             'DefendAttributelist': 75,
             'GKAttributelist': 0
         },
         'Po': 25,
         'S': 180000},
        {'serial': 0,
         'name': 'Matheus Nascimento',
         'skills': {
             'AttackAttributelist': 82,
             'DefendAttributelist': 78,
             'GKAttributelist': 0
         },
         'Po': 27,
         'S': 200000},
        {'serial': 0,
         'name': 'Sérgio Ramos',
         'skills': {
             'AttackAttributelist': 85,
             'DefendAttributelist': 70,
             'GKAttributelist': 0
         },
         'Po': 28,
         'S': 215000},
        {'serial': 0,
         'name': 'Alexandre Souza',
         'skills': {
             'AttackAttributelist': 80,
             'DefendAttributelist': 75,
             'GKAttributelist': 0
         },
         'Po': 27,
         'S': 195000}]

players

for i in players:
        print(i)