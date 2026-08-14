kmRodados = float(input("Digite o total de km rodados: "))
quantDias = int(input("Digite o total de dias alugados: "))
preco = (quantDias*60) + (kmRodados*0.15)

print(f"O após {quantDias} dias e {kmRodados} km rodados, o total a pagar é de R$ {preco:.2f}")