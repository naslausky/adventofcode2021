# Desafio do dia 23/12/2021:
# a) Dado um corredor com acesso a 4 salas contendo peixes, verificar qual o custo mínimo para reorganizá-los corretamente.
# b) Idem porém com cada sala tendo 4 peixes de profundidade.

class Estado: # Classe que representa um estado (organização) dos peixes nas salas e no corredor.
	def __init__(self, corredor, salas, custoAteAgora, parte2 = False):
		self.corredor = corredor # Um dicionário que relaciona o índice no corredor ao peixe que tá nessa posição no corredor (apenas ocupadas). Da forma:{0 : 'A', 3:'B'}.
		self.salas = salas  # Uma lista em que cada elemento é uma outra lista referente a cada sala. Da forma:[[A,B], [C,D],[B,A],[D,C]].
		self.custoAteAgora = custoAteAgora # Quanto foi o custo para chegar nesse estado.
		self.parte2 = parte2

	def __eq__(self,other ): # Necessário para incluir no dicionário.
		if self.corredor != other.corredor:
			return False
		for indiceSala in range(4):
			if self.salas[indiceSala] != other.salas[indiceSala]:
				return False
		return True

	def __hash__(self,): # Necessário para incluir no dicionário.
		return hash (str(self))

	def __str__(self,): # Para poder visualizar uma sala, e usado na função hash.
		corredor = ['.'] * 11
		for chave, valor in self.corredor.items():
			corredor[chave] = valor
		retorno = ''.join(corredor)
		retorno += '\n'
		linhas = ['  '] * self.quantidadeDeLinhas()
		for sala in self.salas:
			for indiceLinha in range(self.quantidadeDeLinhas()):
				linhas[indiceLinha] += sala[indiceLinha] + ' '
		for linha in linhas:
			retorno += linha + '\n'
		return retorno

	def quantidadeDeLinhas(self,): # Função que retorna o tamanho (profundidade) de cada sala.
		return 4 if self.parte2 else 2

	def salaContemApenasPeixesCorretos(self, indice): # Função que retorna se a sala contém somente os peixes destinados a ela. Usado para saber se ela serve como destino, e como origem.
		sala = self.salas[indice]
		peixeCorretoDessaSala = Estado.peixeReferenteASala(indice)
		for espaco in sala:
			if espaco != '.' and espaco != peixeCorretoDessaSala:
				return False
		return True

	def adicionaPeixeCorretoASala(self, indice): # Função que adiciona um peixe correto a sala, na primeira posição livre. Retorna a sala modificada, e quantos passos o peixe teve que dar ao entrar.
		sala = self.salas[indice].copy() # Cópia é necessária pois será usada para gerar um novo estado.
		peixeCorretoDessaSala = Estado.peixeReferenteASala(indice)
		primeiroEspacoOcupado = self.indiceDoPeixeQueVaiSair(indice)
		sala[primeiroEspacoOcupado - 1] = peixeCorretoDessaSala
		return sala, primeiroEspacoOcupado

	def indiceDoPeixeQueVaiSair(self, indice): # Função que retorna o primeiro índice ocupado de uma sala.
		indiceDoPeixeQueVaiSair = 0
		for espaco in self.salas[indice]:
			if espaco == '.':
				indiceDoPeixeQueVaiSair += 1
		return indiceDoPeixeQueVaiSair

	def taEngarrafadoNoCorredor(self, indiceOrigem, indiceDestino): # Função que retorna verdadeiro se tem algum peixe no caminho das coordenadas, falso caso contrário.
		taEngarrafado = False 
		minimo = min(indiceDestino, indiceOrigem)
		maximo = max(indiceDestino, indiceOrigem)
		for indiceCorredor in range(minimo, maximo+1):
			if indiceCorredor in self.corredor:
				if indiceCorredor != indiceOrigem: # Desconsidera se tem alguém no indice de origem pois é o próprio peixe que quer andar (i.e. ele não pode se auto-engarrafar).
					taEngarrafado = True
		return taEngarrafado

	def estadoFinal(self,): # Retorna verdadeiro se chegou na organização desejada.
		for indiceSala in range(4):
			letraDaVez = Estado.peixeReferenteASala(indiceSala)
			if self.salas[indiceSala] != [letraDaVez] * self.quantidadeDeLinhas():
				return False
		return True

	def posicoesDestinoDoCorredor(): # Função que retorna quais as posições no corredor que servem como destino. As posições a frente de uma sala não são úteis como destino.
		return (0,1,3,5,7,9,10)	
	
	def peixeReferenteASala(indiceSala): # Função que converte um índice ao seu peixe respectivo. Exemplo: 0 -> 'A'
		return chr(indiceSala+65)

	def salaDestinoDoPeixe(peixe): # Função que converte um peixe ao seu índice respectivo. Exemplo: 'A' -> 0
		return ord(peixe) - 65

	def proximosEstadosPossiveis(self): # Função que retorna um conjunto de próximos estados possíveis dado o estado atual.
		proximosEstados = [] # Verifica cada peixe para onde pode ir.
		for posicao, peixe in self.corredor.items(): # Verifica os que estão no corredor, com destino a sua sala:
			indiceSalaDestino = Estado.salaDestinoDoPeixe(peixe)
			indiceDaSalaDestinoNoCorredor = indiceSalaDestino * 2 + 2 # No corredor, a sala 0 está na posição 2.
			if self.salaContemApenasPeixesCorretos(indiceSalaDestino): # A sala está disponível como destino se possuir apenas peixes corretos:
				if not self.taEngarrafadoNoCorredor(posicao, indiceDaSalaDestinoNoCorredor): # Gera o novo estado, e adiciona ao retorno:
					novoCorredor = {chave:valor for chave, valor in self.corredor.items() if chave != posicao} # Corredor sem o peixe da vez porque ele andou.
					novasSalas = [sala.copy() for sala in self.salas]
					quantidadeDePassosNecessarios = abs(indiceDaSalaDestinoNoCorredor - posicao)
					salaComONovoPeixe, passosExtras = self.adicionaPeixeCorretoASala(indiceSalaDestino)
					novasSalas[indiceSalaDestino] = salaComONovoPeixe
					quantidadeDePassosNecessarios += passosExtras
					novoCusto = self.custoAteAgora
					novoCusto += (10**indiceSalaDestino) * quantidadeDePassosNecessarios #Custo para chegar ao novo Estado.
					novoEstado = Estado(novoCorredor, novasSalas, novoCusto, self.parte2)
					proximosEstados.append(novoEstado)

		for indiceSala, sala in enumerate(self.salas): #Verifica os das salas:
			indiceDessaSalaNoCorredor = indiceSala * 2 + 2
			indiceDoQueVaiSair = self.indiceDoPeixeQueVaiSair(indiceSala)
			quantidadeDePassosNecessarios = indiceDoQueVaiSair + 1
			if indiceDoQueVaiSair == len(sala):
				continue # Sala está vazia.
			peixeQueVaiSair = sala[indiceDoQueVaiSair]
			peixeQueEssaSalaDeveTer = Estado.peixeReferenteASala(indiceSala)
			if self.salaContemApenasPeixesCorretos(indiceSala):
				continue # Não tem porque sair com ele. Todos os peixes dessa sala pertencem a ela.
			for i in Estado.posicoesDestinoDoCorredor():
				if not self.taEngarrafadoNoCorredor(indiceDessaSalaNoCorredor, i): #Gera uma nova possibilidade de estado futuro para cada posição destino no corredor.
					novoCorredor = {chave:valor for chave, valor in self.corredor.items()}
					novoCorredor[i] = peixeQueVaiSair
					novasSalas = [sala.copy() for sala in self.salas]
					novasSalas[indiceSala][indiceDoQueVaiSair] = '.'
					quantidadeDePassosTotais = quantidadeDePassosNecessarios + abs(i - indiceDessaSalaNoCorredor)
					novoCusto = self.custoAteAgora
					novoCusto += quantidadeDePassosTotais * (10**(Estado.salaDestinoDoPeixe(peixeQueVaiSair)))
					novoEstado = Estado(novoCorredor, novasSalas, novoCusto, self.parte2)
					proximosEstados.append(novoEstado)
		return proximosEstados

	def energiaMinimaParaChegarAoFim(self): # Função que calcula o custo de energia mínimo para chegar ao estado final.
		estadosASeremTestados = [self]
		minimoDeCadaEstado = {self : 0} # Dicionário que relaciona cada estado visto até agora ao minimo que é possível chegar nele até agora.
		while estadosASeremTestados:
			proximosEstados = []
			for estado in estadosASeremTestados:
				proximosCandidatosAEstados = estado.proximosEstadosPossiveis()
				for proximo in proximosCandidatosAEstados:
					if proximo in minimoDeCadaEstado and proximo.custoAteAgora >= minimoDeCadaEstado[proximo]:
						continue # Já cheguei nesse estado com igual ou menor custo.
					minimoDeCadaEstado[proximo] = proximo.custoAteAgora
					proximosEstados.append(proximo)
			estadosASeremTestados = proximosEstados
		resposta = [minimo for estado, minimo  in minimoDeCadaEstado.items() if estado.estadoFinal()]
		return resposta[0] if resposta else 0

with open('input.txt') as file:
	linhas = file.read().splitlines()
	linhasExtrasParte2=['  #D#C#B#A#','  #D#B#A#C#'] # Linhas extras para a parte 2.
	salas = []
	salasParte2 = []
	for i in range(3,10,2):
		salas.append([linhas[2][i],linhas[3][i]])
		salasParte2.append([linhas[2][i], linhasExtrasParte2[0][i], linhasExtrasParte2[1][i], linhas[3][i]])
	estadoInicial = Estado({}, salas, 0)
	estadoInicialParte2 = Estado({}, salasParte2, 0, True)

print('Mínimo de energia necessária para chegar ao estado final:', estadoInicial.energiaMinimaParaChegarAoFim())
print('Mínimo de energia necessária para chegar ao estado final com o diagrama completo:', estadoInicialParte2.energiaMinimaParaChegarAoFim())
