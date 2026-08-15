def escreva(text: str):
    size = len(text)+4
    print("~" * size)
    print(f"{text:^{size}}")
    print("~"*size)

while True:
    msg = str(input("Sua frase: ")).strip()
    if msg == "":
        break
    escreva(msg)
