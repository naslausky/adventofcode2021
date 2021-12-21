# Desafio do dia 21/12/2021:
#a) Receber duas posições iniciais em um jogo com um tabuleiro circular com 10 casas. Cada jogador joga um dado três vezes e anda a soma dos valores sorteados. Calcular quantos pontos o jogador que perdeu fez e quantos lances de dado foram necessários.
#b) Calcular quantas vitórias um jogador pode ter considerando todas as possibilidades de sorteio de dado com resultados de 1 a 3.
with open('input.txt') as file:
	linhas = file.read().splitlines()
	posicoes = [] # Lista de posicoes dos jogadores.
	pontuacoes = []
	for linha in linhas:
		posicoes.append(int(linha.split()[-1]))
		pontuacoes.append(0)
	posicoesOriginais = posicoes[:] # Para parte 2.

numeroDeSorteios = 0
sorteioDoDado = 0 # Valor que representa o valor que o dado vai sortear, quando determinístico.
indicePlayerDaVez = 0
while not any(True for pontuacao in pontuacoes if pontuacao >= 1000):
	somaSorteioDesteTurno = 0
	for _ in range(3):
		sorteioDoDado = (sorteioDoDado % 100) + 1
		somaSorteioDesteTurno += sorteioDoDado
		numeroDeSorteios += 1
	posicoes[indicePlayerDaVez] += somaSorteioDesteTurno
	posicoes[indicePlayerDaVez] = 	(10 
					if posicoes[indicePlayerDaVez] % 10 == 0 
					else posicoes[indicePlayerDaVez] % 10)
	pontuacoes[indicePlayerDaVez] += posicoes[indicePlayerDaVez]
	indicePlayerDaVez = (indicePlayerDaVez + 1) % len(pontuacoes)
print('Com um dado determinístico, o jogador com menor pontuação vezes o número de lances é:', min(pontuacoes)*numeroDeSorteios)

# Parte 2:
gabarito = {} # Utilizado para não precisar chamar uma função novamente caso uma dada entrada já tenha sido calculada.
def jogarUmaRodada(posicoes, pontuacoes, jogadorDaVez):
	chave = (tuple(posicoes),tuple(pontuacoes), jogadorDaVez)
	if chave in gabarito: # Não precisa calcular novamente.
		return gabarito[chave]
	if any(pontuacao >= 21 for pontuacao in pontuacoes):
		return [1 if pontuacao >= 21 else 0 for pontuacao in pontuacoes]

	vitoriasDaquiEmDiante = [0 for _ in posicoes]
	for valorDado1 in range(1,4):
		for valorDado2 in range(1,4):
			for valorDado3 in range(1,4):
				soma = valorDado1 + valorDado2 + valorDado3
				posicoesProximaRodada = posicoes[:]
				posicoesProximaRodada[jogadorDaVez] += soma
				posicoesProximaRodada[jogadorDaVez] = 	(10 
									if posicoesProximaRodada[jogadorDaVez] % 10 == 0 
									else posicoesProximaRodada[jogadorDaVez] % 10)
				pontuacoesProximaRodada = pontuacoes[:]
				pontuacoesProximaRodada[jogadorDaVez] += posicoesProximaRodada[jogadorDaVez]
				vitorias = jogarUmaRodada(posicoesProximaRodada, pontuacoesProximaRodada,(jogadorDaVez+1)%2)
				for indice in range(len(vitorias)):
					vitoriasDaquiEmDiante[indice] += vitorias[indice]
	gabarito[chave] = vitoriasDaquiEmDiante # Salva para não precisar calcular adiante.
	return vitoriasDaquiEmDiante

pontuacoes =  [0 for _ in posicoes]
posicoes = posicoesOriginais
print('Calculando todas as possibilidades, o jogador que mais pode ganhar é:', max(jogarUmaRodada(posicoes, pontuacoes, 0)))
