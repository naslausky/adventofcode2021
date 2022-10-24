# Desafio do dia 24/12/2021:
# a) Receber uma lista de instruções de uma ALU e calcular qual a maior entrada que deixa 0 em um registrador ao final das instruções.
# b) Idem porém calcular a menor entrada.
# Atenção: Esta implementação requer um tempo e memória grandes (~25min e 2,5GB).

listaBlocosInstrucoes = [] # Lista em que cada elemento é uma lista com os comandos originais, divididos a cada comando de input. Cada sublista não contém nenhuma instrução de input.

with open('input.txt') as file:
	instrucoes = file.read().splitlines()
	blocoAtual = []
	for instrucao in instrucoes:
		comando = instrucao.split()[0]
		if comando == 'inp' :
			if blocoAtual: # Para a primeira linha sendo um input não adicionar um bloco vazio.
				listaBlocosInstrucoes.append(blocoAtual)
				blocoAtual = []
		else:
			comando, destino, origem = instrucao.split()
			blocoAtual.append((comando, destino, origem))
	listaBlocosInstrucoes.append(blocoAtual)

def seguirInstrucoes(listaInstrucoes, ZAnterior, WDigitado): # Função que retorna o valor do registrador Z após seguir o bloco de instruções dado e o W inserido.
	registradores = {'x' : 0, 'y' : 0, 'z' : ZAnterior, 'w' : WDigitado}
	# Após analisar meu input verifiquei que a cada bloco de instruções o Y e o X não fazem diferença para cada bloco de instruções. 
	for instrucao in listaInstrucoes:
		comando, destino, origem = instrucao
		valorDestino = registradores[destino]

		if origem in 'wxyz': # Verifica se a origem é um número fixo ou o oriundo de um registrador.
			valorOrigem = registradores[origem]
		else:
			valorOrigem = int(origem)

		resultado = None	
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

valoresDeZASeremTestados = [(0, 0, 0)] 
# Lista de valores de Z. Cada elemento é uma tupla que contém o valor atual de Z e os (maior e menor) números digitados para obtê-lo.
# Essa implementação é uma brute-force que se baseia na descoberta que todos os blocos de códigos não utilizam os valores anteriores de X, Y ou W. Pela quantidade de números salvos, requer bastante tempo e memória (~25 min e um máximo de 2,5GB)
for blocoInstrucoes in listaBlocosInstrucoes:
	proximosValoresDeZ = {} # Dicionário que relaciona os valores de Z a tupla que representa ele. 
	# Usado para caso dois valores gerem o mesmo valor Z, salvar só os com menor e maior códigos.
	for zAnterior, maiorDigitadoAteAgora, menorDigitadoAteAgora in valoresDeZASeremTestados:
		for proximoDigito in range(1, 10): # Para cada possibilidade de dígito a ser inserido.
			ZSeguinte = seguirInstrucoes(blocoInstrucoes, zAnterior, proximoDigito)
			maiorDigitadoSeguinte = maiorDigitadoAteAgora * 10 + proximoDigito
			menorDigitadoSeguinte = menorDigitadoAteAgora * 10 + proximoDigito
			_, maiorValorConhecido, menorValorConhecido = proximosValoresDeZ.get(ZSeguinte, (0, 0, 10**9))
			proximosValoresDeZ[ZSeguinte] = (ZSeguinte, 
											max(maiorValorConhecido, maiorDigitadoSeguinte),
											min(menorValorConhecido, menorDigitadoSeguinte))
	valoresDeZASeremTestados = list(proximosValoresDeZ.values())
resposta = [tuplaCodigos for tuplaCodigos in valoresDeZASeremTestados if x[0] == 0][0]
print('O maior valor válido a ser inserido é:', resposta[1])
print('O menor valor válido a ser inserido é:', resposta[2])
