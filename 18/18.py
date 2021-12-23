#Desafio do dia 18/12/2021:
#a) Receber uma lista de listas aninhadas e um conjunto de regras de redução. Calcular a soma de todas as listas, onde a cada soma é necessário reduzir o resultado.
#b) Calcular o par de linhas que produz o maior resultado.

import math
import copy
with open('input.txt') as file:
	linhasString = file.read().splitlines()
	linhas = list(map(eval,linhasString))
	linhasOriginais = copy.deepcopy(linhas) # Para a parte 2.

def explodirSeNecessario(parOriginal, profundidade): 
	# Função recursiva, que recebe um par e explode uma vez apenas, se válido.
	# Retorna se explodiu, e dois números para somar a esquerda e a direita, caso não seja possível somar nessa volta.
	# Caso o número já tenha sido somado, seu valor é None.
	direita = esquerda = None
	explodiu = False
	substituirAgoraPor0 = False
	for indice, elemento in enumerate(parOriginal):
		if type(elemento) is list:
			# O elemento anterior pode ter explodido.
			if type(elemento[0]) is int and type(elemento[1]) is int and not explodiu:
				if profundidade >= 3 : # Explodir este elemento.
					esquerda = elemento[0]
					direita = elemento[1]
					substituirAgoraPor0 = True
					parOriginal[indice] = 0
					explodiu = True
			elif not explodiu: # Algum dos netos é lista. Chamar a função novamente:
				esquerda, explodiu, direita = explodirSeNecessario(elemento, profundidade+1)
			if explodiu: # Explodiu. Confere se tem algum resquício para somar pros lados:
				if esquerda:
					if indice == 1:
						if type(parOriginal[0]) is int :
							parOriginal[0]+=esquerda
						else:
							incrementarIndice(parOriginal[0], esquerda, 1)
						esquerda = None
				if direita:
					if indice == 0:
						if type(parOriginal[1]) is int:
							parOriginal[1] += direita
						else:
							incrementarIndice(parOriginal[1], direita, 0)
						direita = None
				return esquerda, explodiu, direita
	return None, False, None # Não explodiu nem há nada para somar.
def incrementarIndice (par, numero, indice): #Função que adiciona um número ao número mais a direita/esquerda..
	parAtual = par
	while type(parAtual[indice]) is list:
		parAtual = parAtual[indice]
	parAtual[indice] += numero
def dividirSeNecessario(parOriginal):
	dividiu = False
	for indice, elemento in enumerate(parOriginal):
		if type(elemento) is int:
			if elemento>=10:
				elementoDividido = [math.floor(elemento/2), math.ceil(elemento/2)]	
				parOriginal[indice] = elementoDividido
				return True
		else:
			dividiu = dividirSeNecessario(elemento)
		if dividiu: #Pra não tentar o proximo elemento se for o caso.
			return True
def somar(atual, proximaLinha): #Função que junta dois pares em um novo par.
	if not atual: #Só para o primeiro caso, quando o par anterior é vazio.
		return proximaLinha
	return [atual, proximaLinha]
def reduzir(linhaAtual): # Função que reduz um par. Aplica explosões e divisões até não poder mais.
	mudouAlgo = True
	while mudouAlgo:
		mudouAlgo = False
		_, explodiu, _ = explodirSeNecessario(linhaAtual, 0)
		if explodiu:
			mudouAlgo = True
			continue
		dividiu = dividirSeNecessario(linhaAtual)
		if dividiu:
			mudouAlgo = True
			continue
def calcularMagnitude(par): # Função que recebe um par e calcula sua pontuação.
	magnitude = 0
	coordenadasValores = ((0,3),(1,2)) # Atribui um valor para cada coordenada.
	for coordenada, valor in coordenadasValores:
		if type(par[coordenada]) is int:
			elemento = par[coordenada]
		else:
			elemento = calcularMagnitude(par[coordenada])
		magnitude += valor * elemento
	return magnitude
# Parte 1:
somaAteAgora = []
for linha in linhas:
	somaAteAgora = somar(somaAteAgora, linha)
	reduzir(somaAteAgora)
print('A magnitude da soma final é:', calcularMagnitude(somaAteAgora))
# Parte 2:
linhas = linhasOriginais
magnitudeMaxima = 0 
for linha1Original in linhas:
	for linha2Original in linhas:
		linha1 = copy.deepcopy(linha1Original)
		linha2 = copy.deepcopy(linha2Original)
		if linha1 == linha2:
			continue
		soma = somar(linha1,linha2)
		reduzir(soma)
		magnitudeMaxima = max(magnitudeMaxima, calcularMagnitude(soma))
print('A maior magnitude obtida com a soma de dois elementos é:', magnitudeMaxima)
