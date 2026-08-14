import random

print("Adivinhe o número que escolhi no intervalor de 0 a 5")
num = int(input())
numAleatorio = random.randint(0, 6)

if num == numAleatorio:
    print("Você acertou!", "👏"*200)
else:
    print("k"*100)
    print(f"Eu escolhi {numAleatorio}")
