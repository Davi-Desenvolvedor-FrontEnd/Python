pessoas = []
maisPesadas = []
maisLeves = []

print("-="*20)
while True:
    nome = str(input("Digite um nome: "))
    peso = int(input("Digite um peso: "))
    pessoa = [nome, peso]
    pessoas.append(pessoa)
    continuar = input("Deseja continuar? [S/N] ")
    if continuar in "Nn":
        break

for pessoa in pessoas:
    peso = pessoa[1]
    if len(maisPesadas) == 0 and len(maisLeves) == 0:
        maisPesadas.append(pessoa)
        maisLeves.append(pessoa)
        continue
    else:
        for P in maisPesadas:
            if peso > P[1]:
                maisPesadas.clear()
                maisPesadas.append(pessoa)
            elif peso == P[1]:
                maisPesadas.append(pessoa)
            break
        for L in maisLeves:
            if peso < L[1]:
                maisLeves.clear()
                maisLeves.append(pessoa)
            elif peso == L[1]:
                maisLeves.append(pessoa)
            break

print("-="*20)
print(pessoas)
print("-="*20)
print(f"Foram registradas {len(pessoas)} pessoas")
print(f"Mais pesadas: {maisPesadas}")
print(f"Mais leves: {maisLeves}")

