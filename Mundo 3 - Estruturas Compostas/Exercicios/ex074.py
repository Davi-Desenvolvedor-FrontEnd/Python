palavras = (
    "arroz",
    "desenho",
    "olho"
)

count = 0
vogais = ""

for i in range(0, len(palavras)):
    palavra = palavras[i]
    print(f"A palavra {palavra} tem: ")
    for j in range(0, len(palavra)):
        if palavra[j].lower() in "aeiou":
            count += 1
            vogais += f"{palavra[j].lower()} "

    print(f"{count} vogais, sendo elas: {vogais.strip()}")
    count = 0
    vogais = ""

