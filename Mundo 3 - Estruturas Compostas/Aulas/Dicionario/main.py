# pessoas = [
#     {
#         "nome": "Davi",
#         "sexo": "M",
#         "idade": 18
#     }
# ]
#
# for pessoa in pessoas:
#     for p in pessoa:
#         print(f"{p}: {pessoa[p]}")
#
# print(len(pessoas[0]))

users = []
user = {}
for i in range(1, 3):
    nome = input(f"Digite o nome do {i}° aluno: ")
    idade = int(input(f"Digite a idade do {i}° aluno: "))
    user = {"nome": nome, "idade": idade}
    users.append(user)

for user in users:
    for u in user:
        print(f"{u}: {user[u]}", end=" ")
    print()