jogador = {
    "nome": input("Nome do jogador: "),
    "partidas": int(input("Quantidade de partidas: ")),
    "gols": [],
    "total": 0
}

for i in range(0, jogador["partidas"]):
    g = int(input(f"Quantos gols na partida {i+1}: "))
    jogador["gols"].append(g)
    jogador["total"] += g

print("-"*30)
print(f"O jogador {jogador["nome"]} jogou {jogador['partidas']} partidas, fez em cada partida:")

for i, g in enumerate(jogador["gols"]):
    print(f"       partida {i+1}: {g} gols")
print(f"total de {jogador['total']} gols")
print(f"Média de {(jogador['total']/jogador["partidas"]):.1f} gols por partid")
print("-"*30)