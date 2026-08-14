# expressao = str(input("Digite sua expressão: "))
# count = 0
# for i in range(0, len(expressao)):
#     if expressao[i] == "(" or expressao[i] == ")":
#         count += 1
#
# if count % 2 != 0 or expressao.index(")") < expressao.index("("):
#     print("Expressão inválida")
# else:
#     print("Expressão válida")

expressao = str(input("Digite sua expressão: "))
pilha = []

for e in expressao:
    if e == "(":
        pilha.append(e)
    elif e == ")":
        if len(pilha) > 0 and pilha[len(pilha) - 1] == "(":
            pilha.append(e)

if len(pilha) % 2 == 0:
    print("Expressão válida")
else:
    print("Expressão invalida")