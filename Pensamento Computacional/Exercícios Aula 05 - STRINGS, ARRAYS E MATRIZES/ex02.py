"""Considere uma turma de n alunos onde desejamos calcular a média das notas da prova semestral
 e saber quantas notas estão iguais, acima e abaixo dessa média.
  ▪ Escreva um algoritmo que lê um inteiro n representando a quantidade de alunos
e cada uma das n notas e mostra a média da turma, quantas notas são iguais, acima e abaixo da média da turma. """

students = int(input("Digite o número de alunos: "))

grades = [None] * students
total = 0
mean = 0
above = 0
less = 0
equal = 0

for i in range(len(grades)):
    grades[i] = int(input("Digite a nota: "))

for i in grades:
    total += i
    mean = total / len(grades)

for i in range(len(grades)):
    if grades[i] > mean:
        above += 1

    if grades[i] < mean:
        less += 1

    for j in range(i+1, len(grades), 1):
        if grades[i] == grades[j]:
            equal += 1

print(mean, above, less, equal)