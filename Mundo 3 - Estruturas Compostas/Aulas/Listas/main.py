# lista = ["Davi", 18, 1.80, "Programador"]
# num = [100, 2, 6, 67, 99]
# nomes = ["Davi", "Danilo", "Wittor", "Bryan", "Marcus"]
#
# # for l in lista:
# #     print(l)
#
# # nomes.sort(reverse=True)
# # num.pop(1)
# num.insert(4, 68)
#
# for i, n in enumerate(num):
#     print(f"{i}: {n}")

notas = []
count = 0

while True:
    n = float(input(f"Digite sua {count+1}° nota: "))
    if n < 0:
        break
    notas.append(n)
    count += 1

print(f"Sua média foi {(sum(notas) / len(notas)):.1f}")