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
with open('smallinput.txt') as file:
	linhasBeacons = file.read().split('\n\n')
	for linhaBeacon in linhasBeacons:
		linhasDesteBeacon = linhaBeacon.splitlines()[1:]
		linhasDesteBeacon = [tuple(
							map(int,linha.split(','))) 
							for linha in linhasDesteBeacon]
		listaScanners.append(linhasDesteBeacon)	

for indiceScanner in range(len(listaScanners)): # Para cada Scanner, procurar outro: 
	for indiceScanner2 in range(indiceScanner, len(listaScanners)):
		if indiceScanner == indiceScanner2:
			continue
		listaScanner = listaScanners[indiceScanner]
		listaSegundoScanner = listaScanners[indiceScanner2]
		# Verifica se esses dois scanners tem no mínimo 12 em comum:
		# Precisa fazer isso para cada uma das 24 permutações.
		# Só permutamos o segundo até esse estar na mesma permutação do primeiro.
		print('tentando scanners:', indiceScanner, indiceScanner2)
		l1 = listaScanner.copy()
		l1.sort()
		numeroDeBeaconsScanner1 = len(l1)
		for indicePermutacao in range(24):
			l2 = [permutacoesDeUmaTupla(x)[indicePermutacao] for x in listaSegundoScanner.copy()]
			l2.sort()
			numeroDeBeaconsScanner2 = len(l2)
			for indicePivot1 in range(numeroDeBeaconsScanner1):
				for indicePivot2 in range(numeroDeBeaconsScanner2):
					px, py, pz = l1[indicePivot1] # Coordenadas dos pivots:
					px2, py2, pz2 = l2[indicePivot2]
					#Cria novas listas relativas ao pivot especifico:
					l1Relativo = [(x-px, y-py, z-pz) for x, y, z in l1]
					l2Relativo = [(x-px, y-py, z-pz) for x, y, z in l2]
					# Se eles tiverem 12 elementos em comum, achou
					if indicePermutacao == 0 and indicePivot1 == 9 and indicePivot2 == 0:
						print('pivot1', px,py,pz)
						print('pivot2', px2,py2,pz2)
						print(l1Relativo)
						print(l2Relativo)
						input()
					elementosEmComum = [x for x in l1Relativo if x in l2Relativo]
					if indiceScanner == 0 and indiceScanner2 == 1 and len(elementosEmComum)!= 0:
						print('achados na permutacao>', len(elementosEmComum), indicePermutacao)
					if len(elementosEmComum) >= 12:
						print('Achou!', indiceScanner, indiceScanner2)
