# Desafio do dia 19/12/2021
def somaTuplas(x,y):
	x1,x2,x3 = x
	y1,y2,y3 = y
	return (x1+y1, x2+y2, x3+y3)

def diminuiTuplas(x,y):
	x1,x2,x3 = x
	y1,y2,y3 = y
	return (x1-y1, x2-y2, x3-y3)
	
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
with open('smallinput.txt') as file:
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
			#l2P.sort()
			#if (indicePermutacao == 4 and indiceScanner == 0 and indiceScanner2 == 1):
			#	[print(l1[x], '\t\t', l2[x]) for x in range(25)]
			#	input()
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
					#if (indicePermutacao == 0 and indiceScanner == 0 and indiceScanner2 == 1 and 
					#	indicePivot1 == 6 and indicePivot2 == 4):
					#	print('pivot1', px,py,pz)
					#	print('pivot2', px2,py2,pz2)
					#	[print(l1Relativo[x], '\t\t', l2Relativo[x]) for x in range(25)]
					#	input()
					elementosEmComum = [x for x in l1Relativo if x in l2Relativo]
					if len(elementosEmComum)>=12:
						#print('Achada Interseção!: Scanners: ', parScanner,'Elementos em comum: ',
						#	 len(elementosEmComum),'Permutação: ', indicePermutacao)
#						segundoPontoPermutado = (px2,py2,pz2)
#						segundoPontoOriginal = permutacoesInversasDeUmaTupla(segundoPontoPermutado)[indicePermutacao]
#						px2o, py2o, pz2o = segundoPontoOriginal
						#print('É igual?', segundoPontoOriginal, l2[indicePivot2])
						posicaoRelativa = (px-px2, py-py2, pz-pz2) #Substituir pelo diminui tuplas
						posicoesRelativas[parScanner] = posicaoRelativa
						permutacoes[parScanner] = permutacoesInversasDeUmaTupla(indicePermutacao)
						
						
						#Fazer de novo mudando o referencial para o outro scanner:  Serve só pra facilitar a segunda parte.
						#Para isso, primeiramente a distancia é invertida (a-b vira b-a), e em seguida transformamos usando a inversa
						parScannerInverso = (indiceScanner2, indiceScanner) # Talvez usar o tuple(reversed())
						permutacoes[parScannerInverso] = permutacoesDeUmaTupla(indicePermutacao)
						posicaoRelativaInversa = (px2-px, py2-py, pz2-pz)
						posicaoRelativaInversa = permutacoesInversasDeUmaTupla(indicePermutacao)(*posicaoRelativaInversa)
						posicoesRelativas[parScannerInverso] = posicaoRelativaInversa




#[print(x,y) for x,y in posicoesRelativas.items()]
#[print(x,y) for x,y in permutacoes.items()]
#print('_________')
#[print(x,y) for x,y in permutacoes.items()]
# Preciso preencher o permutações completamente antes de usar abaixo:

#
#permutacoes[(0,4)] = permutacoesInversasDeUmaTupla(4)
#
#input()
#beaconsFinais = set()
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
												permutacoes[(0,par[0])](*delta)
											)
											
				f1 = permutacoes[(0, par[0])]
				f2 = permutacoes[par]
				funcaoComposta = lambda x, y, z: f2(*f1 (x,y,z))
				novasPermutacoes[par[1],0] = funcaoComposta #Como eu salvei ao contrario preciso salvar o contrario do contrario
				
				f1 = permutacoes[(par[0], 0)]
				f2 = permutacoes[par[1],par[0]]
				funcaoComposta = lambda x, y, z: f1 (*f2 (x,y,z))
				novasPermutacoes[novoPar] = funcaoComposta
				
		posicoesRelativas.update(novosCaminhos)
		permutacoes.update(novasPermutacoes)
		#print('atualizado:')
		#[print(x,y) for x,y in posicoesRelativas.items()]
		#print('___________')
#[print(x,y) for x,y in posicoesRelativas.items()]
[print(x,y) for x,y in posicoesRelativas.items() if x[0] == 0]
















		#print(novosCaminhos)
		#input()
#		posicoesRelativas.update(novosCaminhos)
#		[print(x,y) for x,y in posicoesRelativas.items()]
#		input()
	
	#caminhosDescobertosAteOZero = {x:y for x,y in posicoesRelativas.items() if x[0] == 0}
#	for rota, distancia in caminhosDescobertosAteOZero.items():
#		destino = rota[1]
#		novosCaminhos = {(0,x[0]):
#						
#						diminuiTuplas(
#							permutacoesInversasDeUmaTupla(permutacoes[(0,x[1])])(*y),
#							distancia
#						) 
#						for x,y in posicoesRelativas.items() if x[1] == destino # }
#															and (0, x[0]) not in posicoesRelativas}
		#print('novosembaixo', novosCaminhos)
		#print(novosCaminhos)
#		posicoesRelativas.update(novosCaminhos)
#		[print(x,y) for x,y in posicoesRelativas.items()]
#		input()
#	print('PosicoesRelativas:')
#	[print(x,y) for x,y in posicoesRelativas.items()]
#	input()

caminhosDescobertosAteOZero = {x:y for x,y in posicoesRelativas.items() if x[0] == 0}
#[print(x,y) for x,y in caminhosDescobertosAteOZero.items()]
#(0, 1) (68, -1246, -43)
#(1, 3) (160, -1134, -23)
#(2, 4) (1125, -168, 72)
#(1, 4) (88, 113, -1104)




#gabarito = {0:(0,0,0)} # Dicionario que relaciona cada scanner ao scanner 0.
#while(len(listaScanners) != len(gabarito)):
#	itemsAAdicionar = {}
#	for x,y in gabarito.items():
#		novoCaminho={(x,x2[1]):somaTuplas(y,y2) for x2,y2 in posicoesRelativas.items() if x==x2[0] and x2[1] not in gabarito}
#		print('NovoCaminho', novoCaminho)
#		input()
#		posicoesRelativas.update(novoCaminho) 
#		posicoesAoZero = {x[1]:y for x,y in posicoesRelativas.items() if x[0] == 0}
#		itemsAAdicionar.update(posicoesAoZero)
#		print('itemsAAdicionar', itemsAAdicionar) 
#		input()
#	gabarito.update(itemsAAdicionar)
#	print(gabarito)
#	input()
#(0, 1) (68, -1246, -43)
#(1, 3) (160, -1134, -23)
#(2, 4) (1125, -168, 72)
#(1, 4) (88, 113, -1104)
