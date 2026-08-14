from tabulate import tabulate

alunos = []
count = 0
while True:
    nome = str(input("Nome do aluno: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    alunos.append([count, nome, [nota1, nota2], media])
    count += 1
    continuar = str(input("Quer continuar? [S/N] "))
    if continuar in "Nn":
        break

print(f"| {"Id":<10} | {"Nome":<10} | {"Média":<10}")
for i in range(0, len(alunos)):
    for j in range(0, len(alunos[i])):
        if j != 2:
            print(f"| {alunos[i][j]:<10}", end=" ")
    print()
# dados_para_mostrar = []
# for aluno in alunos:
#     dados_para_mostrar.append([
#         aluno[0],
#         aluno[1],
#         f"{aluno[3]:.1f}"  # Formata com 1 casa decimal
#     ])
#
# print(tabulate(dados_para_mostrar, headers=["Id", "Nome", "Média"], tablefmt="simple"))