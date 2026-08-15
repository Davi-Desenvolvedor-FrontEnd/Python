from random import randint
from time import sleep

def sorteio(inicio, fim, count):
    print("-="*50)
    maior = 0
    sleep(1)
    for k in range(0, count):
        sleep(1)
        n = randint(inicio, fim)
        print(n, end=" ")
        if i == 0 or n > maior:
            maior = n
    print(f"Ao todo foram informados {count} valores, \no maior entre eles é {maior}")


while True:
    c = int(input("Quantos valores serão sorteados? "))
    if c == 0:
        break
    print("Intervalo de ", end="")
    i = int(input())
    f = int(input("até "))
    sorteio(i, f, c)
    while True:
        continuar = str(input("Continuar? [S/N] ")).upper()
        if continuar in "SN":
            break
    if continuar == "N":
        break
print("Fim do Programa")