distancia = float(input("Digite uma distância: "))
distanciaKm = distancia/1000
distanciaHem = distancia/100
distanciaDam = distancia/10
distanciaDm = distancia*10
distanciaCm = distancia*100
distanciaMm = distancia*1000

print(f"A medida {distancia} m corresponde a \n {distanciaKm} km \n {distanciaHem} hem \n {distanciaDam} dam \n {distanciaDm} dm \n {distanciaCm} cm \n {distanciaMm} mm")