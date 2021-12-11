with open('smallinput.txt') as file:
	linhas = file.read().splitlines()
	grid = {} 
	for indiceLinha, linha in enumerate(linhas):
		for indiceCaracter, caracter in enumerate(linha):
			coordenada = (indiceLinha, indiceCaracter)
			grid[coordenada] = int(caracter)

quantidadeDeFlashes = 0

def incrementarCoordenada(grid, coordenada):
	grid[coordenada] += 1
	if grid[coordenada] == 9:
		for dx in range(-1,2):
			for dy in range(-1,2):
				if dx != 0 or dy != 0:
					coordenadaAdjacente = (coordenada[0]+dx, coordenada[1]+dy)
					if coordenadaAdjacente in grid:
						incrementarCoordenada(grid, coordenadaAdjacente)
def imprimirGrid(grid):
	for ix in range(10):
		linha = [grid[(ix, iy)] for iy in range(10)]
		print(linha)

numeroDeFlashes = 0
for _ in range(100):
	for coordenada in grid:
		incrementarCoordenada(grid, coordenada)
	#numeroDeFlashesDessePasso = sum([1 for valor in grid.values() if valor>=9])
	for coordenada in grid:
		if grid[coordenada] >= 9:
			numeroDeFlashes += 1
			grid[coordenada] = 0
	imprimirGrid(grid)
	input()
	

print(numeroDeFlashes)

