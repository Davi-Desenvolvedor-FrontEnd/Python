from operator import itemgetter
from random import randint
from time import sleep
print("Valores sorteados: ")

print("-="*40)
jogos = {}
for i in range(1, 5):
     sleep(1)
     jogos[f"jogador {i}"] = randint(1, 6)
     print(f"Jogador {i} jogou os dados e caiu: {jogos[f'jogador {i}']}")
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print("-="*40)

for i, r in enumerate(ranking):
    print(f"{i+1}° Lugar: {r[0]} com {r[1]}.")
print("-="*40)