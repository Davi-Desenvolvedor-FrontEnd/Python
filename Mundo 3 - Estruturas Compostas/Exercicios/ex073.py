items = (
    "Lápis", 18,
    "Sapato", 45,
    "Notebook", 3000
)

for i in range(0, items.__len__()):
    if i % 2 == 0:
        print(f"{items[i]:.<30}", end=" ")
    else:
        print(f"R$ {items[i]:<5}")
