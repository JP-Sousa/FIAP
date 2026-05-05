"""▪ Escreva um algoritmo que lê um número inteiro n,
 cria um vetor de inteiros de tamanho n, faz a leitura de um conjunto de n números inteiros armazenando-os no vetor
  e depois calcula a somatória dos números contidos no vetor.
▪ Dica: note que a somatória deverá ser feita após o vetor estar preenchido."""

n = int(input("Digite o tamanho do vetor: "))

num = [None] * n
soma = 0

for i in range(n):
    num[i] = int(input("Digite um número: "))
    soma += num[i]

print(soma)