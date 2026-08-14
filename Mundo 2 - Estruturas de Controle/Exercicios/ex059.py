primeiroTermo = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
total = 0
n = 1
continuar = True
termo = primeiroTermo
mais = 10
while continuar:
    total = total + mais
    while n <= total:
        termo = termo + razao
        print(f"{termo}{" =>" if n != total else " Pausa para hidratação"}", end=" ")
        n += 1
    mais = int(input("\nQuantos termos a mais? "))
    if mais == 0:
        continuar = False