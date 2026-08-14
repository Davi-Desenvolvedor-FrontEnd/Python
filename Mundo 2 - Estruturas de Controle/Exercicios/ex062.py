fim = False
maior = 0
menor = 0
soma = 0

while not fim:
    n = int(input("Quantos números quer digitar? "))
    for i in range(1, n+1):
        num = int(input(f"{i}° número: "))
        if i == 1:
            maior = num
            menor = num
        else:
            if num > maior:
                maior = num
            elif num < menor:
                menor = num
        soma += num

    print(f"A média dos {n} números digitados foi {(soma/n):.1f}, \no maior entre eles é {maior} e o menor foi {menor}")
    continuar = input("Continuar? [S/N] ")
    if continuar == "N":
        fim = True
    else:
        n = 0
        maior = 0
        menor = 0
        soma = 0