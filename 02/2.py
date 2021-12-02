#Desafio do dia 02/12/2021
#a) Receber uma série de instruções de deslocamento e calcular a posição final.
#b) Idem porém mudando o significado de um dos comandos.
with open('input.txt') as file:
	instrucoes = file.read().splitlines()

posicaoHorizontal = profundidade = profundidade2 = alvo = 0
for instrucao in instrucoes:
	comando, numero = instrucao.split()
	numero = int(numero)
	if "forward" in comando:
		posicaoHorizontal += numero
		#Parte 2:
		profundidade2 += alvo * numero
	elif "down" in comando:
		profundidade += numero
		alvo += numero
	elif "up" in comando:
		profundidade -= numero
		alvo -= numero

print("O produto da profundidade com a distância é de:", profundidade*posicaoHorizontal)
print("Utilizando o segundo significado das instruções o produto é:", profundidade2*posicaoHorizontal)
