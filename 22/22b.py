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
		rangesOrdenados[i].extend(intervalo)
rangesOrdenados = [list(set(r))for r in rangesOrdenados]
[r.sort() for r in rangesOrdenados]

dicionarioFilho2 = {}
for indiceZ in range(len(rangesOrdenados[2])-1):
	rangeZ = (rangesOrdenados[2][indiceZ], rangesOrdenados[2][indiceZ+1])
	dicionarioFilho2[rangeZ] = False
	rangeZ2 = (rangeZ[1], rangeZ[1]+1)
	dicionarioFilho2[rangeZ2] = False
#print('filho2:')
#pretty(dicionarioFilho2)
#input()
dicionarioFilho1 = {}
for indiceY in range(len(rangesOrdenados[1])-1):
	rangeY = (rangesOrdenados[1][indiceY], rangesOrdenados[1][indiceY+1])
	dicionarioFilho1[rangeY] = dicionarioFilho2.copy() 
	rangeY2 = (rangeY[1],rangeY[1]+1)
	dicionarioFilho1[rangeY2] = dicionarioFilho2.copy()

dicionarioPai = {}
for indiceX in range(len(rangesOrdenados[0])-1):
	rangeX = (rangesOrdenados[0][indiceX], rangesOrdenados[0][indiceX+1])
	dicionarioPai[rangeX] = {k:v.copy() for k,v in dicionarioFilho1.items()}
	rangeX2 = (rangeX[1],rangeX[1]+1)
	dicionarioPai[rangeX2] = {k:v.copy() for k,v in dicionarioFilho1.items()}
#pretty(dicionarioPai)
#input()
def inserirInstrucaoNoDicionario(intervalos, aceso, dicDestino):
	ultimoNivel = len(intervalos) == 1
	intervaloDaVez = intervalos[0]
	indiceInferior, indiceSuperior = intervaloDaVez
	comeco = indiceInferior
	while comeco < indiceSuperior:
		intervalo = [x for x in dicDestino if x[0] == comeco][0]
		if ultimoNivel:
			dicDestino[intervalo] = aceso
		else:
			inserirInstrucaoNoDicionario(intervalos[1:], aceso, dicDestino[intervalo])
		comeco = intervalo[1]
	ultimoIntervalo = (indiceSuperior, indiceSuperior+1)
	if ultimoIntervalo in dicDestino:
		if ultimoNivel:
			dicDestino[ultimoIntervalo] = aceso
		else:
			inserirInstrucaoNoDicionario(intervalos[1:], aceso, dicDestino[ultimoIntervalo])

for intervalo, ligado in instrucoes:
	inserirInstrucaoNoDicionario(intervalo, ligado, dicionarioPai)
#pretty(dicionarioPai)
#input()
resposta = 0
for rangeX, dicionarioFilho1 in dicionarioPai.items():
	for rangeY, dicionarioFilho2 in dicionarioFilho1.items():
		for rangeZ, aceso in dicionarioFilho2.items():
			if aceso:
				resposta += ((rangeZ[1] - rangeZ[0])*
						(rangeY[1] - rangeY[0])*
						(rangeX[1] - rangeX[0]))	
print('terminou', resposta)
#resposta = 0
#for indiceX in range(len(rangesOrdenados[0])-1):
#	rangeX = (rangesOrdenados[0][indiceX], rangesOrdenados[0][indiceX+1])
#	for indiceY in range(len(rangesOrdenados[1])-1):
#		rangeY = (rangesOrdenados[1][indiceY], rangesOrdenados[1][indiceY+1])
#		for indiceZ in range(len(rangesOrdenados[2])-1):
#			rangeZ = (rangesOrdenados[2][indiceZ], rangesOrdenados[2][indiceZ+1])
#			esseRangeEstaAceso = False
#			for intervalos, aceso in instrucoes:
#				#Verificar se o rangex, rangey e rangez é afetado por essa instrução:
#				x,y,z = intervalos
#				if rangeX[0] >= x[0] and rangeX[1]<x[1]:
#					if rangeY[0] >= y[0] and rangeY[1]<y[1]:
#						if rangeZ[0]>= z[0] and rangeZ[1] < z[1]:
#							esseRangeEstaAceso = aceso
#			if esseRangeEstaAceso:
#				resposta += ((rangeZ[1] - rangeZ[0])*
#						(rangeY[1] - rangeY[0])*
#						(rangeX[1] - rangeX[0]))
#print(resposta)
