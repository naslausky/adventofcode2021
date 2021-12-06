# Desafio do dia 06/12/2021:
#a) Dada uma lista de células e quantos dias cada uma precisa para se multiplicar, calcular quantas células existirão após 80 dias.
#b) Idem, porém para 256 dias.

with open('input.txt') as file:
	entrada = file.read()
	# Dicionário que relaciona quantos peixes estão em cada época.
	# Como as chaves são simples (0..8), poderia ser uma lista também.
	dicPeixes = {i:entrada.count(str(i))  for i in range(9)}
for _ in range(256): # Calcula o dicionário do dia seguinte baseado no atual.
	if _ == 80: # A parte 1 são só 80 dias.
		qtdPeixes = sum([x for x in dicPeixes.values()])
		print("Número de peixes após 80 dias:", qtdPeixes)
	dicDiaSeguinte = {i:dicPeixes.get(i+1,0) for i in range(9)}
	dicDiaSeguinte[8] = dicPeixes.get(0,0)
	dicDiaSeguinte[6] = dicDiaSeguinte.get(6,0) + dicPeixes.get(0,0)
	dicPeixes = dicDiaSeguinte

qtdPeixes = sum([x for x in dicPeixes.values()])
print("Número de peixes após 256 dias:", qtdPeixes)
