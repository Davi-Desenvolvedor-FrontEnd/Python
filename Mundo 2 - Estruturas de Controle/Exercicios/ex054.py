media = 0
maisVelhoInt = 0
maisVelhoNome = ""
nMulher = 0
nHomem = 0

for i in range(1, 5):
    print("="*40)
    print(f"Análise da {i}° pessoa")
    print("="*40)
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo: ")

    if idade > maisVelhoInt:
        maisVelhoInt = idade
        maisVelhoNome = nome
    if sexo.upper() == "M":
        nHomem+=1
    else:
        nMulher+=1
    media += idade

media = media/4

print(f"A pessoa mais velha do grupo é {maisVelhoNome} e tem {maisVelhoInt} anos de idade \na média das idades é {media:.1f} anos \ne ao todo tempos {nHomem} homens e {nMulher} mulheres")