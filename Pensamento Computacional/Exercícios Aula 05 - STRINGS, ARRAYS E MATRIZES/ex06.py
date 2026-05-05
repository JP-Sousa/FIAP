"""Escreva um algoritmo que lê um número inteiro n > 0
 e preenche um vetor de caracteres de n posições.
  ▪ Depois de preencher o vetor, você deverá inverter o seu conteúdo,
   ou seja, trocar o conteúdo da primeira posição (0) com a ´ultima (n − 1)
    a segunda com a penúltima e assim por diante até que o vetor esteja invertido. """

frase = input("Digite algo: ")

for i in range(len(frase)-1, -1, -1):
    print(frase[i], end="")