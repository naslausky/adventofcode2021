# Desafio do dia 07/12/2021:
#a) Receber uma lista de números e descobrir um número cuja soma das distâncias para os outros pontos seja mínima.
#b) Idem porém para uma função de custo quadrática em relação a distância.

with open('input.txt') as file:
	numerosString = file.read()
	numeros = numerosString.split(',')
	numeros = list(map(int,numeros))

gastoMinimoCombustivel = gastoMinimoCombustivelParte2 = 10**20
for posicao in range (min(numeros),max(numeros)):
	custo = custoParte2 = 0
	for numero in numeros: # Calcula o custo dessa posição para as duas regras:
		custo += abs(numero-posicao) # Parte 1
		distanciaDaPosicao = abs(numero - posicao) # Parte 2
		custoDessaPosicao = distanciaDaPosicao * (distanciaDaPosicao+1) / 2
		custoParte2 += int(custoDessaPosicao)

	if custo < gastoMinimoCombustivel:
		gastoMinimoCombustivel = custo
	if custoParte2 < gastoMinimoCombustivelParte2:
		gastoMinimoCombustivelParte2 = custoParte2
print("O mínimo de combustível necessário para mover os caranguejos é:", gastoMinimoCombustivel)
print("O mínimo de combustível necessário para mover os caranguejos da segunda forma é:", gastoMinimoCombustivelParte2)
