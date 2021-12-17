with open('input.txt') as file:
	linha = file.read().splitlines()[0]
#	linha = 'target area: x=20..30, y=-10..-5'
	linha = linha.replace('target area: ', '')
	areaDestino = []
	for stringIntervalo in linha.split(', '):
		intervalo = stringIntervalo.split('=')[1].split('..')
		intervalo = list(map(int,intervalo))
		areaDestino.append(intervalo)
#print(abs(areaDestino[1][1]-areaDestino[1][0]+1))
#print(areaDestino[1][0])
velocidadesIniciais = {} #Dicionário que relaciona as velocidades iniciais que alcançam o 
for x0 in range(1,areaDestino[0][1]+1):
	y0=areaDestino[1][0] 
	while True: #Laco de incrementar o y0
		posicaoAtual = [0,0]
		velocidade = [x0,y0]
		maiorAltura = 0
		estaNaAreaDestino = False
		while (not estaNaAreaDestino): #Faz 1 passo:
#			print('posicao', posicaoAtual)
#			print('velocidade', velocidade)
			for dim in range(2):
				posicaoAtual[dim] += velocidade[dim]
			maiorAltura = max(maiorAltura, posicaoAtual[1])

			estaNaAreaDestino = True #Verifica se está na area destino:
			for dim in range(2):
				if posicaoAtual[dim] not in range(areaDestino[dim][0],
							areaDestino[dim][1]+1):
					estaNaAreaDestino = False

			velocidade[0] -= 1 if velocidade[0] != 0 else 0
			velocidade[1] -= 1
			#if abs(velocidade[1]) > abs(areaDestino[1][1]-areaDestino[1][0]+1) and velocidade[1]<0:
			if posicaoAtual[1] < areaDestino[1][0]:
				break

		if estaNaAreaDestino:
			velocidadesIniciais[(x0,y0)] = maiorAltura

		if y0 > 300: # Melhorar limite superior
			break
		y0+=1

print(max(valor for valor in velocidadesIniciais.values()))
print(len(velocidadesIniciais))
