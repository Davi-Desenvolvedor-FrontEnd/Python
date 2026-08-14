# pesos = []
#
# for i in range(1, 6):
#     peso = float(input(f"Peso da {i}° pessoa: "))
#     pesos.append(peso)
#
# pesos.sort(reverse=True)
# print(f"Maior peso: {pesos[0]} \nMenor peso: {pesos[4]}")

maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input(f"Peso da {i}° pessoa: "))
    if i == 1:
        maior=peso
        menor=peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f"Maior peso: {maior} \nMenor peso: {menor}")