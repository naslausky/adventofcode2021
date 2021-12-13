# Desafio do dia 13/12/2021:
#a) Receber uma lista de pontos em uma folha e um eixo para dobrar essa folha. Calcular quantos pontos são vistos após a dobra.
#b) Após todas as dobras, calcular quais letras são formadas com a sobreposição dos pontos.

with open('input.txt') as file:
	pontos, dobras  = file.read().split('\n\n')
	pontos = pontos.splitlines()
	dobras = dobras.splitlines()
	dobrasFormatadas = []
	for dobra in dobras:
		eixo,coordenada = dobra.split()[2].split('=')
		coordenada = int(coordenada)
		dobrasFormatadas.append((eixo,coordenada))
	dobras = dobrasFormatadas
	folha = {}
	for ponto in pontos:
		x,y = ponto.split(',')
		coordenada = (int(x),int(y))
		folha[coordenada] = True

for indice, dobra in enumerate(dobras):
	eixo, coordenada = dobra
	if eixo == 'x':
		dimensao = 0
	else:
		dimensao = 1
	pontosMaiores = [ponto for ponto, valor in folha.items() # Obtém os pontos com coordenada maior do que a informada.
				if ponto[dimensao] > coordenada 
				and valor] # Não faz para os que já foram apagados.
	for ponto in pontosMaiores:
		if dimensao == 0:
			pontoEspelhado = (2 * coordenada - ponto[0], ponto[1])
		else:
			pontoEspelhado = (ponto[0], 2 * coordenada - ponto[1])
		folha[pontoEspelhado] = True
		folha[ponto] = False # Desconsidera o ponto na coordenada antiga.
	if not indice: # Para a parte 1 apenas a primeira dobra é considerada:
		quantidadeDePontos = sum(1 for ponto,valor in folha.items() if valor)
		print('Quantidade de pontos visíveis após a primeira dobra:', quantidadeDePontos)
# Parte 2: 
maiorX = max(ponto[0] for ponto, valor in folha.items() if valor) # Checa a maior coordenada que ainda possui ponto visível.
maiorY = max(ponto[1] for ponto, valor in folha.items() if valor)
for indiceLinha in range(maiorY+1):
	pontosDestaLinha = [ponto for ponto,valor in folha.items() if ponto[1] == indiceLinha and valor]
	linha = ''
	for indiceColuna in range(maiorX+1):
		linha += '#' if folha.get((indiceColuna,indiceLinha),False) else ' '
	print(linha)
