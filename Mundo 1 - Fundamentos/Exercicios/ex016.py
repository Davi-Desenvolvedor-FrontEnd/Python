import math
angulo = int(input("Digite um ângulo: "))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))
print(f"Para o ângulo de {angulo}°, \n o seno é igual a: {sen:.1f} \n cosseno é igual a: {cos:.1f} \n e tangente é igual a: {tg:.1f}")