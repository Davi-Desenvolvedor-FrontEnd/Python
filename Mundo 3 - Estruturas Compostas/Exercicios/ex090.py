pessoas = []
mediaIdade = mediaPeso = 0

while True:
    pessoa = dict()
    pessoa["nome"] = str(input("Nome: "))
    pessoa["idade"] = int(input("Idade: "))
    pessoa["peso"] = float(input("Peso: "))
    pessoa["sexo"] = str(input("Sexo [M/F]: ")).upper()
    while pessoa["sexo"] not in "MF":
        pessoa["sexo"] = str(input("Opção ínvalida! Sexo [M/F]: ")).upper()
    pessoas.append(pessoa)
    mediaIdade += pessoa["idade"]
    mediaPeso += pessoa["peso"]
    continuar = str(input("Quer continuar? [S/N]: "))
    while continuar not in "SsNn":
        continuar = str(input("Quer continuar? [S/N]: "))
    if continuar in "Nn":
        break

mediaIdade = mediaIdade / len(pessoas)
mediaPeso = mediaPeso / len(pessoas)
print("-="*30)
print(f"1 - Ao todo foram cadastradas {len(pessoas)} pessoas")
print(f"2 - Á média de idade {mediaIdade:.0f} anos e a média de peso é {mediaPeso:.1f} kg")
print(f"3 - Lista das pessoas acima da média: ")

for p in pessoas:
    if p["idade"] > mediaIdade and p["peso"] > mediaPeso:
        print(f"Nome: {p['nome']}; Idade: {p["idade"]} anos; Peso: {p["peso"]} kg")
print("-="*30)