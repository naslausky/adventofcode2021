import math
import copy
with open('input.txt') as file:
	linhasString = file.read().splitlines()
	linhas = list(map(eval,linhasString))
	linhasOriginais = list(map(eval, linhasString))

teste1 = [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]

def explodirSeNecessario(parOriginal, profundidade): #Recursivo, retorna se explodiu
	direita = esquerda = None
	explodiu = False
	substituirAgoraPor0 = False
#	print(profundidade)
	#print('comeco', parOriginal)
	for indice, elemento in enumerate(parOriginal):
		#print('entrou elemento', indice)
		if type(elemento) is list:
			#print('elemento',indice,'é lista:', elemento)
			if type(elemento[0]) is int and type(elemento[1]) is int and not explodiu:
				if profundidade >= 3 : #explodir
#					print('Explodiu agora!', elemento)
					esquerda = elemento[0]
					direita = elemento[1]
					substituirAgoraPor0 = True
					parOriginal[indice] = 0
					explodiu = True
			elif not explodiu: #um dos dois netos é lista: #Talvez substituir por Else
				esquerda, explodiu, direita = explodirSeNecessario(elemento, profundidade+1)
			if explodiu:
#				print('paroriginal', parOriginal)
#				print('explodiu!', elemento)
				if esquerda:
#					print('esquerda', esquerda)
#					print('era pra ser 1', indice)
					if indice == 1:
						if type(parOriginal[0]) is int :
							parOriginal[0]+=esquerda
							esquerda = None
						else:
							incrementarADireita(parOriginal[0], esquerda)
							esquerda = None
				
				if direita:
#					print('direita', direita)
#					print('era pra ser 0', indice)
					if indice == 0:
						if type(parOriginal[1]) is int:
							parOriginal[1] += direita
							direita = None
						else:
							incrementarAEsquerda(parOriginal[1], direita)
							direita = None
				#if substituirAgoraPor0:
				#	parOriginal[indice] = 0
#				print('retornando', esquerda, explodiu, direita)
				return esquerda, explodiu, direita
	return None, False, None
def incrementarADireita (par, numero):
#	print('chamando incrementar a direita')
	if numero is None:
		return
	parAtual = par
#	print('procurando par:', parAtual)
	while type(parAtual[1]) is list:
		parAtual = parAtual[1]
	parAtual[1] += numero

def incrementarAEsquerda (par, numero):
	#print('chamando incrementar a esquerda')
	if numero is None:
		print('Deu None!')
		return 
	parAtual = par
#	print('procurando par:', parAtual)
	while type(parAtual[0]) is list:
		parAtual = parAtual[0]
	parAtual[0]+= numero
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
		if dividiu: #pra não tentar o proximo elemento se for o caso
			return True
teste2 = [[[[[9,8],1],2],3],4]
gabarito2 = [[[[0,9],2],3],4]
teste3 = [7,[6,[5,[4,[3,2]]]]] 
gabarito3 = [7,[6,[5,[7,0]]]]
teste4 = [[6,[5,[4,[3,2]]]],1]
gabarito4 = [[6,[5,[7,0]]],3]
teste5 = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
gabarito5 = [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
teste6 = [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
gabarito6 = [[3,[2,[8,0]]],[9,[5,[7,0]]]]
testes = ((teste2,gabarito2),(teste3,gabarito3),(teste4,gabarito4),(teste5,gabarito5),(teste6,gabarito6))
#print('Testando explosão:')
for teste,gabarito in testes: #testes de explodir
#	print('_______________')
#	print('Anterior: ', teste)
	explodirSeNecessario(teste, 0)
#	print('Resultado:', teste)
#	print('Gabarito :', gabarito)
#print('Testando divisão:')
teste7 = [[[[0,7],4],[15,[0,13]]],[1,1]]
gabarito7 = [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
teste8 = [[[[0,7],4],[[7,8],[0,13]]],[1,1]] 
gabarito8 =[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
testes = ((teste7,gabarito7),(teste8,gabarito8))
for teste,gabarito in testes: #Testes de dividir
#	print('_______________')
#	print('Anterior: ',teste)
	dividirSeNecessario(teste)
#	print('Resultado:', teste)
#	print('Gabarito: ', gabarito)
def somar(atual, proximaLinha):
	#Talvez comecar com uma vazia e dar 2 extends;
	if not atual: #Só para o primeiro caso.
		return proximaLinha
	return [atual, proximaLinha]
#linhas = [[[[[4,3],4],4],[7,[[8,4],9]]], [1,1]]
#[print(x) for x in linhas]
#print('Começando as somas:')
#print('-------------------')
somaAteAgora = []
for linha in linhas:
	somaAteAgora = somar(somaAteAgora, linha)
	#print('NovaLinha adicionada:', somaAteAgora)
	mudouAlgo = True
	while mudouAlgo:
		#print('SomaAtéAgora:', somaAteAgora)
		mudouAlgo = False
		_, explodiu, _ = explodirSeNecessario(somaAteAgora, 0)
		if explodiu:
			#print('Explodiu!', somaAteAgora)
			mudouAlgo = True
			continue
		dividiu = dividirSeNecessario(somaAteAgora)
		if dividiu:
			#print('Dividiu!', somaAteAgora)
			mudouAlgo = True
			continue

#print(somaAteAgora)
def calcularMagnitude(par):
	magnitude = 0
	if type(par[0]) is int:
		magnitude += 3 * par[0]
	else:
		magnitude += 3 * calcularMagnitude(par[0])
	if type(par[1]) is int:
		magnitude += 2 * par[1]
	else:
		magnitude += 2 * calcularMagnitude(par[1])
	return magnitude

#print('Testando soma de magnitude:')
teste1 = [[1,2],[[3,4],5]]
teste2 = [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
teste3 = [[[[1,1],[2,2]],[3,3]],[4,4]]
teste4 = [[[[3,0],[5,3]],[4,4]],[5,5]]
teste5 = [[[[5,0],[7,4]],[5,5]],[6,6]]
teste6 = [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]	
testes = ((teste1,143),(teste2,1384),(teste3,445),(teste4,791),(teste5,1137),(teste6, 3488))
for teste,gabarito in testes:
	pass
#	print('_______________')
#	print('Resultado:', calcularMagnitude(teste))
#	print('Gabarito: ', gabarito)
print('Resposta final:', calcularMagnitude(somaAteAgora))
# Parte 2:
#print()
linhas = linhasOriginais
magnitudeMaxima = 0 
for linha1Original in linhas:
	for linha2Original in linhas:
		linha1 = copy.deepcopy(linha1Original)
		linha2 = copy.deepcopy(linha2Original)
		if linha1 == linha2:
			continue
		soma = somar(linha1,linha2)
		mudouAlgo = True
		while mudouAlgo:
			mudouAlgo = False
			_, explodiu, _ = explodirSeNecessario(soma, 0)
			if explodiu:
				mudouAlgo = True
				continue
			dividiu = dividirSeNecessario(soma)
			if dividiu:
				mudouAlgo = True
				continue
		magnitudeMaxima = max(magnitudeMaxima, calcularMagnitude(soma))
#		if magnitudeMaxima == calcularMagnitude(soma):
#			print('Maximo!',linha1Original, 'com', linha2Original, '->', magnitudeMaxima)
print(magnitudeMaxima)
