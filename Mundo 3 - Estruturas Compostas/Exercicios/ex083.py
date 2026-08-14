matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
som = somTerCol = maiorSegLin = 0

for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f"Digite o valor para [{i}][{j}]: "))
        matriz[i][j] = n
        if n % 2 == 0:
            som += n
        if i == 1:
            if j == 0 or n > maiorSegLin:
                maiorSegLin = n
    somTerCol += matriz[i][2]

for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{matriz[i][j]:^5}]", end="")
    print()

print(f"A soma dos valores pares da matriz é: {som}")
print(f"A soma dos valores da terceira coluna é: {somTerCol}")
print(f"O maior valor da segundo linha é: {maiorSegLin}")