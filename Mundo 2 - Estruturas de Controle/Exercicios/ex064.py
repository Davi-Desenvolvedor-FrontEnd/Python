while True:
    n = int(input("Deseja ver a tabuada de qual número? "))
    print("-"*38)
    if n < 0:
        break
    for i in range(1, 11):
        print(f"{n} x {i:>2} = {(n*i):>2}")

print("PROGRAMA FINALIZADO COM SUCESSO!")