with open('input.txt') as file:
	linhas = file.read().splitlines()

coordenadasPercorridas = {} # Dicionário que relaciona coordenadas (x,y) com o número de vezes que uma linha passa por cima dela.
for linha in linhas:
	origem, destino = linha.split(" -> ")
	origem = origem.split(',')
	origem = list(map(int, origem))
	destino = destino.split(',')
	destino = list(map(int, destino))
	
	if origem[0] == destino[0]:
		delta = (origem[1],destino[1])
		for indice in range(min(delta), max(delta)+1):
			chave = (origem[0], indice)
			coordenadasPercorridas[chave] = coordenadasPercorridas.get(chave, 0) + 1
	elif origem[1] == destino[1]:
		delta = (origem[0],destino[0])
		for indice in range(min(delta), max(delta)+1):
			chave = (indice, origem[1])
			coordenadasPercorridas[chave] = coordenadasPercorridas.get(chave, 0) + 1
	else: #Diagonais
		coordenadaAtual = origem[:]
		while tuple(coordenadaAtual) != tuple(destino):
			chave = tuple(coordenadaAtual)
			coordenadasPercorridas[chave] = coordenadasPercorridas.get(chave, 0) + 1
			#incrementa um passo:
			coordenadaAtual[0] += 1 if coordenadaAtual[0] < destino[0] else -1
			coordenadaAtual[1] += 1 if coordenadaAtual[1] < destino[1] else -1
		chave = tuple(coordenadaAtual)
		coordenadasPercorridas[chave] = coordenadasPercorridas.get(chave, 0) + 1
coordenadasComSobreposicaoDeLinhas = [chave 
					for chave,valor in coordenadasPercorridas.items() 
					if valor > 1]
print(len(coordenadasComSobreposicaoDeLinhas))


