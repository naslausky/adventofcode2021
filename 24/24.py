# Desafio do dia 24/12/2021:
# a) Receber uma lista de instruções de uma ALU e calcular qual a maior entrada que deixa 0 em um registrador ao final das instruções.
# b) Idem porém calcular a menor entrada.

listaBlocosInstrucoes = [] # Lista em que cada elemento é uma lista com os comandos originais, divididos a cada comando de input. Cada sublista não contém nenhuma instrução de input.

with open('input.txt') as file:
	instrucoes = file.read().splitlines()
	blocoAtual = []
	for instrucao in instrucoes:
		comando = instrucao.split()[0]
		if comando == 'inp' :
			if blocoAtual: # Só precisa disso para a primeira linha.
				listaBlocosInstrucoes.append(blocoAtual)
				blocoAtual = []
		else:
			comando, destino, origem = instrucao.split()
			blocoAtual.append((comando, destino, origem))
	listaBlocosInstrucoes.append(blocoAtual)

def seguirInstrucoes(listaInstrucoes, ZAnterior, WDigitado): # Função que retorna o valor do registrador Z após seguir o bloco de instrucoes dado.
	registradores = {'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0}
	registradores['z'] = ZAnterior
	registradores['w'] = WDigitado

	for instrucao in listaInstrucoes:
		comando, destino, origem = instrucao
		valorDestino = registradores[destino]
		resultado = 99999
		
		if origem in 'wxyz':
			valorOrigem = registradores[origem]
		else:
			valorOrigem = int(origem)

		if comando == 'add':
			resultado = valorOrigem + valorDestino

		elif comando == 'mul':
			resultado = valorOrigem * valorDestino

		elif comando == 'div':
			resultado = int(valorDestino / valorOrigem)

		elif comando == 'mod':
			resultado = valorDestino % valorOrigem

		elif comando == 'eql':
			resultado = 1 if valorDestino == valorOrigem else 0

		registradores[destino] = resultado

	return registradores['z']


valoresDeZASeremTestados = [(0,'')] # Lista de valores de Z.

for blocoInstrucoes in listaBlocosInstrucoes:
	proximosValoresDeZ = {} #Dicionário que relaciona os valores de Z a tupla que representa ele.
	for zAnterior, digitadoAteAgora in valoresDeZASeremTestados:
		for proximoDigito in range(1, 10):
			ZSeguinte = seguirInstrucoes(blocoInstrucoes, zAnterior, proximoDigito)
			digitadoSeguinte = digitadoAteAgora + str(proximoDigito)
			if ZSeguinte in proximosValoresDeZ:
				_, valorConhecido = proximosValoresDeZ[ZSeguinte]
				if int(valorConhecido) > int(digitadoSeguinte):
					proximosValoresDeZ[ZSeguinte] = (ZSeguinte, digitadoSeguinte)
			else:
				proximosValoresDeZ[ZSeguinte] = (ZSeguinte, digitadoSeguinte)
	listaProximoEstado = list(proximosValoresDeZ.values())
	print('Próximos Valores A Serem Testados:', len(listaProximoEstado))
	valoresDeZASeremTestados = listaProximoEstado

print([x for x in valoresDeZASeremTestados if x[0] == 0])
