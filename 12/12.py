with open('input.txt') as file:
	linhas = file.read().splitlines()
	conexoes = {}
	for linha in linhas:
		origem,destino = linha.split('-')
		if origem in conexoes:
			conexoes[origem].add(destino)
		else:
			conexoes[origem] = {destino}
		if destino in conexoes:
			conexoes[destino].add(origem)
		else:
			conexoes[destino] = {origem}

def numeroDeCaminhosAteOFinal(rotaAteAqui, parte2 = False):
	noAtual = rotaAteAqui[-1]
	resposta = 0
	cavernasPequenasAteAgora = [caverna for caverna in rotaAteAqui 
					if caverna.islower()]
	existeCavernaDuplicada = any(cavernasPequenasAteAgora.count(cave)>1 # Parte 2: Verifica se alguma caverna pequena já foi passada duas vezes.
					for cave in cavernasPequenasAteAgora)
	for conexao in conexoes[noAtual]:
		if conexao == 'end':
			resposta += 1
			continue
		if parte2: # Uma conexão pequena pode ser passada duas vezes se outra já não tiver feito isso.
			if conexao == 'start':
				continue
			if conexao.islower() and existeCavernaDuplicada and conexao in rotaAteAqui:
				continue
		elif conexao.islower() and conexao in rotaAteAqui: # Uma conexão pequena só pode ser passada uma vez na parte 1.
			continue
		rotaAtualizada = rotaAteAqui + [conexao]
		resposta += numeroDeCaminhosAteOFinal(rotaAtualizada, parte2)
	return resposta

print('Número de formas de chegar ao final passando uma vez por cada caverna pequena:', numeroDeCaminhosAteOFinal(['start']))
print('Número de formas de chegar ao final passando duas vezes em uma caverna pequena:', numeroDeCaminhosAteOFinal(['start'], True))
