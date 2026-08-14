soma = count = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    soma += n
    count += 1
print(f"O usuário digitou {count} números \ne a soma entre eles é {soma}")