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

def inserirInstrucao(intervalos, aceso, dicDestino):
	ultimoNivel = len(intervalos) == 1
	intervaloDaVez = intervalos[0]
	indiceInferior, indiceSuperior = intervaloDaVez
	# Indice inferior:
	contemEsseIndice = [intervalo for intervalo in dicDestino if indiceInferior in range(*intervalo)]
	if contemEsseIndice: #Algum intervalo no dicionário já contem esse índice inferior. Quebrar.
		intervaloAQuebrar = contemEsseIndice[0]
		valor = dicDestino[intervaloAQuebrar]
		if indiceInferior != intervaloAQuebrar[0]:
			novoIntervalo1 = (intervaloAQuebrar[0], indiceInferior)
			novoIntervalo2 = (indiceInferior, intervaloAQuebrar[1])
			dicDestino.pop(intervaloAQuebrar, 0) #Ou del
			dicDestino[novoIntervalo1] = valor
			dicDestino[novoIntervalo2] = valor
	else: # Nenhum intervalo no dicionário contém esse índice inferior. Adicionar
		intervalosPresentesMaiores = [x[0] for x in dicDestino if x[0] > indiceInferior]
		novoSuperior = indiceSuperior + 1
		if intervalosPresentesMaiores:
			minimoParcial = min(intervalosPresentesMaiores)
			novoSuperior = min(minimoParcial, indiceSuperior+1)
		novoIntervaloACriar = (indiceInferior, novoSuperior)
		valor = False if ultimoNivel else {}
		dicDestino[novoIntervaloACriar] = valor
	#Índice Superior:
	contemEsseIndice = [intervalo for intervalo in dicDestino if indiceSuperior in range(*intervalo)]
	if contemEsseIndice:
		intervaloAQuebrar = contemEsseIndice[0]
		try:
			valor = dicDestino[intervaloAQuebrar]
		except:
			print(contemEsseIndice)
			exit()
		if indiceSuperior != (intervaloAQuebrar[1] - 1): 

			novoIntervalo1 = (intervaloAQuebrar[0], indiceSuperior + 1)
			novoIntervalo2 = (indiceSuperior + 1, intervaloAQuebrar[1])
			dicDestino.pop(intervaloAQuebrar, 0)
			dicDestino[novoIntervalo1] = valor
			dicDestino[novoIntervalo2] = valor
	else:
		intervalosPresentesMenores = [x[1] for x in dicDestino if x[1] <= indiceSuperior]
		novoInferior = indiceInferior
		if intervalosPresentesMenores:
			maximoParcial = max(intervalosPresentesMenores)
			novoInferior = max(maximoParcial, indiceInferior)
		novoIntervaloACriar = (novoInferior, indiceSuperior+1)
		valor = False if ultimoNivel else {}
		dicDestino[novoIntervaloACriar] = valor

	comeco = intervaloDaVez[0] 
	while comeco < intervaloDaVez[1]:
		intervalo = [x for x in dicDestino if x[0] == comeco]
		if not intervalo:
			#precisa inserir um novo intervalo entre 2 intervalos quebrados:
			inferior = comeco
			superior = min([x[0] for x in dicDestino if x[0] > inferior])
			intervalo = (inferior,superior)
			valor = False if ultimoNivel else {}
			dicDestino[intervalo] = valor
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
pretty(dicionarioCubos)
valorTotal = 0
for rangeX, dicionarioFilho1 in dicionarioCubos.items():
	for rangeY, dicionarioFilho2 in dicionarioFilho1.items():
		for rangeZ, booleano in dicionarioFilho2.items():
			if booleano:
				valorTotal += ((rangeZ[1] - rangeZ[0])*
						(rangeY[1] - rangeY[0])*
						(rangeX[1] - rangeX[0]))
print(valorTotal)
