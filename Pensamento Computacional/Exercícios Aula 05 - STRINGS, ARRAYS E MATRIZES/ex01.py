"""▪ Escreva um algoritmo que recebe um número inteiro n > 0,
 cria um vetor de números reais com n posições e preenche o vetor com n números aleatórios reais.
  ▪ Depois de preenchido o vetor, imprima na tela todos os números gerados. """

import random

n = int(input("Digite um numero inteiro maior que 0: "))

num = [None] * n

for i in range(0, len(num), 1):
    num[i] = random.random()

print(num)

#for i in range(n):
#    teste.append(random.random())
#print(teste)