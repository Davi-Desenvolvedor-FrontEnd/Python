matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f"Digite o valor para [{i}][{j}]: "))
        matriz[i][j] = n

for m in range(0, 3):
    for n in range(0, 3):
        print(f'{matriz[m][n]:>5}', end="")
    print("")