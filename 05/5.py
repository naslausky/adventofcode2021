# Desafio do dia 05/12/2021
#a) Dada uma lista de segmentos de linha em um espaço discreto, calcular quantos pontos contém mais de uma linha.
#b) Idem porém considerando também as linhas diagonais.

with open('input.txt') as file:
	linhas = file.read().splitlines()

def qtdDeCoordenadasSobrepostas(linhas, parte2=False):
	coordenadasPercorridas = {} # Dicionário que relaciona coordenadas (x,y) com o número de vezes que uma linha passa por cima dela.
	for linha in linhas:
		origem, destino = linha.split(" -> ")
		origem = origem.split(',')
		origem = list(map(int, origem))
		destino = destino.split(',')
		destino = list(map(int, destino))
		if not parte2: # Ignora as linhas diagonais se não for a parte 2.
			if origem[0] != destino[0] and origem[1] != destino[1]:
				continue
		coordenadaAtual = origem[:]
		chave = tuple(coordenadaAtual)
		coordenadasPercorridas[chave] = coordenadasPercorridas.get(chave,0) + 1 # Como ele inclui os pontos iniciais e finais, preciso fazer aqui também.
		while tuple(coordenadaAtual) != tuple(destino):
			for dim in range (2): # Repete para o eixo X e Y.
				if coordenadaAtual[dim] != destino[dim]: # Ainda não chegou nessa dimensão.
					coordenadaAtual[dim] += 1 if coordenadaAtual[dim] < destino[dim] else -1 # Incrementa um passo nesse eixo.
			chave = tuple(coordenadaAtual)
			coordenadasPercorridas[chave] = coordenadasPercorridas.get(chave,0) + 1
	coordenadasComSobreposicaoDeLinhas = [chave 
						for chave,valor in coordenadasPercorridas.items() 
						if valor > 1]
	return len(coordenadasComSobreposicaoDeLinhas)

print("Número de coordenadas com sobreposição de linhas:", qtdDeCoordenadasSobrepostas(linhas))
print("Número de coordenadas com sobreposição de linhas considerando as diagonais:", qtdDeCoordenadasSobrepostas(linhas, True))
