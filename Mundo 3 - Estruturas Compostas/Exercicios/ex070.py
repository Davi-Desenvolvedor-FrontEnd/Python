from datetime import date

BR_2026 = (
    "Palmeiras",
    "Flamengo",
    "Athletico-PR",
    "Fluminense",
    "Bahia",
    "RB Bragantino",
    "Cruzeiro",
    "Botafogo",
    "Corinthians",
    "Atlético-MG",
    "Coritiba",
    "São Paulo",
    "Vitória",
    "Mirassol",
    "Santos",
    "Internacional",
    "Grêmio",
    "Vasco",
    "Remo",
    "Chapecoense"
)

print("-="*40)
print(f"Classificação do Brasileirão 2026:")
for i, b in enumerate(BR_2026):
    print(f"{i+1} - {b}")

print("-="*40)
print(f"5 primeiros colocados:")
for i in range(0, 5):
    print(f"{i+1} - {BR_2026[i]}")

print("-="*40)
print(f"4 últimos colocados:")
for i in range(-4, 0):
    print(f"{20+i+1} - {BR_2026[i]}")

print("-="*40)
print("Classificação em ordem alfabetica: ")
for i, b in enumerate(sorted(BR_2026)):
    print(f"{i+1} - {b}")

print("-="*40)
chape = BR_2026.index("Chapecoense")
print(f"A Chapecoense está na {chape+1}° posição")