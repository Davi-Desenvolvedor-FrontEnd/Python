sair = False

while not sair:
    print(""" Escolha uma opção abaixo:
              [1] soma
              [2] subtrair
              [3] multiplicar
              [4] maior
              [5] sair""")
    opcao = int(input().strip())
    while opcao < 1 or opcao > 5:
        print("Opção invalida")
        print("""Escolha uma opção abaixo:
                 [1] soma
                 [2] subtrair
                 [3] multiplicar
                 [4] maior
                 [5] sair
        """)
        opcao = int(input().strip())
    if opcao == 5:
        sair = True
    else:
        n1 = float(input("Digite seu primeiro valor: ").strip())
        n2 = float(input("Digite seu segundo valor: ").strip())
        if opcao == 1:
            print(f"{n1} + {n2} = {n1 + n2}")
        elif opcao == 2:
            print(f"{n1} - {n2} = {n1 - n2}")
        elif opcao == 3:
            print(f"{n1} x {n2} = {n1 * n2}")
        else:
            if n1 > n2:
                print(f"{n1} é maior que {n2}")
            elif n1 < n2:
                print(f"{n1} é menor que {n2}")
            else:
                print(f"{n1} e {n2} são iguais")
