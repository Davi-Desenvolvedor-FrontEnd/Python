valorCasa = float(input("Digite o valor da casa: R$ "))
anos = int(input("Digite em quantos anos deseja pagar: "))
salario = float(input("Digite seu sálario atual: R$ "))

tempo = anos*12
prestacao = valorCasa/tempo

if prestacao > (salario*0.3):
    messagem = "emprestimo negado"
else:
    messagem = "emprestimo aprovado"

print(f"A pretação será de R$ {prestacao:.2f} num perído de {anos} anos, {messagem}")