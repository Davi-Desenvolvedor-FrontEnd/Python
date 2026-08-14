import datetime

ano = int(input("Qual ano deseja analisar? (Digite 0 para ano atual) "))

if ano == 0:
    resposta = datetime.date.today().year
elif ano % 4 == 0:
    resposta = "É bissexto"
else:
    resposta = "Não é bissexto"

print(resposta)