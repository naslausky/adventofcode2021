class Estado:
	def __init__(self, corredor, salas, custoAteAgora):
		self.corredor = corredor #Um dicionário que relaciona o índice no corredor ao peixe que tá nessa posição no corredor (apenas ocupadas). # {0 : 'A', 3:'B'}
		self.salas = salas  #Uma lista em que cada elemento é uma outra lista referente a uma sala. # [[A,B], [C,D],[B,A],[D,C]]
		self.custoAteAgora = custoAteAgora #Quanto é o custo para chegar nesse estado.

	def __eq__(self,other ): #Para poder ser incluído e comparável no dicionário.
		if self.corredor != other.corredor:
			return False
		for indiceSala in range(4):
			if self.salas[indiceSala] != other.salas[indiceSala]:
				return False
		return True

	def __hash__(self,): #Para poder ser incluído e comparável no dicionário
		#hash((self.corredor,tuple(tuple(sala) for sala in self.salas)))
		return hash (str(self))

	def __str__(self,): #A princípio para debugar, mas depois usado como é usado como um identificador de estado na função Hash, foi removida a print do custo.
		#retorno = 'Custo atual: ' + str(self.custoAteAgora) + '\n'
		corredor = ['.'] * 11
		for chave, valor in self.corredor.items():
			corredor[chave] = valor
		retorno = ''.join(corredor)
		retorno += '\n'
		primeiraLinha = '  '
		segundaLinha = '  '
		for sala in self.salas:
			primeiraLinha += sala[0] + ' '
			segundaLinha += sala[1] + ' '
		return retorno + primeiraLinha + '\n' + segundaLinha + '\n'

	def taEngarrafadoNoCorredor(self, indiceOrigem, indiceDestino): #Função que retorna verdadeiro se tem algum peixe no caminho das coordenadas, falso caso contrário:
		taEngarrafado = False 
		minimo = min(indiceDestino, indiceOrigem)
		maximo = max(indiceDestino, indiceOrigem)
		for indiceCorredor in range(minimo, maximo+1):
			if indiceCorredor in self.corredor:
				if indiceCorredor != indiceOrigem: #Desconsidera se tem alguém no indiceOrigem pois é o próprio peixe que quer andar (ele não pode se auto-engarrafar)
					taEngarrafado = True
		return taEngarrafado

	def estadoFinal(self,): #Retorna verdadeiro se chegou na organização desejada.
		for indiceSala in range(4):
			letraDaVez = chr(65+indiceSala)
			if self.salas[indiceSala] != [letraDaVez, letraDaVez]:
				return False
		return True

	def posicoesDestinoDoCorredor(): #Função que retorna quais as posições no corredor que servem como destino.
		return (0,1,3,5,7,9,10)	

	def proximosEstadosPossiveis(self): #Função que retorna um conjunto de próximos estados possíveis dado o estado atual.
		proximosEstados = []
		#Verifica cada peixe para onde pode ir.
		for posicao, peixe in self.corredor.items(): #Verifica os do corredor:
			indiceSalaDestino = ord(peixe) - 65
			indiceDaSalaDestinoNoCorredor = indiceSalaDestino * 2 + 2 #No corredor, a sala 0 está na posição 2.
			if (self.salas[indiceSalaDestino][1]=='.' or  #Para a sala estar disponível como destino, a posição de baixo precisa estar vazia (e consequentemente a de cima), ou
				(self.salas[indiceSalaDestino][0]=='.' and  #A de cima precisa estar vazia, e a de baixo precisa já ter o peixe correto.
				self.salas[indiceSalaDestino][1]==peixe)) : #Se a sala tiver disponível, vê se o caminho pelo corredor tá vazio:
				if not self.taEngarrafadoNoCorredor(posicao, indiceDaSalaDestinoNoCorredor):
					#Gera o novo estado, e adiciona ao retorno:
					novoCorredor = {chave:valor for chave, valor in self.corredor.items() if chave != posicao} #Corredor sem o peixe da vez porque ele andou.
					novasSalas = [sala.copy() for sala in self.salas]
					quantidadeDePassosNecessarios = abs(indiceDaSalaDestinoNoCorredor - posicao)
					if self.salas[indiceSalaDestino][1] == '.':
						novasSalas[indiceSalaDestino][1] = peixe
						quantidadeDePassosNecessarios += 2
					else:
						novasSalas[indiceSalaDestino][0] = peixe
						quantidadeDePassosNecessarios += 1
					novoCusto = self.custoAteAgora
					novoCusto += (10**indiceSalaDestino) * quantidadeDePassosNecessarios #Custo para chegar ao novo Estado.
					novoEstado = Estado(novoCorredor, novasSalas, novoCusto)
					proximosEstados.append(novoEstado)

		for indiceSala, sala in enumerate(self.salas): #Verifica os das salas:
			indiceDessaSalaNoCorredor = indiceSala * 2 + 2
			if sala[0] != '.': #Cada sala pode sair o que está mais na frente. Nesse caso, sai o de cima: #Dá pra substituir por um for no futuro
				indiceDoQueVaiSair = 0
				quantidadeDePassosNecessarios = 1
			elif sala[1] != '.': #Sai o de baixo:
				indiceDoQueVaiSair = 1
				quantidadeDePassosNecessarios = 2
			else:
				continue #Sala tá vazia, não vai sair ninguém.
			peixeQueVaiSair = sala[indiceDoQueVaiSair]
			peixeQueEssaSalaDeveTer = chr(indiceSala+65)
			if peixeQueVaiSair == peixeQueEssaSalaDeveTer:
				if indiceDoQueVaiSair == 0 and sala[1] != peixeQueEssaSalaDeveTer:
					pass #Mesmo o peixe da frente estando certo, ele tem que sair da frente porque o de trás tá errado.
				else:
					continue #O peixe já tá na sala certa. 
			for i in Estado.posicoesDestinoDoCorredor():
				if not self.taEngarrafadoNoCorredor(indiceDessaSalaNoCorredor, i): #Gera uma nova possibilidade de estado futuro para cada posição destino no corredor.
					novoCorredor = {chave:valor for chave, valor in self.corredor.items()}
					novoCorredor[i] = peixeQueVaiSair
					novasSalas = [sala.copy() for sala in self.salas]
					novasSalas[indiceSala][indiceDoQueVaiSair] = '.'
					quantidadeDePassosTotais = quantidadeDePassosNecessarios + abs(i - indiceDessaSalaNoCorredor)
					novoCusto = self.custoAteAgora
					novoCusto += quantidadeDePassosTotais * (10**(ord(peixeQueVaiSair)-65))
					novoEstado = Estado(novoCorredor, novasSalas, novoCusto)
					proximosEstados.append(novoEstado)
		return proximosEstados
					

