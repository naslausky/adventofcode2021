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
paresEncontrados = set()
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
			l2P.sort()
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
						print('Achado!: Scanner: ',indiceScanner,' Scanner2:', indiceScanner2,'Elementos em comum: ',
							 len(elementosEmComum),'Permutação: ', indicePermutacao)
						#[print(l1Relativo[x], l2Relativo[x]) for x in range(25)]
						resposta-=len(elementosEmComum)
						paresEncontrados.add(parScanner)


print(resposta)
