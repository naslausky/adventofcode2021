#Desafio do dia 03/12/2021
#a) Dada uma lista de números binários de mesmo comprimento, calcular para cada posição qual o valor mais e menos comum.
#b) Dada a mesma lista, ir filtrando apenas os números que contém o elemento mais ou menos comum e calcular o produto do último a sobrar.

with open('input.txt') as file:
	numeros = file.read().splitlines()
taxaGamma = ''
taxaEpsilon = ''
numerosPossiveisOxigenio = numeros[:]
numerosPossiveisCO2 = numeros[:]
for indiceCaracter in range(len(numeros[0])): #Pelo enunciado todos tem mesmo tamanho
	contagemDe1s = len([numero 
			for numero in numeros 
			if numero[indiceCaracter]=='1'])
	bitMaisComum = '1' if contagemDe1s > len(numeros)/2 else '0'
	taxaGamma+=bitMaisComum
	numeroInverso = '0' if bitMaisComum == '1' else '1'
	taxaEpsilon+=numeroInverso
#Parte 2:
	contagemDe1sOxigenio = len([numero #Verificação do bit mais comum apenas dentre os números de O2 que sobraram.
			for numero in numerosPossiveisOxigenio 
			if numero[indiceCaracter]=='1'])
	contagemDe1sCO2 = len([numero 
			for numero in numerosPossiveisCO2 
			if numero[indiceCaracter]=='1'])
	bitMaisComumOxigenio = '1' if contagemDe1sOxigenio >= len(numerosPossiveisOxigenio) / 2 else '0'
	bitMenosComumCO2 = '0' if contagemDe1sCO2 >= len(numerosPossiveisCO2) / 2 else '1'
	if len(numerosPossiveisOxigenio) > 1:
		numerosPossiveisOxigenio = [numero 
						for numero in numerosPossiveisOxigenio
						if numero[indiceCaracter] == bitMaisComumOxigenio]
	if len(numerosPossiveisCO2) > 1:
		numerosPossiveisCO2 = [numero 
						for numero in numerosPossiveisCO2
						if numero[indiceCaracter] == bitMenosComumCO2]
taxaEpsilonBase10 = int(taxaEpsilon, 2)
taxaGammaBase10 = int(taxaGamma,2)
print("O consumo de energia do submarino é de:", taxaEpsilonBase10*taxaGammaBase10)
#Parte 2:
numeroFinalOxigenio = int(numerosPossiveisOxigenio[0],2)
numeroFinalCO2 = int(numerosPossiveisCO2[0],2)
produto = numeroFinalOxigenio * numeroFinalCO2
print('A taxa de suporte de vida desse submarino é:', produto)	
