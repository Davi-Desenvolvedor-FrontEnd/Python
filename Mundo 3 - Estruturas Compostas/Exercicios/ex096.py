from random import randint


def somPar(lista):
    som = 0
    count = randint(1, 10)
    print(f"Sorteando {count} valores da lista: ")
    while count > 0:
        n = randint(1, 100)
        if n not in lista:
            lista.append(n)
            if n % 2 == 0:
                som += n
            print(f"{n:.^5}", end="")
            count -= 1
    print()
    print(f"Da lista acima, a soma dos valores pares é {som}")

num = []
somPar(num)
print(num)