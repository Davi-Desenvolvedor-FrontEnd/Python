idade = int(input("Qual sua idade? "))

# if idade < 18:
#     print("Você é criança")
# elif idade >= 18 and idade < 65:
#     print("Você é adulto")
# else:
#     print("Você é velho")

media = float(input("Digite sua média total: "))
frequencia = int(input("Digite sua frequência total (em %): "))

if media >= 60 and frequencia >= 75:
    print("Aluno aprovado!")
elif media < 60 and frequencia >= 75:
    print("Aluno de recuperação!")
elif media > 60 and frequencia < 75:
    print("Aluno reprovado!")

print("=== FIM ===")