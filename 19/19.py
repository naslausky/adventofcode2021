# Desafio do dia 19/12/2021

def permutacoesDeUmaTupla(tupla): #Retorna todas as 24 permutações dos eixos da coordenada tupla.
	x, y, z = tupla
	return (
			(x, y, z),
			(x, -z, y),
			(x, -y, -z),
			(x, z, -y),
			
			(-x, y, -z),
			(-x, z, y),
			(-x, -y, z),
			(-x, -z, -y),

			(y, z, x),
			(y, x, -z),
			(y, -z, -x),
			(y, -x, z),

			(-y, x, z),
			(-y, -z, x),
			(-y, -x, -z),
			(-y, z, -x),

			(z, y, -x),
			(z, x, y),
			(z, -y, x),
			(z, -x, -y),

			(-z, y, x),
			(-z, x, -y),
			(-z, -y, -x),
			(-z, -x, y),
			)

def permutacoesInversasDeUmaTupla(tupla): #Retorna todas as 24 permutações dos eixos da coordenada tupla.
	x, y, z = tupla
	return (
			(x, y, z),
			(x, z, -y),
			(x, -y, -z),
			(x, -z, y),
			
			(-x, y, -z),
			(-x, z, y),
			(-x, -y, z),
			(-x, -z, -y),

			(z, x, y),
			(y, x, -z),
			(-z, x, -y),
			(-y, x, z),

			(y, -x, z),
			(z, -x, -y),
			(-y, -x, -z),
			(-z, -x, y),

			(-z, y, x),
			(y, z, x),
			(z, -y, x),
			(-y, -z, x),

			(z, y, -x),
			(y, -z, -x),
			(-z, -y, -x),
			(-y, z, -x),
			)

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
paresEncontrados = set()
posicoesRelativas = {}
pontosFinais = set()
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
			l2P = [permutacoesDeUmaTupla(x)[indicePermutacao] for x in l2]
			#l2P.sort()
			#if (indicePermutacao == 4 and indiceScanner == 0 and indiceScanner2 == 1):
			#	[print(l1[x], '\t\t', l2[x]) for x in range(25)]
			#	input()
			for indicePivot1 in range(numeroDeBeaconsScanner1):
				for indicePivot2 in range(numeroDeBeaconsScanner2):
					if parScanner in paresEncontrados:
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
						print('Achada Interseção!: Scanners: ', parScanner,'Elementos em comum: ',
							 len(elementosEmComum),'Permutação: ', indicePermutacao)
						segundoPontoPermutado = (px2,py2,pz2)
						segundoPontoOriginal = permutacoesInversasDeUmaTupla(segundoPontoPermutado)[indicePermutacao]
						px2o, py2o, pz2o = segundoPontoOriginal
						print('É igual?', segundoPontoOriginal, l2[indicePivot2])
						posicaoRelativa = (px-px2, py-py2, pz-pz2)
						if (parScanner==(1,4)):
							print(posicaoRelativa)
							print(px,py,pz)
							print(px2,py2,pz2)
							print('_________________')
#						
#						if (parScanner==(0,1)):
#							print(posicaoRelativa)
#							print(px,py,pz)
#							print(px2,py2,pz2)
#							print('_________________')
						#print('Posicao Relativa:', posicaoRelativa)
						#[print(l1Relativo[x], l2Relativo[x]) for x in range(25)]
						posicoesRelativas[parScanner] = posicaoRelativa
						resposta-=len(elementosEmComum)
						paresEncontrados.add(parScanner)

print(resposta)
def somaTuplas(x,y):
	x1,x2,x3 = x
	y1,y2,y3 = y
	return (x1+y1, x2+y2, x3+y3)

def diminuiTuplas(x,y):
	x1,x2,x3 = x
	y1,y2,y3 = y
	return (x1-y1, x2-y2, x3-y3)

[print(x,y) for x,y in posicoesRelativas.items()]
print('_________')
qtdScanners = len(listaScanners) 
while (len([x for x,y in posicoesRelativas.items() if x[0]==0]) < qtdScanners):
	caminhosDescobertosAteOZero = {x:y for x,y in posicoesRelativas.items() if x[0] == 0}
	#print('camin_ate_0:',caminhosDescobertosAteOZero)
	for rota, distancia in caminhosDescobertosAteOZero.items():
		destino = rota[1]
		novosCaminhos = {(0,x[1]):somaTuplas(distancia,y) 
						for x,y in posicoesRelativas.items() if x[0] == destino # }
															and (0, x[1]) not in posicoesRelativas}
		#print(novosCaminhos)
		posicoesRelativas.update(novosCaminhos)
#		[print(x,y) for x,y in posicoesRelativas.items()]
#		input()
	
	caminhosDescobertosAteOZero = {x:y for x,y in posicoesRelativas.items() if x[0] == 0}
	for rota, distancia in caminhosDescobertosAteOZero.items():
		destino = rota[1]
		novosCaminhos = {(0,x[0]):diminuiTuplas(y,distancia) 
						for x,y in posicoesRelativas.items() if x[1] == destino # }
															and (0, x[0]) not in posicoesRelativas}
		#print('novosembaixo', novosCaminhos)
		#print(novosCaminhos)
		posicoesRelativas.update(novosCaminhos)
#		[print(x,y) for x,y in posicoesRelativas.items()]
#		input()
#	print('PosicoesRelativas:')
#	[print(x,y) for x,y in posicoesRelativas.items()]
#	input()

caminhosDescobertosAteOZero = {x:y for x,y in posicoesRelativas.items() if x[0] == 0}
[print(x,y) for x,y in caminhosDescobertosAteOZero.items()]
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
