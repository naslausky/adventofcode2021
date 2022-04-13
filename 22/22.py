# Desafio do dia 22/12/2021
# a)
# b)
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
def pretty(d, indent=0):
	for key, value in d.items():
		print('\t' * indent + str(key))
		if isinstance(value, dict):
			pretty(value, indent+1)
		else:
			print('\t' * (indent+1) + str(value))
#Faz 3 listas com cada range possível
rangesOrdenados = [[],[],[]]
for intervalos, _ in instrucoes:
	for i, intervalo in enumerate(intervalos):
		intervaloNormalizado = (intervalo[0],intervalo[1]+1)
		rangesOrdenados[i].extend(intervaloNormalizado)
rangesOrdenados = [list(set(r))for r in rangesOrdenados]
[r.sort() for r in rangesOrdenados]
def intervaloEstaContidoNaInstrucao(intervalos, instrucao):
	for dimensao in range(len(intervalos)): 
		if not 	intervaloEstaContidoEmOutro(intervalos[dimensao], instrucao[dimensao]):
			return False
	return True
	
def intervaloEstaContidoEmOutro(menor, maior):
	if menor[0]>= maior[0] and menor[1] <= maior[1]+1:
		return True
	return False
respostaFinal = 0
print('Objetivo:',len(rangesOrdenados[0]))
#print(len(rangesOrdenados[1]))
#print(len(rangesOrdenados[2]))
for indiceX in range(len(rangesOrdenados[0])-1):
	if not indiceX % 100:
		print('Alcançado', indiceX)
	rangeX = (rangesOrdenados[0][indiceX],rangesOrdenados[0][indiceX+1])
	iX = [(i,l) for i, l in instrucoes if intervaloEstaContidoEmOutro(rangeX,i[0])]
	if not iX:
		continue
	for indiceY in range(len(rangesOrdenados[1])-1):
		rangeY = (rangesOrdenados[1][indiceY],rangesOrdenados[1][indiceY+1])
		iY = [(i,l) for i,l in iX if intervaloEstaContidoEmOutro(rangeY, i[1])]
		if not iY:
			continue
		for indiceZ in range(len(rangesOrdenados[2])-1):
			rangeZ = (rangesOrdenados[2][indiceZ],rangesOrdenados[2][indiceZ+1])
			iZ = [(i,l) for i,l in iY if intervaloEstaContidoEmOutro(rangeZ,i[2])]
			if not iZ:
				continue
			intervaloAVerificar = (rangeX,rangeY,rangeZ) #Acho que nem precisa
			intervaloAceso = False
			#for intervalos, ligado in iZ: #Posso limitar aqui tb
			#	#Ve se esse range é afetado por essa instrucao:
			#	if intervaloEstaContidoNaInstrucao(intervaloAVerificar ,intervalos):
			intervaloAceso = iZ[-1][1]
			if intervaloAceso:
				respostaFinal +=((rangeZ[1] - rangeZ[0])*
						(rangeY[1] - rangeY[0])*
						(rangeX[1] - rangeX[0]))

print(respostaFinal)
