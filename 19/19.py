# Desafio do dia 19/12/2021
def somaTuplas(x,y):
	x1,x2,x3 = x
	y1,y2,y3 = y
	return (x1+y1, x2+y2, x3+y3)

def diminuiTuplas(x,y):
	x1,x2,x3 = x
	y1,y2,y3 = y
	return (x1-y1, x2-y2, x3-y3)

def comporFuncao(f1, f2):
	return lambda x, y, z: f1 (*f2 (x,y,z))
	
def permutacoesDeUmaTupla(indice): #Retorna todas as 24 permutações dos eixos da coordenada tupla.
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


listaScanners = [] # Lista em que cada elemento é uma lista de tuplas contendo a leitura de cada beacon.
with open('input.txt') as file:
	linhasBeacons = file.read().split('\n\n')
	for linhaBeacon in linhasBeacons:
		linhasDesteBeacon = linhaBeacon.splitlines()[1:]
		linhasDesteBeacon = [tuple(
							map(int,linha.split(','))) 
							for linha in linhasDesteBeacon]
		listaScanners.append(linhasDesteBeacon)	
resposta = sum([len(x) for x in listaScanners])

posicoesRelativas = {}
permutacoes = {}

for indiceScanner in range(len(listaScanners)): # Para cada Scanner, procurar outro: 
	for indiceScanner2 in range(indiceScanner+1, len(listaScanners)):
		parScanner = (indiceScanner, indiceScanner2)
		listaScanner = listaScanners[indiceScanner]
		listaSegundoScanner = listaScanners[indiceScanner2]
		# Verifica se esses dois scanners tem no mínimo 12 em comum:
		# Precisa fazer isso para cada uma das 24 permutações.
		# Só permutamos o segundo até esse estar na mesma permutação do primeiro.
		#print('Testando scanners:', indiceScanner, indiceScanner2)
		l1 = listaScanner.copy()
		l1.sort()
		l2 = listaSegundoScanner.copy()
		numeroDeBeaconsScanner1 = len(l1)
		numeroDeBeaconsScanner2 = len(l2)
		for indicePermutacao in range(24):
			l2P = [permutacoesDeUmaTupla(indicePermutacao)(*x) for x in l2]
			for indicePivot1 in range(numeroDeBeaconsScanner1):
				for indicePivot2 in range(numeroDeBeaconsScanner2):
					if parScanner in posicoesRelativas:
						continue
					px, py, pz = l1[indicePivot1] # Coordenadas dos pivots:
					px2, py2, pz2 = l2P[indicePivot2]
					#Cria novas listas relativas ao pivot especifico:
					l1Relativo = [(x-px, y-py, z-pz) for x, y, z in l1]
					l2Relativo = [(x-px2, y-py2, z-pz2) for x, y, z in l2P]
					# Se eles tiverem 12 elementos em comum, achou
					
					elementosEmComum = [x for x in l1Relativo if x in l2Relativo]
					if len(elementosEmComum)>=12:
						posicaoRelativa = (px-px2, py-py2, pz-pz2) #Substituir pelo diminui tuplas
						posicoesRelativas[parScanner] = posicaoRelativa
						permutacoes[parScanner] = permutacoesInversasDeUmaTupla(indicePermutacao)
						
						#Permutacao[(a,b)] representa a função que precisamos aplicar a A para coincidir com os elementos de B
						#Fazer de novo mudando o referencial para o outro scanner:  Serve só pra facilitar a segunda parte.
						#Para isso, primeiramente a distancia é invertida (a-b vira b-a), e em seguida transformamos usando a inversa
						parScannerInverso = (indiceScanner2, indiceScanner) # Talvez usar o tuple(reversed())
						permutacoes[parScannerInverso] = permutacoesDeUmaTupla(indicePermutacao)
						posicaoRelativaInversa = (px2-px, py2-py, pz2-pz)
						posicaoRelativaInversa = permutacoesInversasDeUmaTupla(indicePermutacao)(*posicaoRelativaInversa)
						posicoesRelativas[parScannerInverso] = posicaoRelativaInversa

qtdScanners = len(listaScanners) 
while ( len([x for x,y in posicoesRelativas.items() if x[0]==0] ) < qtdScanners):
	caminhosDescobertosAteOZero = {x:y for x,y in posicoesRelativas.items() if x[0] == 0}
	for rota, distancia in caminhosDescobertosAteOZero.items():
		destino = rota[1]
		novosCaminhos = {}
		novasPermutacoes = {}
		for par, delta in posicoesRelativas.items():
			novoPar = (0, par[1])
			if par[0] == destino and novoPar not in posicoesRelativas:
				novosCaminhos[novoPar] = somaTuplas(
												distancia,
												permutacoes[(par[0],0)](*delta)
											)
				# Eu tinha o 0 a X e de X a Y
				# permutação [0, Y] é a função que deve ser aplicada aos elementos de 0 para ficarem iguais aos vistos por Y
				# ou seja,
				# Se Y enxerga (1,2,3), aplicamos permutacao(Y,X), significa que o 1,2,3 está permutado corretamente para a visão do X
				# Com o resultado disso aplicamos permutacao(X,0), significa que o ponto que antigamente Y via agora está para o 0.
				# Como fizemos um ponto visto por Y convertido para ser visto por 0, significa que isso é o valor de permutacao [Y,0]
				f1 = permutacoes[(par[0], 0)]
				f2 = permutacoes[(par[1],par[0])]
				funcaoComposta = comporFuncao(f1,f2) 
				novasPermutacoes[par[1],0] = funcaoComposta
				
				# Se 0 enxerga (1,2,3), aplicamos a permutacao (0,X), que é como X ve (1,2,3)
				# Depois, aplicamos [X,Y] e com isso temos como Y ve (1,2,3)
				# E isso é como transformamos o de 0 em Y, que é [0,Y]
				
				f3 = permutacoes[(0, par[0])]
				f4 = permutacoes[par]
				funcaoComposta2 = comporFuncao(f4,f3) 
				novasPermutacoes[novoPar] = funcaoComposta2
				
		posicoesRelativas.update(novosCaminhos)
		permutacoes.update(novasPermutacoes)
		
beaconsTotaisReferentesAoZero = set()

for indice, lista in enumerate(listaScanners):
	funcaoParaEsseScanner = permutacoes[(0, indice)]
	parIndice = (0,indice)
	distanciaAoZero = posicoesRelativas[parIndice]
	funcaoDeTransformacao = permutacoes[(parIndice[1],parIndice[0])]
	listaTransformada = [funcaoDeTransformacao(*x) for x in lista]
	listaTransladada = [somaTuplas(x, distanciaAoZero) for x in listaTransformada]
	beaconsTotaisReferentesAoZero.update(listaTransladada)
print(len(beaconsTotaisReferentesAoZero))


caminhosDescobertosAteOZero = [y for x,y in posicoesRelativas.items() if x[0] == 0]


maiorDistancia = 0

for indice1 in range(len(caminhosDescobertosAteOZero)):
	for indice2 in range(indice1 + 1, len(caminhosDescobertosAteOZero)):
		d1 = caminhosDescobertosAteOZero[indice1]
		d2 = caminhosDescobertosAteOZero[indice2]
		dist = abs(d1[0] - d2[0]) + abs(d1[1] - d2[1]) + abs(d1[2] - d2[2])
		maiorDistancia = max(maiorDistancia, dist)
		
print(maiorDistancia)



