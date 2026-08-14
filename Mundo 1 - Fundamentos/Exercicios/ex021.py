num = int(input("Digite um número: "))
milhar = str(num % 10000)
centena = str(num % 1000)
dezena = str(num % 100)
unidade = str(num % 10)

print(f"O número {num} tem: \n milhar: {milhar[0]} \n centena: {centena[0]} \n dezena: {dezena[0]} \n unidade: {unidade[0]}")