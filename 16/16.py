# Desafio do dia 16/12/2021:
#a) Receber uma sequência de bits, e uma regra de protocolo, e somar o número de versão de todos pacotes e sub pacotes.
#b) Interpretar o significado de cada pacote, podendo representar operações e calcular o valor do pacote mais externo.

with open('input.txt') as file:
	linha = file.read().splitlines()[0]
	linha = '1' + linha # Para incluir os zeros a esquerda, coloco um bit 1 na frente e depois removo ele.
	numeroHexadecimal = int(linha,16)
	stringEmBinario = bin(numeroHexadecimal)[3:] # Exclui o '0b' e o '1' inicial que eu coloquei acima.

def extrairPrimeirosCaracteres(string, quantidade, decimal = False): # Função que extrai os primeiros N caracteres de uma string, retorna eles e o que sobrou dela.
	valorExtraido = string[:quantidade]
	if decimal:
		valorExtraido = int(valorExtraido, 2)
	return valorExtraido, string[quantidade:]	
	
def gerarPacoteBaseadoNosBits(stringBinaria): # Função recursiva que recebe uma string de bits e retorna:
	# 1) Um dicionário representando o (primeiro) pacote formado por ela, incluindo os seus subPacotes.
	# 2) O resto da string que não foi utilizado para gerar esse pacote.
	bitsVersao = stringBinaria[:3] # Os três primeiros bits são o número da versão.
	versaoDoPacote = int(bitsVersao, 2)
	bitsTipo = stringBinaria[3:6] # Os três bits seguintes representam o identificador de tipo.
	idTipo = int(bitsTipo, 2)
	dicPacote = {'versao': versaoDoPacote, 'idTipo': idTipo} # Cria o dicionário final com o que já temos.
	restoDaString = stringBinaria[6:]
	if idTipo == 4: # Representa um valor literal:
		numeroBinario = ''
		chegouNoUltimoPacote = False
		while (not chegouNoUltimoPacote):
			subPacote = restoDaString[:5]
			restoDaString = restoDaString[5:]
			if subPacote[0] == '0': # É o ultimo pacote pois começa com 0.
				chegouNoUltimoPacote = True
			subPacote = subPacote[1:]
			numeroBinario += subPacote
		numeroLiteral = int(numeroBinario, 2)
		dicPacote['valor'] = numeroLiteral
		return dicPacote, restoDaString
	else: # Representa um operador (e seus operandos): 
		idTipoComprimento, restoDaString = extrairPrimeirosCaracteres(restoDaString, 1)
		dicPacote['idTipoComprimento'] =  int(idTipoComprimento) # Não precisa para resposta final.
		if idTipoComprimento == '0': # Significa que os próximos 15 bits representam o número de bits de sub-pacotes.
			comprimentoSubPacotes, restoDaString = extrairPrimeirosCaracteres(restoDaString, 15, True)
			bitsSubPacotes, restoDaString = extrairPrimeirosCaracteres(restoDaString, comprimentoSubPacotes)
			primeiroPacote, bitsSubPacotes = gerarPacoteBaseadoNosBits(bitsSubPacotes)
			subPacotes = [primeiroPacote]
			while bitsSubPacotes: # Monta próximos pacotes enquanto não foram utilizados todos os bits reservados.
				proximoPacote, bitsSubPacotes = gerarPacoteBaseadoNosBits(bitsSubPacotes)
				subPacotes.append(proximoPacote)
		else: # Significa que os próximos 11 bits representam quantos sub-pacotes tem.
			numeroSubPacotes, restoDaString = extrairPrimeirosCaracteres(restoDaString, 11, True)
			subPacotes = []
			for _ in range(numeroSubPacotes): # Monta pacotes pelo número de vezes informado.
				subPacote, restoDaString = gerarPacoteBaseadoNosBits(restoDaString)
				subPacotes.append(subPacote)
		dicPacote['subPacotes'] = subPacotes
		# Parte 2:
		if idTipo == 0: # Operador que soma os valores dos sub pacotes.
			resultado = sum(subPacote['valor'] for subPacote in subPacotes)
		elif idTipo == 1: # Operador que retorna o produto dos valores dos sub pacotes.
			produto = 1
			for subPacote in subPacotes:
				produto *= subPacote['valor']
			resultado = produto
		elif idTipo == 2: # Operador que retorna o valor mínimo dos sub pacotes.
			resultado = min(subPacote['valor'] for subPacote in subPacotes)
		elif idTipo == 3: # Operador que retorna o valor máximo dos sub pacotes.
			resultado = max(subPacote['valor'] for subPacote in subPacotes)
		elif idTipo == 5: # Operador com dois sub pacotes que retorna 1 se o primeiro for maior, 0 caso contrário.
			resultado = 1 if subPacotes[0]['valor'] > subPacotes[1]['valor'] else 0
		elif idTipo == 6: # Operador com dois sub pacotes que retorna 1 se o primeiro for menor, 0 caso contrário.
			resultado = 1 if subPacotes[0]['valor'] < subPacotes[1]['valor'] else 0
		elif idTipo == 7: # Operador com dois sub pacotes que retorna 1 se o valor de ambos é igual, 0 caso contrário..
			resultado = 1 if subPacotes[0]['valor'] == subPacotes[1]['valor'] else 0
		dicPacote['valor'] = resultado 
		return dicPacote, restoDaString

pacotePrincipal, _ = gerarPacoteBaseadoNosBits(stringEmBinario) # Monta o dicionário do pacote mais externo baseado no input.

def calcularSomaVersao(pacote): # Função recursiva que calcula a resposta para a parte 1:
	return pacote['versao'] + sum(calcularSomaVersao(subPacote) for subPacote in pacote.get('subPacotes',[]))

print('Soma dos números de versão de todos os pacotes:', calcularSomaVersao(pacotePrincipal))
print('Valor do pacote da camada mais externa:', pacotePrincipal['valor'])
