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

def calcularQuantidadeDeCaracteres(dicTemplate): # Função que recebe o dicionário e contabiliza a resposta

	pass

for i in range(40): # Aplica 40 passos do processo.
	novoTemplate = {}
	for parDeCaracteres in dicTemplate:
		if parDeCaracteres in dicRegras:
			caracterCentral = dicRegras[parDeCaracteres]
			parEsquerda = parDeCaracteres[0] + caracterCentral
			parDireita = caracterCentral + parDeCaracteres[1]
			novoTemplate[parEsquerda] = novoTemplate.get(parEsquerda, 0) + dicTemplate[parDeCaracteres]
			novoTemplate[parDireita] = novoTemplate.get(parDireita, 0) +  dicTemplate[parDeCaracteres]
		else: 
			novoTemplate[parDeCaracteres] = dicTemplate[parDeCaracteres]
	dicTemplate = novoTemplate

contagemCaracteres = {template[0]:1, template[-1]:1}
for chave, valor in dicTemplate.items():
	for indiceCaracter in range(2):
		contagemCaracteres[chave[indiceCaracter]] = contagemCaracteres.get(chave[indiceCaracter], 0) + valor
for chave, valor in contagemCaracteres.items():
	contagemCaracteres[chave] = int(valor / 2)
quantidadeCaracterMaisComum = max(valor for valor in contagemCaracteres.values())
quantidadeCaracterMenosComum = min(valor for valor in contagemCaracteres.values())
print(quantidadeCaracterMaisComum - quantidadeCaracterMenosComum)
