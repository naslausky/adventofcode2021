# Desafio do dia 19/12/2021:
# a) Receber uma lista de scanners e beacons que possuem interseções e calcular quantos beacons existem.
# b) Calcular a maior distância entre dois scanners.

def somaTuplas(x, y): # Função que recebe duas tuplas e calcula a soma elemento a elemento entre eles.
	x1, x2, x3 = x
	y1, y2, y3 = y
	return (x1 + y1, x2 + y2, x3 + y3)

def diminuiTuplas(x, y): # Função que recebe duas tuplas e calcula a diferença elemento a elemento.
	x1, x2, x3 = x
	y1, y2, y3 = y
	return (x1 - y1, x2 - y2, x3 - y3)

def comporFuncao(f1, f2): # Função que retorna outra função com a composição de duas funções.
	return lambda x, y, z: f1( *f2(x,y,z)) # Precisei fazer isso para gerar um novo escopo e evitar um bug.
	
def permutacoesDeUmaTupla(indice): 
	# Função que retorna uma função representando uma das 24 permutações dos eixos.
	if indice == 0: return lambda x, y, z:(x, y, z)
	if indice == 1: return lambda x, y, z: (x, -z, y)
	if indice == 2: return lambda x, y, z: (x, -y, -z)
	if indice == 3: return lambda x, y, z: (x, z, -y)
	if indice == 4: return lambda x, y, z: (-x, y, -z)
	if indice == 5: return lambda x, y, z: (-x, z, y)
	if indice == 6: return lambda x, y, z: (-x, -y, z)
	if indice == 7: return lambda x, y, z: (-x, -z, -y)
	if indice == 8: return lambda x, y, z: (y, z, x)
	if indice == 9: return lambda x, y, z: (y, x, -z)
	if indice == 10: return lambda x, y, z: (y, -z, -x)
	if indice == 11: return lambda x, y, z: (y, -x, z)
	if indice == 12: return lambda x, y, z: (-y, x, z)
	if indice == 13: return lambda x, y, z: (-y, -z, x)
	if indice == 14: return lambda x, y, z: (-y, -x, -z)
	if indice == 15: return lambda x, y, z: (-y, z, -x)
	if indice == 16: return lambda x, y, z: (z, y, -x)
	if indice == 17: return lambda x, y, z: (z, x, y)
	if indice == 18: return lambda x, y, z: (z, -y, x)
	if indice == 19: return lambda x, y, z: (z, -x, -y)
	if indice == 20: return lambda x, y, z: (-z, y, x)
	if indice == 21: return lambda x, y, z: (-z, x, -y)
	if indice == 22: return lambda x, y, z: (-z, -y, -x)
	if indice == 23: return lambda x, y, z: (-z, -x, y)

def permutacoesInversasDeUmaTupla(indice):
	# Função que retorna uma função representando a inversa da permutação de mesmo índice.
	if indice == 0: return lambda x, y, z: (x, y, z)
	if indice == 1: return lambda x, y, z: (x, z, -y)
	if indice == 2: return lambda x, y, z: (x, -y, -z)
	if indice == 3: return lambda x, y, z: (x, -z, y)
	if indice == 4: return lambda x, y, z: (-x, y, -z)
	if indice == 5: return lambda x, y, z: (-x, z, y)
	if indice == 6: return lambda x, y, z: (-x, -y, z)
	if indice == 7: return lambda x, y, z: (-x, -z, -y)
	if indice == 8: return lambda x, y, z: (z, x, y)
	if indice == 9: return lambda x, y, z: (y, x, -z)
	if indice == 10: return lambda x, y, z: (-z, x, -y)
	if indice == 11: return lambda x, y, z: (-y, x, z)
	if indice == 12: return lambda x, y, z: (y, -x, z)
	if indice == 13: return lambda x, y, z: (z, -x, -y)
	if indice == 14: return lambda x, y, z: (-y, -x, -z)
	if indice == 15: return lambda x, y, z: (-z, -x, y)
	if indice == 16: return lambda x, y, z: (-z, y, x)
	if indice == 17: return lambda x, y, z: (y, z, x)
	if indice == 18: return lambda x, y, z: (z, -y, x)
	if indice == 19: return lambda x, y, z: (-y, -z, x)
	if indice == 20: return lambda x, y, z: (z, y, -x)
	if indice == 21: return lambda x, y, z: (y, -z, -x)
	if indice == 22: return lambda x, y, z: (-z, -y, -x)
	if indice == 23: return lambda x, y, z: (-y, z, -x)

