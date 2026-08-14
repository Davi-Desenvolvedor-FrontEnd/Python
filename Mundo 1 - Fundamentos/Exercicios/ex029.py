distanciaViagem = float(input("Digite o distância da viagem: "))

if distanciaViagem <= 200:
    preco = distanciaViagem*0.5
else:
    preco = distanciaViagem*0.45

print(f"O valor a ser pago é de R$ {preco:.2f}")