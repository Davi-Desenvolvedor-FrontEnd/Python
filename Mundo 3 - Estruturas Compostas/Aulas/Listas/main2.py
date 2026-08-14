# matriz = [
#     [1, 0, 0],
#     [0, 1, 0],
#     [0, 0, 1],
# ]
#
# for i in range(0, len(matriz)):
#     for j in range(0, len(matriz[i])):
#         print(matriz[i][j])

A = [
    [1, 2],
    [3, 4]
]

dP = 0
dS = 0

for i in range(0, len(A)):
    for j in range(0, len(A[i])):
        if i == j:
            if dP == 0:
                dP = A[i][j]
            else:
                dP *= A[i][j]
        else:
            if dS == 0:
                dS = A[i][j]
            else:
                dS *= A[i][j]

print(f"A matriz A, possui o determinante igual à: {dP-dS}")