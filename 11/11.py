# Desafio do dia 11/12/2021:
#a) Receber uma grid 10x10 e uma regra de incremento. Calcular quantas vezes os números passam de 10 ao longo de 100 passos.
#b) Calcular o número de passos para que a grid esteja toda com os números iguais.

with open('input.txt') as file:
	linhas = file.read().splitlines()
	grid = {} 
	for indiceLinha, linha in enumerate(linhas):
		for indiceCaracter, caracter in enumerate(linha):
			coordenada = (indiceLinha, indiceCaracter)
			grid[coordenada] = int(caracter)

def verificarFlash(grid, coordenada):
	if coordenada in coordenadasComFlash:
		return # Essa coordenada já teve flash esse turno.
	if grid[coordenada] >= 10:
		coordenadasComFlash.add(coordenada)
		for dx in range(-1,2):
			for dy in range(-1,2):
				if dx != 0 or dy != 0:
					coordenadaAdjacente = (coordenada[0]+dx, coordenada[1]+dy)
					if coordenadaAdjacente in grid:
						grid[coordenadaAdjacente] += 1		
						verificarFlash(grid, coordenadaAdjacente)
def imprimirGrid(grid):
	nLinhas = int(len(grid)**0.5)
	for ix in range(nLinhas):
		linha = [grid[(ix, iy)] for iy in range(nLinhas)]
		print(linha)

numeroDeFlashes = 0
numeroDePassos = 0
while sum([valor for valor in grid.values()]):
	coordenadasComFlash = set()
	for coordenada in grid:
		grid[coordenada] += 1
	for coordenada in grid:
		verificarFlash(grid, coordenada)
	for coordenada in grid:
		if grid[coordenada] > 9:
			numeroDeFlashes += 1
			grid[coordenada] = 0
	numeroDePassos += 1
	if numeroDePassos == 100:
		print("Número de flashes após 100 passos:", numeroDeFlashes)
print("Número de passos para os polvos sincronizarem:", numeroDePassos)

