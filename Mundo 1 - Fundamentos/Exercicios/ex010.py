preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o valor do desconto (em %): "))
precoFinal = preco * (1 - (desconto/100))
print(f"O produto que custava R$ {preco} com o desconto de {desconto}%, agora custa R ${precoFinal:.2f}")