import math

def Area(tipo, dimensoes: list):
       if tipo == "Q":
           a = math.pow(dimensoes[0], 2)
           print(f"O quadrado de lado {dimensoes[0]} tem {a:.1f} m²")
       elif tipo == "T":
           a = (dimensoes[0] * dimensoes[1]) / 2
           print(f"O triângulo de base {dimensoes[0]} e altura {dimensoes[1]} \ntem {a:.1f} m²")
       elif tipo == "H":
           a = ( 3 * math.pow(dimensoes[0], 2) * math.pow(3, 0.5)) / 2
           print(f"O hexágono de lado {dimensoes[0]} tem {a:.1f} m²")
       elif tipo == "C":
           a = math.pi * math.pow(dimensoes[0], 2)
           print(f"O círculo de raio {dimensoes[0]} tem {a:.1f} m²")

medidas = list()
print("Qual área deseja medir? ")
print("Q - Quadrado")
print("T - Triângulo")
print("R - Retângulo")
print("H - Hexágono")
print("C - Círculo")
figura = input().upper()

if figura == "Q" or figura == "H":
    medidas.append(int(input("Lado: ")))
elif figura == "T" or figura == "R":
    medidas.append(int(input("Base: ")))
    medidas.append(int(input("Altura: ")))
else:
    medidas.append(int(input("Raio: ")))

Area(figura, medidas)