# Desafio do dia 09/12/2021:
#a) Receber um mapa 2D de alturas e calcular quantos pontos mínimos existem.
#b) No mesmo mapa, calcular o produto do tamanho das três maiores bacias.

with open('input.txt') as file:
	linhas = file.read().splitlines()
	alturas = {} # Dicionário que relaciona as coordenadas a suas alturas.
	for indiceLinha, linha in enumerate(linhas):
		for indiceCaracter, caracter in enumerate(linha):
			coordenada = (indiceLinha, indiceCaracter)
			alturas[coordenada] = int(caracter)
somaDasAlturasDosPontosMinimos = 0
coordenadasPontosBaixos = [] # Lista dos pontos mínimos para usar na parte 2.
for coordenada, altura in alturas.items():
	adjacentes = ((-1,0),(1,0),(0,-1),(0,1))
	possuiPontoMenorAdjacente = False
	for adjacente in adjacentes:
		coordenadaAVerificar = (coordenada[0]+adjacente[0],
					coordenada[1]+adjacente[1])
		if coordenadaAVerificar in alturas:
			if alturas[coordenadaAVerificar] <= altura:
				possuiPontoMenorAdjacente = True
	if not possuiPontoMenorAdjacente: # Significa que é um ponto mínimo.
		somaDasAlturasDosPontosMinimos += 1 + altura 
		coordenadasPontosBaixos.append(coordenada)
print('A soma das alturas de todos os pontos mínimos é:', somaDasAlturasDosPontosMinimos) 

# Parte 2:
def quantidadeDePontosMaiores(coordenada): # Função que recebe uma coordenada e retorna o conjunto de outras coordenadas ao redor dela que tem seu valor crescente.
	resposta = {coordenada} # Precisa ser um conjunto pois não podemos contar duas vezes uma coordenada.
	adjacentes = ((-1,0),(1,0),(0,-1),(0,1))
	for adjacente in adjacentes:
		coordenadaAVerificar = (coordenada[0] + adjacente[0],
					coordenada[1] + adjacente[1])
		if coordenadaAVerificar in alturas:
			if alturas[coordenadaAVerificar] > alturas[coordenada] and alturas[coordenadaAVerificar] != 9:
				resposta.update(quantidadeDePontosMaiores(coordenadaAVerificar))
	return resposta

tamanhosDasBacias = [len(quantidadeDePontosMaiores(coordenada)) for coordenada in coordenadasPontosBaixos]
tamanhosDasBacias.sort()
multiplicacaoDoTamanhoDasBacias = 1
for _ in range(3):
	multiplicacaoDoTamanhoDasBacias *= tamanhosDasBacias.pop()
print("O produto do tamanho das três maiores bacias é:", multiplicacaoDoTamanhoDasBacias)
