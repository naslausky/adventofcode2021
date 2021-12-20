# Desafio do dia 20/12/2021:
# Receber um mapa de booleanos infinito e uma regra de transformação, que transforma cada coordenada baseado no valor das 9 coordenadas ao redor.
#a) Efetuar a transformação duas vezes e dizer quantas coordenadas verdadeiras existem.
#b) Idem porém para cinquenta vezes.

with open('input.txt') as file:
	regra, linhaImagem = file.read().split('\n\n')
	linhas = linhaImagem.splitlines()
	mapa = {} # Mapa com o estado atual da imagem.
	for indiceLinha, linha in enumerate(linhas):
		for indiceCaracter, caracter in enumerate(linha): 
			mapa[(indiceCaracter, indiceLinha)] = caracter

valorPadrao = '.' # Comeca com todos apagados. É necessário pois a transformação diz que 9 pixels apagados gera um acesso, e vice-versa.
for indiceTransformacao in range(50):
	novoMapa = {}
	
	area = []
	for dimensao in range(2): # Obtém as coordenadas mínima e máxima de cada eixo:
		minimo = min(coord[dimensao] for coord in mapa) # Para podermos percorrer o mapa infinito apenas onde é necessário.
		maximo = max(coord[dimensao] for coord in mapa)
		area.append((minimo,maximo))
	
	for indiceLinha in range(area[0][0]-1, area[0][1]+2): # Como os pixels ao redor influenciam, uma camada além da borda também precisa ser considerada.
		for indiceCaracter in range(area[1][0]-1, area[1][1]+2): #Para todos as coordenadas presentes no mapa, mais essa camada externa:
			string3x3 = ''
			for dy in range(-1,2):
				for dx in range(-1,2):
					chave = (indiceCaracter + dx, indiceLinha + dy)
					string3x3 += mapa.get(chave, valorPadrao)
			string3x3 = string3x3.replace('#','1').replace('.','0')
			numeroBinario = int(string3x3, 2)
			novoMapa[(indiceCaracter, indiceLinha)] = regra[numeroBinario]
	if valorPadrao == '.': # Valor padrão é o valor para as coordenadas não presentes no mapa, visto que é infinito.
		valorPadrao = regra[0]  # Se todas as coordenadas forem '.', representa o número 0 em binário.
	else:
		valorPadrao = regra[-1] # Se todas as coordenadas forem '#', representa o número 511 (ou último).
	mapa = novoMapa # Atualiza o mapa após a transformação.
	if indiceTransformacao == 1:
		print('Número de pixels acesos após 2 iterações:', sum(1 for valor in mapa.values() if valor == '#'))
print('Número de pixels acesos após 50 iterações:', sum(1 for valor in mapa.values() if valor == '#'))
