with open('input.txt') as file:
	linhas = file.read().splitlines()
	numeroDeLinhas = len(linhas)
	numeroDeColunas = len(linhas[0])
	mapa = {}
	for indiceLinha, linha in enumerate(linhas):
		for indiceNumero, numero in enumerate(linha):
			coordenada = (indiceLinha, indiceNumero)
			mapa[coordenada] = int(numero)

menorResposta = None
gabarito = {}
def menorRiscoAteOFim(coordenadaAtual, riscoAteAqui):
	global menorResposta
	if menorResposta and menorResposta < riscoAteAqui:
		return riscoAteAqui

	parametros = (coordenadaAtual, riscoAteAqui)
	if parametros in gabarito:
		return gabarito[parametros]

	if coordenadaAtual == (numeroDeLinhas-1, numeroDeColunas-1): #Já chegou
		menorResposta = riscoAteAqui + mapa[coordenadaAtual]
		return riscoAteAqui + mapa[coordenadaAtual]

	caminhos = ((0,1),(1,0) )#  ,(-1,0),(0,-1))
	riscosPossiveis = []
	for caminho in caminhos:
		proximaCoordenada = (coordenadaAtual[0]+caminho[0], coordenadaAtual[1]+caminho[1])
		if proximaCoordenada in mapa:
			riscosPossiveis.append(menorRiscoAteOFim(proximaCoordenada,
						 riscoAteAqui+mapa[proximaCoordenada]))
	if riscosPossiveis:
		resultado = min(riscosPossiveis) 
		gabarito[parametros] = resultado
		return resultado
	else:
		return None

print(menorRiscoAteOFim((0,0),0))
	
