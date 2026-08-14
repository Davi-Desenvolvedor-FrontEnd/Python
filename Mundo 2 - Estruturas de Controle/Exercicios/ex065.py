from random import randint

vitoria = True
count = 0
while vitoria:
    print("="*50)
    tipo = " "
    while tipo.upper() not in "PI":
        tipo = str(input("Par ou Ímpar [P/I]: "))
    jogador = int(input("Digite um número: "))
    computador = randint(1, 10)
    n = jogador + computador
    print(f"{jogador} + {computador} = {n}")
    if tipo.upper() == "P":
        if n % 2 == 0:
            count += 1
            print("Vítoria do Jogador")
        else:
            vitoria = False
            print("Vítoria do PC")
    else:
        if n % 2 == 0:
            vitoria = False
            print("Vítoria do PC")
        else:
            count += 1
            print("Vítoria do Jogador")

print(f"Obrigado por jogar! O jogador teve {count} vítorias")