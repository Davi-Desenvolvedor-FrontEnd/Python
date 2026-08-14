num = []

for i in range(0, 5):
    n = int(input("Digite um valor: "))
    if i == 0 or n > max(num):
        num.append(n)
    elif n < min(num):
        num.insert(0, n)
    else:
        for p, numero in enumerate(num):
            if n < numero:
                num.insert(p, n)
                break
    print(num)

