with open('smallinput.txt') as file:
	linhas = file.read().splitlines()
	templateOriginal = template = linhas[0]
	regras = linhas[2:]
	dicRegras = {}
	for regra in regras:
		origem, destino = regra.split(' -> ')
		dicRegras[origem] = destino

for i in range(10): # Aplica 10 passos do processo.
	print("Aplicando passo:", i)
	novoTemplate = ''
	for indiceCaracter, caracter in enumerate(template[:-1]):
		novoTemplate+=caracter
		origem = caracter+template[indiceCaracter+1]
		novoTemplate += dicRegras.get(origem, '')
	novoTemplate += template[-1]
	template = novoTemplate
quantidadeCaracterMaisComum = max(template.count(char) for char in template)
quantidadeCaracterMenosComum = min(template.count(char) for char in template)
print(quantidadeCaracterMaisComum - quantidadeCaracterMenosComum)
