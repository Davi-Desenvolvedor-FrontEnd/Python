maisBaratoNome = ""
maisBaratoNum = total = maisMil = count = 0 
while True:
    nome = input("Nome do produto: ")
    preco = float(input(f"Preço do {nome}: R$ "))
    total += preco
    count += 1
    if count == 0 or preco < maisBaratoNum:
        maisBaratoNum = preco
        maisBaratoNome = nome
    elif preco > 1000:
        maisMil += 1
    continuar = str(input("Quer continuar? [S/N] ")).upper()
    print("-"*40)
    if continuar == "N":
        break

print(f"O total da compra foi de R${total:.2f} \n{maisMil} {"produtos custaram" if maisMil > 1 else "produto custou"} mais de R$ 1000.00 \ne o produto mais barato foi {maisBaratoNome.lower()} que custou R$ {maisBaratoNum:.2f}")