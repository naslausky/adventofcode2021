# Desafio do dia 22/12/2021:
# a) Receber uma lista de instruções, referentes a acender ou apagar seções em um espaço tridimensional discreto. Calcular quantos pontos terminaram acesos.
# b) O mesmo, porém para muito mais instruções e que englobem índices bem maiores (+-50k).

with open('input.txt') as file:
	instrucoes = []
	linhas = file.read().splitlines()
	for linha in linhas:
		ligado, intervalos = linha.split()	
		ligado = True if ligado == 'on' else False
		intervalos = intervalos.split(',')
		intervalos = [i.split('=')[1] for i in intervalos]
		intervalos = [i.split('..') for i in intervalos]
		intervalos = [list(map(int,i)) for i in intervalos]
		intervalos = tuple([tuple(i) for i in intervalos])
		instrucoes.append((intervalos, ligado))	

intervalosOrdenados = [[],[],[]] # Lista que pega todos os intervalos possíveis em cada dimensão. Cada instrução adiciona dois números em cada lista.
for intervalos, _ in instrucoes:
	for indice, intervalo in enumerate(intervalos):
		intervaloNormalizado = (intervalo[0],intervalo[1]+1) # Soma um ao índice superior pois cada instrução acende os índices inferior e superior inclusive.
		intervalosOrdenados[indice].extend(intervaloNormalizado)
intervalosOrdenados = [list(set(r))for r in intervalosOrdenados] # Remove duplicatas na lista de intervalos.
[r.sort() for r in intervalosOrdenados]

def intervaloEstaContidoNaInstrucao(intervalos, instrucao): # Função que verifica se um conjunto de 3 intervalos (x,y,z) é afetado por uma instrução.
	for dimensao in range(len(intervalos)): 
		if not 	intervaloEstaContidoEmOutro(intervalos[dimensao], instrucao[dimensao]):
			return False
	return True
	
def intervaloEstaContidoEmOutro(menor, maior): # Função que verifica se um intervalo (a,b) está incluso em outro.
	if menor[0]>= maior[0] and menor[1] <= maior[1]+1: # +1 foi necessário pois "maior" é utilizado vindo direto das instruções de entrada.
		return True
	return False

def intervaloEstaContidoNaZonaDeInicializacao(intervalos): # Função que diferencia a parte 1 da parte 2.
	for intervalo in intervalos:
		for indice in intervalo:
			if abs(indice) > 50:
				return False
	return True

somaRegiaoInicializacao = 0 # Resposta parte 1.
somaCompleta = 0 # Resposta parte 2.
for indiceX in range(len(intervalosOrdenados[0])-1): # Verifica todas as combinações de intervalos possíveis.
	rangeX = (intervalosOrdenados[0][indiceX],intervalosOrdenados[0][indiceX+1]) # Monta o intervalo a ser testado.
	iX = [(i,l) for i, l in instrucoes if intervaloEstaContidoEmOutro(rangeX,i[0])] # Das instruções, quais afetam esse intervalo X específico.
	if not iX: #
		continue
	for indiceY in range(len(intervalosOrdenados[1])-1):
		rangeY = (intervalosOrdenados[1][indiceY],intervalosOrdenados[1][indiceY+1])
		iY = [(i,l) for i,l in iX if intervaloEstaContidoEmOutro(rangeY, i[1])] # Das instruções que sobraram, quais também afetam esse intervalo Y. 
		if not iY:
			continue # Não tem porque iterar sobre todos os intervalos Z se nenhuma instrução afeta essa combinação de intervalos X e Y.
		for indiceZ in range(len(intervalosOrdenados[2])-1):
			rangeZ = (intervalosOrdenados[2][indiceZ],intervalosOrdenados[2][indiceZ+1])
			iZ = [(i,l) for i,l in iY if intervaloEstaContidoEmOutro(rangeZ,i[2])]
			if not iZ:
				continue
			intervaloAceso = iZ[-1][1] # É necessário apenas olhar a última instrução que afeta esse intervalo X,Y,Z.
			if intervaloAceso:
				quantidadeDeElementosNoIntervalo = ((rangeZ[1] - rangeZ[0]) *
									(rangeY[1] - rangeY[0]) *
									(rangeX[1] - rangeX[0]))
				somaCompleta += quantidadeDeElementosNoIntervalo
				if intervaloEstaContidoNaZonaDeInicializacao((rangeX,rangeY,rangeZ)):
					somaRegiaoInicializacao += quantidadeDeElementosNoIntervalo

print('Quantidade de cubos acesos na região de inicialização:', somaRegiaoInicializacao)
print('Quantidade de cubos acesos na região completa:', somaCompleta)
