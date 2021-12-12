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

def numeroDeCaminhosAteOFinal(rotaAteAqui):
	noAtual = rotaAteAqui[-1]
	resposta = 0
	for conexao in conexoes[noAtual]:
		if conexao.islower() and conexao in rotaAteAqui:
			continue
		if conexao == 'end':
			resposta+=1
		else:
			rotaAtualizada = rotaAteAqui+[conexao]
			resposta += numeroDeCaminhosAteOFinal(rotaAtualizada)
	return resposta

def numeroDeCaminhosAteOFinalParte2(rotaAteAqui):
	noAtual = rotaAteAqui[-1]
	resposta = 0
	cavernasPequenasAteAgora = [caverna for caverna in rotaAteAqui 
					if caverna.islower()]
	existeCavernaDuplicada = any(cavernasPequenasAteAgora.count(cave)>1 
					for cave in cavernasPequenasAteAgora)

	for conexao in conexoes[noAtual]:
		if conexao == 'start':
			continue
		if conexao == 'end':
			#print(rotaAteAqui)
			resposta+=1
			continue
		if conexao.islower():
			if existeCavernaDuplicada:
				if conexao in rotaAteAqui:
					continue
		rotaAtualizada = rotaAteAqui+[conexao]
		resposta += numeroDeCaminhosAteOFinalParte2(rotaAtualizada)
	return resposta
print(numeroDeCaminhosAteOFinalParte2(['start']))
