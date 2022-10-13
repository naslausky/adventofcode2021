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

for listaScanner in listaScanners: #Para cada Scanner, procurar outro 
	[print(beacon) for beacon in listaScanner]
	break
