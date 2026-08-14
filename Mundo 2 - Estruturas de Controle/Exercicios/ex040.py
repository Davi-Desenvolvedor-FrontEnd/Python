arquivo = open("../../Mundo 1 - Fundamentos/Exercicios/resultado.txt", "r")
pode = arquivo.readline().strip()
lado1 = int(arquivo.readline().strip())
lado2 = int(arquivo.readline().strip())
lado3 = int(arquivo.readline().strip())
arquivo.close()

if pode == "True":
    if lado1 == lado2 == lado3:
        print("Este triângulo é equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Este triângulo é isósceles")
    else:
        print("Este triângulo é escaleno")
else:
    print("")