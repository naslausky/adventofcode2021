#Desafio do dia 17/12/2021:
#a) Receber uma área destino e calcular a maior altura que um torpedo pode alcançar e ainda passar por ela.
#b) Calcular quantas velocidades iniciais distintas passam pela área destino.
# Esta resolução supõe que a área destino fica a direita e abaixo da posição inicial.
with open('input.txt') as file:
	linha = file.read().splitlines()[0]
	linha = linha.replace('target area: ', '')
	areaDestino = []
	for stringIntervalo in linha.split(', '):
		intervalo = stringIntervalo.split('=')[1].split('..')
		intervalo = list(map(int,intervalo))
		areaDestino.append(intervalo)
velocidadesIniciais = {} # Dicionário que relaciona as velocidades iniciais que alcançam o destino com sua maior altura alcançada.
for x0 in range(1,areaDestino[0][1]+1):
	limiteInferior = areaDestino[1][0] 
	limiteSuperior = 1 - areaDestino[1][0] 
	for y0 in range(limiteInferior, limiteSuperior+1):
		posicaoAtual = [0,0]
		velocidade = [x0,y0]
		maiorAltura = 0
		estaNaAreaDestino = False
		while (not estaNaAreaDestino): # Faz passo a passo:
			for dim in range(2): # Incrementa a posição atual.
				posicaoAtual[dim] += velocidade[dim]
			maiorAltura = max(maiorAltura, posicaoAtual[1])

			estaNaAreaDestino = True # Verifica se está na area destino:
			for dim in range(2):
				if posicaoAtual[dim] not in range(areaDestino[dim][0],
							areaDestino[dim][1]+1):
					estaNaAreaDestino = False

			velocidade[0] -= 1 if velocidade[0] != 0 else 0 # Devido ao atrito com a água.
			velocidade[1] -= 1 # Devido a gravidade.
			if posicaoAtual[1] < areaDestino[1][0]: # Se já tá mais embaixo do que a área destino, podemos tentar outra velocidade inicial:
				break

		if estaNaAreaDestino:
			velocidadesIniciais[(x0,y0)] = maiorAltura
print('Maior altura possível de alcançar:', max(valor for valor in velocidadesIniciais.values()))
print('Número de velocidades iniciais que acertam o alvo:', len(velocidadesIniciais))
