sair = False
count = 0
soma = 0
while not sair:
    n = int(input("Digite um número: "))
    if n == 999:
        sair = True
    else:
        soma += n
        count += 1

print(f"{count} valores digitados, \na soma entre eles é {soma}")