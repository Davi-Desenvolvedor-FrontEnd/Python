n = int(input("Quantos termos do fibonacci? "))
first = 0
second = 1

print(f"{first}, {second}, ", end="")
while n > 0:
    termo = first + second
    print(f"{termo}, ", end='')
    first = second
    second = termo
    n -= 1
