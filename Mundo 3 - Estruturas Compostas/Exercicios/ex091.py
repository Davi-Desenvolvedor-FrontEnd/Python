from tabulate import tabulate

jogadores = []
jogador = {}

while True:
    jogador.clear()
    jogador["nome"] = str(input("Nome: "))
    jogador["partidas"] = int(input("Partidas: "))
    jogador["gols"] = []
    if jogador["partidas"] > 0:
        for i in range(0, jogador["partidas"]):
            jogador["gols"].append(int(input(f"Gols na partida {i + 1}: ")))
    jogadores.append(jogador.copy())
    continuar = str(input("Quer continuar? [S/N] ")).upper()
    if continuar == "N":
        break

# print("-"*40)
# for j in jogador:
#     print(f"{j:^10}", end=" ")
# print()
# print("-"*40)
# for jogador in jogadores:
#     for j in jogador:
#         print(f"{jogador[j]}", end=" ")
#     print()

print(tabulate(jogadores, headers="keys", tablefmt="psql"))