soma = 0
count = 0
for i in range(1, 500):
    if i % 2 != 0:
        if i % 3 == 0:
            count += 1
            soma += i

print(f"A soma dos {count} números ímpares e mútliplos de 3 é {soma}")