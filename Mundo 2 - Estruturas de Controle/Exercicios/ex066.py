maiores = nHomens = count = 0

while True:
    print("-"*30)
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).upper()
    if idade >= 18:
        maiores += 1
    if sexo == "M":
        nHomens += 1
    count += 1
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Deseja continuar? [S/N] ")).upper()
    if continuar == "N":
        break

nMulheres = count-nHomens
print(f"Ao total: \nforam cadastradas {count} pessoas \n{maiores} são maior de idade \n{nHomens} são homens \ne {nMulheres} são mulheres")