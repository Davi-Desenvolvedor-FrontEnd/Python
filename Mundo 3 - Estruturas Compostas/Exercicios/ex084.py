from random import randint
import time

nJogos = int(input("Quantos jogos quer que eu sorteie? "))
numSorteados = []

print("Sorteando....")
print("-="*40)
for i in range(1, nJogos + 1):
    count = 0
    time.sleep(1)
    while count < 6:
        n = randint(1, 60)
        if n not in numSorteados:
            numSorteados.append(n)
            count += 1
    print(f"Jogo {i}: {numSorteados}")
    numSorteados.clear()
time.sleep(1)
print("-="*20)
print("Fim do sorteio")