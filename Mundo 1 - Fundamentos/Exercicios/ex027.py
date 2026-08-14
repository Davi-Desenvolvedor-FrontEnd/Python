limite = 80
multa = 7

velocidade = float(input("Qual a velocidade do carro? "))

if velocidade > limite:
    print(f"Limite de velocidade excedido, valor a pagar de multa: R$ {((velocidade-limite)*multa):.2f}")
else:
    print("Tenha um bom dia!")