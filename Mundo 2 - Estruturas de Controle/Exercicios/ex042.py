preco = float(input("Preço do produto: "))
print("Opção de pagamento: ")
print("""
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] parcelado em 2x no cartão
[4] 3x ou mais no cartão
""")
opcao = int(input())

if opcao == 1:
    valorFinal = preco * 0.9
    print(f"Valor final do produto: R${valorFinal:.2f}")
elif opcao == 2:
    valorFinal = preco * 0.95
    print(f"Valor final do produto: R${valorFinal:.2f}")
elif opcao == 3:
    parcela = preco/2
    valorFinal = preco
    print(f"Sua compra será parcelada em 2x sem juros, \no valor final do produto será de R${valorFinal:.2f}")
elif opcao == 4:
    parcelaInt = int(input("Quantas parcelas? "))
    parcela = (preco * 1.2)/ parcelaInt
    valorFinal = preco * 1.2
    print(f"Sua compra será parcelada em {parcelaInt}x de R$ {parcela:.2f} com juros, \no valor final será de R${valorFinal:.2f}")
else:
    print("Opção de pagamento invalida")

print("-=" * 20)