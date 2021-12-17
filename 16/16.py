with open('input.txt') as file:
	linha = file.read().splitlines()[0]
	#linha = 'D2FE28' #primeiro caso
	#linha = '38006F45291200'
	#linha = 'EE00D40C823060'
	#linha = '8A004A801A8002F478'
	#linha = '620080001611562C8802118E34'
	#linha = 'C0015000016115A2E0802F182340'
	#linha = 'A0016C880162017C3686B18A3D4780'
#	print(linha)
	linha = '1'+linha # Gambiarra pra incluir os zeros iniciais.
	numeroHexadecimal = int(linha,16)
	stringEmBinario = bin(numeroHexadecimal)[3:] # Exclui o 0b e o 1 inicial que eu coloquei na gambiarra.
	#while stringEmBinario[-1] == '0':
	#	stringEmBinario = stringEmBinario[:-1] # Descarta os zeros ao final do pacote mais externo.
	#print(stringEmBinario)
	#print('00111000000000000110111101000101001010010001001000000000')
	#input()	

def gerarPacoteBaseadoNosBits(stringBinaria):
	bitsVersao = stringBinaria[:3]
	versaoDoPacote = int(bitsVersao, 2)
	bitsTipo = stringBinaria[3:6]
	idTipo = int(bitsTipo, 2)
	dicPacote = {'versao': versaoDoPacote, 'idTipo': idTipo}
	restoDaString = stringBinaria[6:]
	#print('DicAtéAgora:', dicPacote)
	if idTipo == 4: # Valor literal:
	#	print('idTipo', idTipo)
		numeroBinario = ''
	#	input()
		chegouNoUltimoPacote = False
		while (not chegouNoUltimoPacote):
			subPacote = restoDaString[:5]
			restoDaString = restoDaString[5:]
			if subPacote[0] == '0': #É o ultimo pacote
				chegouNoUltimoPacote = True
			subPacote = subPacote[1:]
			numeroBinario += subPacote
		numeroLiteral = int(numeroBinario, 2)
		dicPacote['valorLiteral'] = numeroLiteral
		return dicPacote, restoDaString
	else: # Operador:
		
		idTipoComprimento = restoDaString[0]
		restoDaString = restoDaString[1:]
		dicPacote['idTipoComprimento'] =  int(idTipoComprimento)
		if idTipoComprimento == '0':
	#		print('entrou id comprimento 0')
			comprimentoSubPacotes = restoDaString[:15]
			restoDaString = restoDaString[15:]
			comprimentoSubPacotes = int(comprimentoSubPacotes, 2)
			
			bitsSubPacotes = restoDaString[:comprimentoSubPacotes]
			restoDaString = restoDaString[comprimentoSubPacotes:]

			#if (bitsSubPacotes):
			primeiroPacote, bitsSubPacotes = gerarPacoteBaseadoNosBits(bitsSubPacotes)
			subPacotes = [primeiroPacote]
			while bitsSubPacotes:
				proximoPacote, bitsSubPacotes = gerarPacoteBaseadoNosBits(bitsSubPacotes)
				subPacotes.append(proximoPacote)
			dicPacote['subPacotes'] = subPacotes
			return dicPacote, restoDaString
		else:
			numeroSubPacotes = restoDaString[:11]
			restoDaString = restoDaString[11:]
			numeroSubPacotes = int(numeroSubPacotes, 2)
			subPacotes = []
			for _ in range(numeroSubPacotes):
				subPacote, restoDaString = gerarPacoteBaseadoNosBits(restoDaString)
				subPacotes.append(subPacote)
			dicPacote['subPacotes'] = subPacotes
			return dicPacote, restoDaString

pacotePrincipal, _ = gerarPacoteBaseadoNosBits(stringEmBinario)

def calcularSomaVersao(pacote):
	return pacote['versao'] + sum(calcularSomaVersao(subPacote) for subPacote in pacote.get('subPacotes',[]))

print(calcularSomaVersao(pacotePrincipal))


