# Desafio do dia 15/12/2021:
#a) Receber uma matriz de pesos e calcular o menor custo do caminho de um canto ao outro.
#b) Idem, porém com a matriz de pesos aumentada em 5 vezes em cada dimensão.

with open('input.txt') as file:
	linhas = file.read().splitlines()
	coordenadaFim = (len(linhas) - 1, len(linhas[0]) - 1 )
	tamanhoOriginal = (len(linhas), len(linhas[0]))
	mapa = {} # Dicionário com o valor de cada coordenada.
	for indiceLinha, linha in enumerate(linhas):
		for indiceNumero, numero in enumerate(linha):
			coordenada = (indiceLinha, indiceNumero)
			mapa[coordenada] = int(numero)

coordenadaAtual = (0,0) #Começa no começo.
coordenadasVerificadas = set() # Dicionário que relaciona o menor valor possível para chegar em uma dada coordenada.
gabarito = {coordenadaAtual : 0} # Dicionário que relaciona o mínimo possível para alcançar cada nó.
while (coordenadaFim not in coordenadasVerificadas): #Todas as coordenadas precisam ser verificadas.
	possibilidadesDeCaminhos = ((1,0),(0,1),(-1,0),(0,-1))
	for caminho in possibilidadesDeCaminhos:
		proximaCoordenada = (coordenadaAtual[0]+caminho[0], coordenadaAtual[1]+caminho[1])
		if proximaCoordenada not in mapa:
			continue
		gabarito[proximaCoordenada] = min(gabarito[coordenadaAtual] + mapa[proximaCoordenada],
						 gabarito.get(proximaCoordenada, 1000))
	coordenadasVerificadas.add(coordenadaAtual)
	proximasCandidatas = [coordenada for coordenada in gabarito if coordenada not in coordenadasVerificadas]
	if proximasCandidatas:
		custoDaProximaCoordenadaAVerificar = min(gabarito[coordenada] for coordenada in proximasCandidatas)
		proximasCoordenadaAVerificar = [coordenada for coordenada in proximasCandidatas if gabarito[coordenada]==custoDaProximaCoordenadaAVerificar]
		coordenadaAtual = proximasCoordenadaAVerificar[0]
print('Menor custo para percorrer a caverna:', gabarito[coordenadaFim])	
# Parte 2:
coordenadaFim = (((coordenadaFim[0]+1)*5)-1, ((coordenadaFim[1]+1)*5)-1)
novoMapa = {}
for chave in mapa:
	for indiceColuna in range(5):
		for indiceLinha in range(5):
			coordenadaReplicada = (chave[0]+indiceLinha*tamanhoOriginal[0], chave[1] + indiceColuna*tamanhoOriginal[1])	
			valor =  (mapa[chave] + indiceColuna + indiceLinha) % 9
			valor = 9 if valor == 0 else valor
			novoMapa[coordenadaReplicada] = valor
mapa = novoMapa
gabarito = {coordenadaFim : 0} # Dicionário que relaciona o mínimo possível para alcançar cada nó.
mudouAlgo = True
while (mudouAlgo):
	mudouAlgo = False
	for indiceLinha in range(coordenadaFim[0],-1,-1):
		for indiceColuna in range(coordenadaFim[1],-1,-1):
			coordenadaAtual = (indiceLinha, indiceColuna)
			possibilidadesDeCaminhos = ((1,0),(0,1),(-1,0),(0,-1))
			valores = []
			for caminho in possibilidadesDeCaminhos:
				proximaCoordenada = (coordenadaAtual[0]+caminho[0], coordenadaAtual[1]+caminho[1])
				if proximaCoordenada not in mapa:
					continue
				valores.append(mapa[proximaCoordenada] + gabarito.get(proximaCoordenada, 10**6))
			valores.append(gabarito.get(coordenadaAtual, 10**6))
			minimo = min(valores)
			if minimo != gabarito.get(coordenadaAtual, 10**6):
				mudouAlgo = True
				gabarito[coordenadaAtual] = minimo
print('Menor custo para percorrer a caverna expandida:', gabarito[(0,0)])	
