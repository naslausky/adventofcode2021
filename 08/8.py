# Desafio do dia 08/12/2021:
#a) Recebido uma lista de segmentos acesos descobrir quantos digitos 1,4,7 ou 8 existem.
#b) Dada a mesma lista, descobrir qual valor cada display exibe e calcular a soma.

with open('input.txt') as file:
	linhas = file.read().splitlines()

quantidadeDeDigitos1748 = 0
somaDosValoresDeTodosOsDisplays = 0
for linha in linhas:
	todosOsDigitos, digitosSaida = linha.split(' | ')
	listaDigitos = todosOsDigitos.split()
	listaDigitosSaida = digitosSaida.split()
	quantidadeDeSegmentosAcesosParaCadaDigito = [len(x) for x in listaDigitosSaida]
	for qtd in quantidadeDeSegmentosAcesosParaCadaDigito:
		if qtd == 2 or qtd == 4 or qtd == 3 or qtd == 7:
			quantidadeDeDigitos1748 += 1
	#Parte 2:
	listaDosConjuntos = [frozenset(digito) for digito in listaDigitos] #FrozenSet para poder ser usado de chave depois.
	listaDosConjuntosSaida = [frozenset(digito) for digito in listaDigitosSaida]
	gabarito = {} # Dicionário que relaciona o número a seu conjunto de segmentos acesos.
	for conjunto in listaDosConjuntos: # Como o enunciado diz, alguns números são unicamente identificáveis baseado no número de segmentos acesos:
		if len(conjunto) == 2:
			gabarito[1] = conjunto # Só o digito 1 utiliza 2 segmentos.
		elif len(conjunto) == 3:
			gabarito[7] = conjunto # Só o digito 7 utiliza 3 segmentos.
		elif len(conjunto) == 4:
			gabarito[4] = conjunto # Só o digito 4 utiliza 4 segmentos.
		elif len(conjunto) == 7:
			gabarito[8] = conjunto # Só o digito 8 utiliza 7 segmentos.

	for conjunto in listaDosConjuntos:# Descobre os que faltam. São os que possuem 5 e 6 segmentos acesos.
		if len(conjunto) == 5 : # Dos dígitos que tem 5 segmentos acesos (2,3,5):
			if conjunto.issuperset(gabarito[7]): # O dígito 3 é o único que contém o dígito 7 todo:
				gabarito[3] = conjunto
			elif len(conjunto - gabarito[4]) == 3: # O dígito 2 subtraído do dígito 4 sobram 3 segmentos.
				gabarito[2] = conjunto
			else: # O dígito 5 subtraído do dígito 4 sobram 2 segmentos.
				gabarito[5] = conjunto
		if len(conjunto) == 6: # Dos que tem 6 segmentos acesos (0,6,9):
			if conjunto.union(gabarito[1]) == gabarito[8]: # O dígito 6 é o único que somado ao dígito 1 dá o dígito 8.
				gabarito[6] = conjunto
			elif len(conjunto-gabarito[4]) == 3: # O dígito 0 é o único que, além do 6, quando subtraído o dígito 4 sobram 3 segmentos.
				gabarito[0] = conjunto # (Por isso é importante ele vir no else depois do 6. Talvez tenha outra forma que ignore a ordem.)
			else: # O dígito 9 é o único que ao diminuir o dígito 4 sobram 2 segmentos.
				gabarito[9] = conjunto

	gabaritoInverso = {valor:chave for chave, valor in gabarito.items()} # Dicionário inverso para poder saber o número baseado nos segmentos acesos.
	valorDesteDisplay = (gabaritoInverso[listaDosConjuntosSaida[0]] * (10**3) +
				gabaritoInverso[listaDosConjuntosSaida[1]] * (10**2) +
				gabaritoInverso[listaDosConjuntosSaida[2]] * (10**1) +
				gabaritoInverso[listaDosConjuntosSaida[3]] * (10**0))
	somaDosValoresDeTodosOsDisplays += valorDesteDisplay
print('Quantidade de dígitos 1,4,7 e 8:', quantidadeDeDigitos1748)
print('Soma dos valores de todos os displays:', somaDosValoresDeTodosOsDisplays)
