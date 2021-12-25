#Desafio do dia 25/12/2021:
#a) Receber uma matriz de ., > e <. Onde cada caracter vai pro lado que está apontando, se estiver vago.
#   Calcular após quantos passos a matriz se estabiliza.
with open('input.txt') as file:
	linhas = file.read().splitlines()
	mapa = {}
	numeroDeLinhas = len(linhas)
	numeroDeColunas = len(linhas[0])
	for indiceLinha, linha in enumerate(linhas):
		for indiceCaracter, caracter in enumerate(linha):
			if caracter != '.':
				mapa[(indiceCaracter,indiceLinha)] = caracter
numeroDePassos = 0
mudouAlgo = True
while(mudouAlgo):
	mudouAlgo = False
	peixesParaDireita = {chave : valor for chave, valor in mapa.items() if valor == '>'}
	chavesARemover = []
	for coordenada in peixesParaDireita:
		coordenadaADireita = ((coordenada[0]+1)%numeroDeColunas, (coordenada[1])%numeroDeLinhas)
		if mapa.get(coordenadaADireita, '.') == '.':
			chavesARemover.append(coordenada)
			mapa[coordenadaADireita] = '>'
	for chave in chavesARemover:
		mudouAlgo = True
		mapa.pop(chave)
	peixesParaBaixo = {chave : valor for chave, valor in mapa.items() if valor == 'v'}
	chavesARemover = []
	for coordenada in peixesParaBaixo:
		coordenadaAbaixo = ((coordenada[0])%numeroDeColunas, (coordenada[1]+1)%numeroDeLinhas)
		if mapa.get(coordenadaAbaixo, '.') == '.':
			chavesARemover.append(coordenada)
			mapa[coordenadaAbaixo] = 'v'
	for chave in chavesARemover:
		mudouAlgo = True
		mapa.pop(chave)
	numeroDePassos+=1
print('Número de passos necessários para os peixes estabilizarem:', numeroDePassos)


