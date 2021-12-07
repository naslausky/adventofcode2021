# Desafio do dia 07/12/2021:
#a) Receber uma lista de números e descobrir um número cuja soma das distâncias para os outros pontos seja mínima.
#b) Idem porém para uma função de custo quadrática em relação a distância.

with open('input.txt') as file:
	numerosString = file.read()
	numeros = numerosString.split(',')
	numeros = list(map(int,numeros))

gastoMinimoCombustivel = 10**20
for posicao in range (min(numeros),max(numeros)):
	combustivel = 0
	for numero in numeros:
		combustivel += abs(numero-posicao)
	if combustivel < gastoMinimoCombustivel:
		gastoMinimoCombustivel = combustivel
print("O mínimo de combustível necessário para mover os caranguejos é:", gastoMinimoCombustivel)

#Parte 2:
gastoMinimoCombustivel = 10**20
for posicao in range(min(numeros), max(numeros)):
	custo = 0
	for numero in numeros:
		distanciaDaPosicao = abs(numero - posicao)
		custoDessaPosicao = distanciaDaPosicao * (distanciaDaPosicao+1) / 2
		custo += int(custoDessaPosicao)
	if custo < gastoMinimoCombustivel:
		gastoMinimoCombustivel = custo

print("O mínimo de combustível necessário para mover os caranguejos da segunda forma é:", gastoMinimoCombustivel)
