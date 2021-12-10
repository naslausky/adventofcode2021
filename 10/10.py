# Desafio do dia 10/12/2021:
#a) Receber uma série de strings e para cada uma achar o primeiro caracter que não fecha corretamente.
#b) Calcular os caracteres faltantes em cada linha.

with open('input.txt') as file:
	linhas = file.read().splitlines()
mapaFechamento = {'(':')', '[':']', '{':'}', '<':'>'} # Dicionário que relaciona cada caracter ao seu outro caracter de fechamento.
mapaPontuacao = {')':3, ']':57, '}':1197, '>':25137} # Dicionário com a pontuação para a parte 1.
mapaPontuacaoCompletar = {'(':1, '[':2, '{':3, '<':4} # Dicionário com a pontuação para a parte 2.

somaDosErros = 0 # Resposta da parte 1
pontuacoesCaracteresFaltantes = [] # Resposta da parte 2
for linha in linhas:
	linhaCorrompida = False
	listaCaracteres= []
	for caracter in linha:
		if caracter in '([{<':
			listaCaracteres.append(caracter)
		else:
			if mapaFechamento[listaCaracteres.pop()] != caracter:
				somaDosErros+=mapaPontuacao[caracter]
				linhaCorrompida = True # O certo era parar de varrer a linha por aqui, mas pelo visto nesse input não precisa.
	if not linhaCorrompida: # Parte 2: ignorar as linhas corrompidas.
		pontuacaoCaracteresRestantes = 0 # Pontuação dessa linha.
		for caracter in reversed(listaCaracteres):
			pontuacaoCaracteresRestantes *= 5
			pontuacaoCaracteresRestantes += mapaPontuacaoCompletar[caracter]
		pontuacoesCaracteresFaltantes.append(pontuacaoCaracteresRestantes)
print("A soma da pontuação de todas as linhas corrompidas é:", somaDosErros)

# Parte 2:
pontuacoesCaracteresFaltantes.sort()
indiceElementoCentral = len(pontuacoesCaracteresFaltantes) // 2
elementoCentral = pontuacoesCaracteresFaltantes[indiceElementoCentral]
print("A pontuação mediana das linhas incompletas é:", elementoCentral)
