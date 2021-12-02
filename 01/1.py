#Desafio do dia 01/12/2021:
#a) Dada uma lista de números, contar quantas vezes o número foi maior que seu antecessor.
#b) Idem, porém para uma janela móvel de 3 números na mesma lista.

with open('input.txt') as file:
	numeros = file.read().splitlines()
	numeros = list(map(int,numeros))
resposta = 0
for i in range(1,len(numeros)):
	if numeros[i]>numeros[i-1]:
		resposta+=1
print("Número de elementos maiores que os antecessores:", resposta)

#Parte 2:
resposta = 0
somaAnterior=sum(numeros[:3])
for i in range(2,len(numeros)):
	soma = sum(numeros[i-2:i+1])
	if soma>somaAnterior:
		resposta+=1
	somaAnterior=soma
print("Número de janelas de 3 elementos maiores que as anteriores:", resposta)