listaScanners = [] # Lista em que cada elemento é uma lista de tuplas contendo a leitura de cada scanner.
with open('input.txt') as file:
	linhasBeacons = file.read().split('\n\n')
	for linhaBeacon in linhasBeacons:
		linhasDesteBeacon = linhaBeacon.splitlines()[1:]
		linhasDesteBeacon = [tuple(
							map(int,linha.split(','))) 
							for linha in linhasDesteBeacon]
		listaScanners.append(linhasDesteBeacon)	

# Dicionário que relaciona uma tupla representando o índice de dois scanners e a distância entre eles.
# Da forma: {(0,1) : (123, 456, 789) ...}
posicoesRelativas = {}

# Dicionário que relaciona uma tupla representando o índice de dois scanners e a função que,
# quando aplicada aos beacons vistos pelo primeiro scanner, converte para os eixos do segundo:
# Da forma: {(2,3) : lambda } onde lambda(tupla_2) = tupla_3.
permutacoes = {}
# A parte 1 do desafio é feita em três etapas: a) Obter as interseções entre os scanners.
for indiceScanner in range(len(listaScanners)): # Para cada par de Scanners: 
	for indiceScanner2 in range(indiceScanner + 1, len(listaScanners)):
		parScanner = (indiceScanner, indiceScanner2) 
		listaScanner1 = listaScanners[indiceScanner] 
		listaScanner2 = listaScanners[indiceScanner2]
		# Verificar se esses dois scanners tem no mínimo 12 elementos em comum:
		# Tentar encontrá-los para cada uma das 24 permutações.
		# Só é necessário permutar um deles até este estar na mesma permutação do outro.
		numeroDeBeaconsScanner1 = len(listaScanner1)
		numeroDeBeaconsScanner2 = len(listaScanner2)
		for indicePermutacao in range(24):
			listaScanner2Permutada = [permutacoesDeUmaTupla(indicePermutacao)(*x) for x in listaScanner2]
			# Escolher um elemento de cada lista, e re-criar a lista tendo este ponto como centro.
			# Se os dois elementos escolhidos forem o mesmo, a variação pros outros também vai ser a mesma.
			for indicePivot1 in range(numeroDeBeaconsScanner1):
				for indicePivot2 in range(numeroDeBeaconsScanner2):
					pivot1 = listaScanner1[indicePivot1]
					pivot2 = listaScanner2Permutada[indicePivot2]
					# Cria as novas listas relativas ao pivot especifico:
					listaScanner1Relativa = [diminuiTuplas(elemento, pivot1) for elemento in listaScanner1]
					listaScanner2Relativa = [diminuiTuplas(elemento, pivot2) for elemento in listaScanner2Permutada]
					# Se eles tiverem 12 elementos em comum, achamos uma interseção.
					elementosEmComum = [1 for elemento in listaScanner1Relativa 
										if elemento in listaScanner2Relativa]
					if len(elementosEmComum) >= 12: 
						# Salvar a distância entre os scanners, bem como a permutação de eixos entre eles.
						posicaoRelativa = diminuiTuplas(pivot1, pivot2) # Posição entre os dois scanners.
						posicoesRelativas[parScanner] = posicaoRelativa
						permutacoes[parScanner] = permutacoesInversasDeUmaTupla(indicePermutacao)
						# Anotar também o caminho inverso:
						parScannerInverso = tuple(reversed(parScanner))
						permutacoes[parScannerInverso] = permutacoesDeUmaTupla(indicePermutacao)
						posicaoRelativaInversa = diminuiTuplas(pivot2, pivot1)
						posicaoRelativaInversa = permutacoes[parScanner](*posicaoRelativaInversa)
						posicoesRelativas[parScannerInverso] = posicaoRelativaInversa

