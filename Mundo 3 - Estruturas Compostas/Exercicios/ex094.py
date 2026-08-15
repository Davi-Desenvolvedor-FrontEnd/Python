from time import sleep

def contagem(inicio, fim, passo):
    print("=" * 30)
    sleep(1)
    print(f"Contagem de {inicio} até {fim}, de {passo} em {passo}")
    if inicio > fim:
        passo *= -1
        fim -= 1
    else:
        fim += 1
    for k in range(inicio, fim, passo):
        print(k, end=" ")
        sleep(0.5)
    print("\n")

# contagem(1, 10, 1)
# contagem(10, 1, 1)

print("Sua vez!")
while True:
    i = int(input("Início: "))
    f = int(input("Fim: "))
    while True:
        p = int(input("Passo: "))
        if p > 0:
            break
    contagem(i, f, p)
    while True:
        continuar = str(input("Continuar? [S/N] "))
        if continuar.upper() in "SN":
            break
    if continuar.upper() == "N":
        break