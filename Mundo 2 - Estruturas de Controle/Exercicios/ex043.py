import random
from time import sleep

print("="*100)
print("Escolha sua jogada: ")
print("="*100)

print("""
[0] Pedra
[1] Papel
[2] Tesoura
""")

player = int(input())
pc = random.randint(0, 1)
jogadas = ["Pedra", "Papel", "Tesoura"]
print("Jô")
sleep(1)
print("Ken")
sleep(1)
print("Pó")
sleep(1)
print("="*40)
if player == pc:
    print("Empate")
elif player == 0 and pc == 1 or player == 1 and pc == 2 or player == 2 and pc == 0:
    print("Vítoria do computador")
else:
    print("Vítoria do jogador")
print(f"Computador jogou {jogadas[pc]} e jogador jogou {jogadas[player]}")