# b) Dada as interseções encontradas, obter a transformação entre todos os scanners e um mesmo scanner de referência.
quantidadeDeScanners = len(listaScanners) 
while (len([x for x, y in posicoesRelativas.items() if x[0] == 0] ) < quantidadeDeScanners):
	# Compõe novos caminhos tendo o zero como origem. i.e: Obter (0 -> X) a partir de (0 -> Y) e (Y -> X)
	# Calcular para esses novos caminhos tanto a permutação quanto a posição relativa. 
	# Fazer isso até ter no mínimo um caminho de um mesmo scanner (no caso o 0) para todos os outros.
	caminhosDescobertosAteOZero = { x : y for x, y in posicoesRelativas.items() if x[0] == 0}
	for caminhoDescoberto, distanciaRelativa in caminhosDescobertosAteOZero.items():
		novaOrigem = caminhoDescoberto[1] # Buscar por novos caminhos que tem como origem este scanner.
		novosCaminhos = {} # Cria um novo dicionário pois o principal é o que vai ser iterado. 
		novasPermutacoes = {} # Idem para as permutações, embora acho que neste caso não precisasse.
		for parConhecido, delta in posicoesRelativas.items():
			novoPar = (0, parConhecido[1]) # Novo par a ser obtido após a composição.
			novoParInvertido = tuple(reversed(novoPar))
			if parConhecido[0] == novaOrigem and novoPar not in posicoesRelativas: # Significa que é um par que vai incrementar ao nosso dicionário.
				novosCaminhos[novoPar] = somaTuplas( # A distância (A -> B) é a distância (A -> X) + distância (X -> B).
												distanciaRelativa, # Poderíamos atualizar também a distância contrária (B -> A), mas aqui não é necessário ao problema, eu acho.
												permutacoes[(parConhecido[0],0)](*delta)
											)
				
				funcao1 = permutacoes[(parConhecido[0], 0)] # Funcao1 é a função que aplicada a um elemento visto por parConhecido[0], converte ele para os eixos do Scanner 0.
				funcao2 = permutacoes[(parConhecido[1], parConhecido[0])] 
				funcaoComposta = comporFuncao(funcao1,funcao2) # Primeiro aplicamos funcao2, para depois aplicarmos funcao1.
				novasPermutacoes[novoParInvertido] = funcaoComposta
				funcao1 = permutacoes[(0, parConhecido[0])] # Fazer o mesmo para o caminho da volta. É necessário pois existem Scanners que só descobrimos relações tendo ele com origem.
				funcao2 = permutacoes[parConhecido]
				funcaoComposta = comporFuncao(funcao2, funcao1) # A ordem de aplicação é inversa na volta.
				novasPermutacoes[novoPar] = funcaoComposta
				
		posicoesRelativas.update(novosCaminhos) # Atualizamos os nossos dicionários com as novas composições encontradas.
		permutacoes.update(novasPermutacoes)

# c) Juntar todos os beacons vistos por todos os scanners, utilizando as transformações encontradas e eliminando os repetidos.
beaconsTotaisReferentesAoZero = set() # Conjunto que vai conter todos os beacons vistos porém transformados para ter o Scanner 0 como seu referencial.
for indiceScanner, listaBeacons in enumerate(listaScanners):
	funcaoParaEsseScanner = permutacoes[(0, indiceScanner)]
	parIndice = (0, indiceScanner)
	parIndiceInvertido = tuple(reversed(parIndice))
	distanciaAoScannerZero = posicoesRelativas[parIndice]
	funcaoDeTransformacao = permutacoes[parIndiceInvertido] # Talvez se eu tivesse adotado a convenção contrária tivesse ficado mais intuitivo.
	listaTransformada = [funcaoDeTransformacao(*x) for x in listaBeacons] # Aplica a transformação para adaptar os eixos desse scanner.
	listaTransladada = [somaTuplas(x, distanciaAoScannerZero) for x in listaTransformada] # Após corrigir os eixos, aplicar a distância para transladar o referencial.
	beaconsTotaisReferentesAoZero.update(listaTransladada) # Soma ao conjunto esses beacons com a origem ao scanner 0.
print('O número total de beacons lidos pelos scanners é:', len(beaconsTotaisReferentesAoZero))

# Parte 2: Calcular a maior distância existente entre dois scanners.
caminhosDescobertosAteOZero = [y for x,y in posicoesRelativas.items() if x[0] == 0] # Podemos utilizar o dicionário de posições relativas já preenchido para a parte 1.
maiorDistancia = 0 # Variável que armazena a maior distância encontrada, e a resposta do problema.
for indiceScanner1 in range(len(caminhosDescobertosAteOZero)): # Percorre por todos os pares de scanner possíveis.
	for indiceScanner2 in range(indiceScanner1 + 1, len(caminhosDescobertosAteOZero)):
		distancia1 = caminhosDescobertosAteOZero[indiceScanner1] 
		distancia2 = caminhosDescobertosAteOZero[indiceScanner2]
		distanciaEntreOsScanners = diminuiTuplas(distancia1, distancia2)
		distanciaEntreOsScanners = sum(abs(distancia) for distancia in distanciaEntreOsScanners)
		maiorDistancia = max(maiorDistancia, distanciaEntreOsScanners)
print('A maior distância Manhattan entre dois scanners é:', maiorDistancia)
