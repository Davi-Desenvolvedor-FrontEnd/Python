import math
print("-=" * 20)
print("{:^20}".format("\033[1;34;40m Calculadora de IMC \033[m"))
print("-=" * 20)
peso = float(input("Seu peso (em kg): "))
altura = float(input("Sua altura (em metros): "))

imc = peso / (math.pow(altura, 2))

if imc < 18.5:
    res = "Abaixo do peso"
elif imc < 25:
    res = "Peso ideal"
elif imc < 30:
    res = "Sobrepeso"
elif imc < 40:
    res = "Obesidade"
else:
    res = "Obesidade morbida"

print(f"Seu imc é {imc:.2f} \nsua classificação: {res}")
print("-=" * 20)