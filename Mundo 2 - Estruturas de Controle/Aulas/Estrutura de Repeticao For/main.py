# inicio = int(input("Ínicio: "))
# fim = int(input("Fim: "))
# passo = int(input("Passo: "))
# soma = 0
# tamanho = int(((fim - inicio)/passo) + 1)
# for c in range(inicio, fim + 1, passo):
#     print(c)
#     soma+=c
#
# print(f"Na PA de a1 igual {inicio}, razão igual a {passo} e tamanho igual a {tamanho}, a soma é {soma}")

import math

primeiro_termo = int(input("Primeiro termo: "))
tamanho = int(input("Tamanho: "))
razao = int(input("Razão: "))
soma = int(primeiro_termo * ((math.pow(razao, tamanho) - 1) / (razao-1)))
for i in range(1, tamanho+1):
    print(f"{i}, {int(primeiro_termo * math.pow(razao, i-1))}")
print(f"Soma da PG finita: {soma}")