# Desafio do dia 22/12/2021
# a)
# b)
import copy
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

def inserirInstrucao(intervalos, aceso, dicDestino):
	ultimoNivel = len(intervalos) == 1
	intervaloDaVez = intervalos[0]
	indiceInferior, indiceSuperior = intervaloDaVez
	dicConsulta = copy.deepcopy(dicDestino)
	for intervalo, valor in dicConsulta.items():
		if indiceInferior in range(*intervalo):
			intervaloAQuebrar = intervalo
			if indiceInferior == intervaloAQuebrar[0]:
				continue
			novoIntervalo1 = (intervaloAQuebrar[0], indiceInferior)
			novoIntervalo2 = (indiceInferior, intervaloAQuebrar[1])
			dicDestino.pop(intervalo, 0)
			dicDestino[novoIntervalo1] = valor
			dicDestino[novoIntervalo2] = valor
	dicConsulta = copy.deepcopy(dicDestino)
	for intervalo, valor in dicConsulta.items():
		if indiceSuperior in range(*intervalo):
			intervaloAQuebrar = intervalo
			if indiceSuperior == intervaloAQuebrar[1] - 1:
				continue
			novoIntervalo1 = (intervaloAQuebrar[0], indiceSuperior + 1)
			novoIntervalo2 = (indiceSuperior + 1, intervaloAQuebrar[1])
			dicDestino.pop(intervalo, 0)
			dicDestino[novoIntervalo1] = valor
			dicDestino[novoIntervalo2] = valor
	if not any ([indiceInferior in range(*intervalo) for intervalo in dicDestino]):
		intervalosPresentesMaiores = [x[0] for x in dicDestino if x[0] > indiceInferior]
		if not intervalosPresentesMaiores:
			novoSuperior = indiceSuperior + 1
		else:
			minimoParcial = min(intervalosPresentesMaiores)
			novoSuperior = min(minimoParcial, indiceSuperior+1)
		novoIntervaloACriar = (indiceInferior, novoSuperior)
		valor = False if ultimoNivel else {}
		dicDestino[novoIntervaloACriar] = valor
	if not any ([indiceSuperior in range(*intervalo) for intervalo in dicDestino]):
		intervalosPresentesMenores = [x[1] for x in dicDestino if x[1] < indiceSuperior]
		if not intervalosPresentesMenores:
			novoInferior = indiceInferior
		else:
			maximoParcial = max(intervalosPresentesMenores)
			novoInferior = max(maximoParcial, indiceInferior)
		novoIntervaloACriar = (novoInferior, indiceSuperior+1)
		valor = False if ultimoNivel else {}
		dicDestino[novoIntervaloACriar] = valor
	comeco = intervaloDaVez[0]
	while comeco < intervaloDaVez[1]:
		intervalo = [x for x in dicDestino if x[0] == comeco] # Presumo que sempre vai ter
		if not intervalo:
			#precisa inserir um novo intervalo entre 2 intervalos quebrados:
			inferior = comeco
			superior = min([x[0] for x in dicDestino if x[0] > inferior])
			intervalo = (inferior,superior)
			valor = False if ultimoNivel else {}
			dicDestino[(inferior,superior)] = valor
		else:
			intervalo = intervalo[0]
		if ultimoNivel:
			dicDestino[intervalo] = aceso
		else:
			inserirInstrucao(intervalos[1:], aceso, dicDestino[intervalo])
		comeco = intervalo[1]
dicionarioCubos = {}
for intervalo, ligado in instrucoes:
	inserirInstrucao(intervalo, ligado, dicionarioCubos)
#Contabilizando:
print(dicionarioCubos)
valorTotal = 0
for rangeX, dicionarioFilho1 in dicionarioCubos.items():
	print('rangeX:',rangeX)
	valor1 = 0
	for rangeY,dicionarioFilho2 in dicionarioFilho1.items():
		print('rangeY',rangeY)
		valor2 = 0
		for rangeZ, booleano in dicionarioFilho2.items():
			print('rangeZ',rangeZ)
			print('aceso:',booleano)
			if booleano:
				valor2 += rangeZ[1] - rangeZ[0]
		valor1 += valor2
	valorTotal += valor1
print(valorTotal)
