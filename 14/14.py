# Desafio do dia 14/12/2021:
#a) Receber uma string e uma transformação para cada par de caracteres seguidos na string.
#   Aplicar a transformação 10 vezes e calcular os caracteres mais e menos comuns.
#b) Idem porém para 40 passos.

with open('input.txt') as file:
	linhas = file.read().splitlines()
	template = linhas[0]
	regras = linhas[2:]
	dicRegras = {} # Dicionário que relaciona um par de caracteres ao novo caracter central.
	for regra in regras:
		origem, destino = regra.split(' -> ')
		dicRegras[origem] = destino
	dicTemplate = {} # Dicionário que conta quantos de cada par de caracteres sequenciais existem.
	for indiceCaracter, caracter in enumerate(template[:-1]):
		parDeCaracteres = caracter + template[indiceCaracter+1]
		dicTemplate[parDeCaracteres] = dicTemplate.get(parDeCaracteres, 0) + 1

def calcularQuantidadeDeCaracteres(dicTemplate): # Função que recebe o dicionário e contabiliza a resposta.
	# Todos os caracteres foram contados duas vezes: "ABC" (O 'B' é contado no par 'AB' e no par 'BC')
	# Exceto o primeiro e o último da string original. Então adiciono uma unidade de cada na contagem.
	# Para no final dividir todos por dois.
	contagemCaracteres = {template[0]:1, template[-1]:1}
	for chave, valor in dicTemplate.items():
		for indiceCaracter in range(2): # Para ambos os caracteres no par:
			contagemCaracteres[chave[indiceCaracter]] = contagemCaracteres.get(chave[indiceCaracter], 0) + valor
	for chave, valor in contagemCaracteres.items(): # Divide o valor de todos por dois:
		contagemCaracteres[chave] = int(valor / 2)
	quantidadeCaracterMaisComum = max(valor for valor in contagemCaracteres.values())
	quantidadeCaracterMenosComum = min(valor for valor in contagemCaracteres.values())
	return quantidadeCaracterMaisComum - quantidadeCaracterMenosComum

for i in range(40): # Aplica 40 passos do processo.
	if i==10: # Imprime a resposta da parte 1:
		print('Diferença entre os caracteres após 10 passos:', calcularQuantidadeDeCaracteres(dicTemplate))
	novoTemplate = {} # Cada par de caracteres gera dois novos pares após um passo.
	for parDeCaracteres in dicTemplate:
		if parDeCaracteres in dicRegras:
			caracterCentral = dicRegras[parDeCaracteres]
			parEsquerda = parDeCaracteres[0] + caracterCentral
			parDireita = caracterCentral + parDeCaracteres[1]
			for chave in (parEsquerda, parDireita): # Incrementa a contagem dos dois novos pares de caracteres.
				novoTemplate[chave] = novoTemplate.get(chave, 0) + dicTemplate[parDeCaracteres]
		else: # Creio não precisar, mas poderia ocorrer de um par não ter uma regra de transformação.
			novoTemplate[parDeCaracteres] = dicTemplate[parDeCaracteres]
	dicTemplate = novoTemplate
print('Diferença entre os caracteres após 40 passos:', calcularQuantidadeDeCaracteres(dicTemplate))