with open('input.txt') as file:
	linhas = file.read().splitlines()
	
	salas = []
	for i in range(3,10,2):
		salas.append([linhas[2][i],linhas[3][i]])
	estadoInicial = Estado({},salas, 0)
#print(estadoInicial)
#print('______________________')
#a = estadoInicial.proximosEstadosPossiveis()[16].proximosEstadosPossiveis()[2].proximosEstadosPossiveis()[0].proximosEstadosPossiveis()[2].proximosEstadosPossiveis()[0].proximosEstadosPossiveis()[2].proximosEstadosPossiveis()[0].proximosEstadosPossiveis()[0].proximosEstadosPossiveis()[0].proximosEstadosPossiveis()[0].proximosEstadosPossiveis()[0].proximosEstadosPossiveis()[0]
#print(a.taEngarrafadoNoCorredor())
#print(a,a.custoAteAgora)
#[print(x, x.custoAteAgora) for x in a]
#print('______________________')
#b = estadoInicial.proximosEstadosPossiveis()[14].proximosEstadosPossiveis()[5]
#print(b)
#print('______________________')
#conjunto = set()
#print('hashes:')
#print(a.__hash__())
#print(b.__hash__())
#conjunto.add(a)
#conjunto.add(b)
#dicionario = {}
#dicionario[a]=0
#dicionario[b]=0
#print(dicionario)
#print(conjunto)
#estadoTeste = Estado({5:'A'}, [           ['.','.'],              ['.','.'],           ['.','.'],           ['.','.']         ], 0)
#estadoTeste = Estado({}, [           ['A','A'],              ['B','B'],           ['C','C'],           ['D','D']         ], 0)
#print(estadoTeste)
#print(estadoTeste.taEngarrafadoNoCorredor(5,2))
#teste = estadoInicial.proximosEstadosPossiveis()[3]
#teste = teste.proximosEstadosPossiveis()[0]
#print(teste)
#print('______________________')
#[print(sala) for sala in estadoTeste.proximosEstadosPossiveis()]
#print('______________________')
#minimo = 14000
#input()
minimo = 20000
estadosASeremTestados = [estadoInicial]
minimoDeCadaEstado = {estadoInicial : 0} #Dicionário que relaciona cada estado ao minimo que é possível chegar nele visto até agora.
while estadosASeremTestados:
#	print(len(estadosASeremTestados))
	proximosEstados = []
	for estado in estadosASeremTestados:
		proximosCandidatosAEstados = estado.proximosEstadosPossiveis()
		for proximo in proximosCandidatosAEstados:
			if proximo in minimoDeCadaEstado and proximo.custoAteAgora >= minimoDeCadaEstado[proximo]:
				continue #Já cheguei nesse estado com igual ou menor custo.
			minimoDeCadaEstado[proximo] = proximo.custoAteAgora
			proximosEstados.append(proximo)
			if proximo.estadoFinal():
				minimo = min(minimo, proximo.custoAteAgora)#Descobrir porque que não tá funcionando olhar no dicionário
	estadosASeremTestados = proximosEstados
#	print('Resposta:', [x.custoAteAgora for x in minimoDeCadaEstado if x.estadoFinal()])

print(minimo)
