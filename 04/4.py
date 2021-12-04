# Desafio do dia 04/12/2021:
#a) Dado uma série de cartelas de bingo, e os números sorteados, descobrir qual é a cartela vencedora e calcular sua pontuação.
#b) Idem, porém para a última cartela vencedora.

with open('input.txt') as file:
	conteudo = file.read().split('\n\n')
	numerosSorteados = conteudo[0].splitlines()[0]
	numerosSorteados = list(map(int,numerosSorteados.split(',')))
	cartelasString = conteudo[1:]
	cartelas = []
	for cartela in cartelasString:
		linhasCartela = cartela.splitlines()
		numerosDessaCartela = []
		for linha in linhasCartela:
			numerosDessaCartela.extend(linha.split())
		numerosDessaCartela = list(map(int,numerosDessaCartela))
		cartelas.append(tuple(numerosDessaCartela))

numeroDeLinhas = int(len(numerosDessaCartela)**0.5) #Grid 5x5
dicAcertos = {x:[] for x in cartelas} #Dicionário que relaciona uma cartela aos seus números já acertados.
cartelasQueJaBateram = set() #Uma cartela que já bateu vai continuar "batendo" em sorteios subsequentes, diminuindo sua própria pontuação. 
pontuacaoPrimeiraCartelaVencedora = 0
pontuacaoUltimaCartelaVencedora = 0
for sorteio in numerosSorteados:
	for cartela, acertos in dicAcertos.items(): #Marca o número em todas as cartelas:
		if sorteio in cartela:
			acertos.append(cartela.index(sorteio))
		for indice1 in range(numeroDeLinhas): #Verifica se a cartela bateu:
			contemTodosOsElementosDessaLinha = True
			contemTodosOsElementosDessaColuna = True
			for indice2 in range(numeroDeLinhas):
				if (indice1*numeroDeLinhas + indice2) not in acertos:
					contemTodosOsElementosDessaLinha = False
				if (indice2*numeroDeLinhas + indice1) not in acertos:
					contemTodosOsElementosDessaColuna = False
			if contemTodosOsElementosDessaLinha or contemTodosOsElementosDessaColuna:
				somaDosNumerosNaoMarcados = sum([numero for indice, numero in enumerate(cartela) if indice not in acertos])
				pontuacaoDessaCartela = somaDosNumerosNaoMarcados * sorteio
				if not pontuacaoPrimeiraCartelaVencedora:
					pontuacaoPrimeiraCartelaVencedora = pontuacaoDessaCartela
				if cartela not in cartelasQueJaBateram:
					pontuacaoUltimaCartelaVencedora = pontuacaoDessaCartela
					cartelasQueJaBateram.add(cartela)

print("Pontuação da cartela que fez bingo primeiro:", pontuacaoPrimeiraCartelaVencedora)
print("Pontuação da cartela que fez bingo por último:", pontuacaoUltimaCartelaVencedora)
